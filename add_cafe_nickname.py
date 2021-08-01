import csv
from constants import DIRNAME

target_dir = DIRNAME
official_member_list_file = "조합원 리스트 - 조합원 리스트.csv"
cafe_member_file = "카페가입신청-20210616.csv"
outfile = "조합원리스트카페가입확인체크오프.csv"

max_member = 10000

# query selector for cafe member registration form
# email: document.querySelectorAll('td > div > div > ol > li:nth-child(1) > p').forEach(e => x.push(e.innerText))
# nickname: document.querySelectorAll('td:nth-child(2) > div > a').forEach(e => x.push(e.innerText))

cafe_member_email = []
cafe_member_nickname = []

with open(target_dir + "/" + cafe_member_file, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        cafe_member_email.append(row[0])
        cafe_member_nickname.append(row[1])


with open(target_dir + "/" + official_member_list_file, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    hit_list = []

    f = open(target_dir + "/" + outfile, 'w', newline='', encoding='utf-8')

    for row in csvreader:
        row_to_be_written = row[5] + ',' + row[6]

        for index, email in enumerate(cafe_member_email):
            if index > max_member:
                break

            if row[3] == email:
                hit_list.append(email)
                if row[5] == "" and row[6] == "":
                    print('Writing nickname: ', cafe_member_nickname[index])
                    row_to_be_written = '승인완료,' + cafe_member_nickname[index]
                else:
                    # If already a member, leave the content
                    print('Already a member', row)

        f.write(row_to_be_written + '\n')

    for index, email in enumerate(cafe_member_email):
        if email not in hit_list:
            print('Not in list: ', email, cafe_member_nickname[index])

print('total: {}, hit count: {}'.format(len(cafe_member_nickname), len(hit_list)))
