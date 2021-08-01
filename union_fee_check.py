import os
import csv
from constants import DIRNAME

# 납부 기준일까지 가입한 조합원 리스트
member_list_file_name = "조합원 리스트 - 납부자 리스트.csv"
# 말일까지의 거래내역
transaction_file_name = "거래내역조회_입금_20210707.csv"
# Output file
output_file_name = "조합비 납부 내역_temp.csv"

# 납부 리스트 열 상수
COL_MEMBER_NO = 0
COL_MEMBER_NAME = 1
COL_MEMBER_BIRTH = 2
COL_MEMBER_PHONE = 3
COL_MEMBER_EMAIL = 4
COL_MEMBER_CAFE_NICKNAME = 6

member_list = []
paid_list = []
paid_excessively = []
duplicate_list = []

with open(DIRNAME + "/" + member_list_file_name, newline='', encoding='utf-8') as members_csvfile:
    member_reader = csv.reader(members_csvfile)
    noname_count = 0

    for member_row in member_reader:
        member_name = member_row[COL_MEMBER_NAME]

        if (member_name == ''):
            noname_count += 1

        # No., 이름, 생년월일, 이메일 주소, 카페 닉네임 (아이디), 핸드폰 번호
        member_list.append([
            member_row[COL_MEMBER_NO],
            member_name,
            member_row[COL_MEMBER_BIRTH],
            member_row[COL_MEMBER_EMAIL],
            member_row[COL_MEMBER_CAFE_NICKNAME],
            member_row[COL_MEMBER_PHONE]
        ])

    print("members with name: ", len(member_list))
    print("members without name: ", noname_count)

with open(DIRNAME + "/" + transaction_file_name, newline='', encoding='utf-8') as transactions_csv:
    transaction_reader = csv.reader(transactions_csv)
    total_count = 0

    for transaction_row in transaction_reader:
        # Trim name and number
        transaction_name = ""
        last_four_digit = ""

        for char in transaction_row[2]:
            if char.isalpha():
                transaction_name += char
            elif char.isdigit():
                last_four_digit += char

        # spendings
        if int(transaction_row[3]) > 0:
            continue

        # Income
        amount = int(transaction_row[4])

        total_count += 1
        paid_enough = amount >= 30000

        if paid_enough:
            paid_list.append([transaction_name, last_four_digit])

        if amount > 30000:
            paid_excessively.append([transaction_name, last_four_digit, amount - 30000])

    print("Total:", total_count, "| Paid Enough:", len(paid_list), "| Paid Excessive:", len(paid_excessively))

with open(DIRNAME + "/" + output_file_name, 'w', encoding='utf-8') as fd:
    not_in_list_count = 0
    in_list_count = 0
    dup_found_count = 0
    no_name_count = 0

    # 전체 조합원 리스트
    for member in member_list:
        member_name = member[1]

        if member_name == "":
            no_name_count += 1
            fd.write(member[0] + "," + member[1] + "," + member[2] + "," + member[3] + "," + member[4] + "," + member[5] + ",False\n")
            continue

        candidate = []
        for paid_person in paid_list:
            if member_name == paid_person[0]:
                candidate.append(paid_person)
            elif member_name in paid_person[0]:
                # Only partly match
                print("Partially matches name", paid_person)
                candidate.append(paid_person)

        if len(candidate) == 0:
            # Name match 0
            not_in_list_count += 1
            fd.write(member[0] + "," + member[1] + "," + member[2] + "," + member[3] + "," + member[4] + "," + member[5] + ",False\n")
        elif len(candidate) == 1:
            # Name match only one
            in_list_count += 1
            fd.write(member[0] + "," + member[1] + "," + member[2] + "," + member[3] + "," + member[4] + "," + member[5] + ",True\n")
        else:
            # Name matches more than one
            member_hit = []

            for x in candidate:
                # compare if last four digits match
                if x[1] != "" and member[5] != "" and x[1] == member[5][-4:]:
                    member_hit.append(x)

            if len(member_hit) > 0:
                # Same person, submitted multiple times
                in_list_count += 1
                fd.write(member[0] + "," + member[1] + "," + member[2] + "," + member[3] + "," + member[4] + "," + member[5] + "".join(",True" for i in member_hit) + "\n")
                continue

            # Found same names with different phone numbers
            fd.write(member[0] + "," + member[1] + "," + member[2] + "," + member[3] + "," + member[4] + "," + member[5] + ",Either: " + "".join("|" + str(x[0]) + str(x[1]) for x in candidate) + "\n")
            duplicate_list.append("Either: " + "".join("|" + str(x[0]) + str(x[1]) for x in candidate))
            dup_found_count += 1


    print("No name:", no_name_count, "| Not paid:", not_in_list_count, "| Paid:", in_list_count, "| same name different person: ", dup_found_count)

    for duplicate in duplicate_list:
        print(duplicate)

    for member in paid_excessively:
        print("Paid more:", member)
