import csv

target_dir = "DO_NOT_COMMIT_THIS_DIR"

# Input files
official_member_list_file = "조합원 리스트 - 조합원 리스트.csv"
online_submission = "가입 신청서 응답 (온라인 제출) - 설문지 응답 시트1.csv"

# Output files
output_filename = "address List (in order of member id).csv"

member_list = []
member_list_from_online = []

# 조합원 리스트 - 조합원 리스트.csv 열 정보
COL_NAME = 1
COL_BIRTH = 2
COL_EMAIL = 3
COL_PHONE = 7
COL_ADDRESS_WORK = 18
COL_ADDRESS_HOME = 19
COL_TEAM = 20

# 구글폼 온라인 열 정보
GOOG_ONLINE_COL_NAME = 1
GOOG_ONLINE_COL_EMAIL = 3
GOOG_ONLINE_COL_ADDRESS_HOME = 16
GOOG_ONLINE_COL_TEAM = 17
GOOG_ONLINE_COL_ADDRESS_WORK = 18

with open(target_dir + "/" + online_submission, newline='', encoding='utf-8') as online_members_csvfile:
    member_reader = csv.reader(online_members_csvfile)

    for member_row in member_reader:
        member_list_from_online.append(member_row)

fd = open(target_dir + "/" + output_filename, 'w', encoding='utf-8')

with open(target_dir + "/" + official_member_list_file, newline='', encoding='utf-8') as members_csvfile:
    member_reader = csv.reader(members_csvfile)
    total_count = 0
    not_found_count = 0
    already_added_count = 0
    added_count = 0

    for member_row in member_reader:
        member_name = member_row[COL_NAME]
        member_birth = member_row[COL_BIRTH]
        member_email = member_row[COL_EMAIL]
        member_phone = member_row[COL_PHONE]
        member_address_work = member_row[COL_ADDRESS_WORK]
        member_address_home = member_row[COL_ADDRESS_HOME]
        member_team = member_row[COL_TEAM]

        written = False

        if (member_email == ''):
            # print("End of list")
            break

        total_count += 1

        # Already added
        if member_address_work != '' and len(member_row) > COL_ADDRESS_WORK:
            already_added_count += 1
            fd.write("{},{},{}\n".format(
                member_name.replace('\n', '').replace('\r', '').replace(',', ' '),
                member_address_work.replace('\n', '').replace('\r', '').replace(',', ' '),
                member_team.replace('\n', '').replace('\r', '').replace(',', ' '))
            )
            continue

        # Check each file using email as key
        for online_member in member_list_from_online:
            if member_email == online_member[GOOG_ONLINE_COL_EMAIL]:
                fd.write("{},{},{}\n".format(
                    member_name.replace('\n', '').replace('\r', '').replace(',', ' '),
                    online_member[GOOG_ONLINE_COL_ADDRESS_WORK].replace('\n', '').replace('\r', '').replace(',', ' '),
                    online_member[GOOG_ONLINE_COL_TEAM].replace('\n', '').replace('\r', '').replace(',', ' '))
                )
                written = True
                break

        if written:
            added_count += 1
        else:
            print("Cannot find:", member_row)
            fd.write(member_name + ",\n")
            not_found_count += 1

    print('Total: {}, Added: {}, Not found: {}, Already added: {}'.format(total_count, added_count, not_found_count, already_added_count))

