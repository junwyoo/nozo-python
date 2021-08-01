import csv

target_dir = "DO_NOT_COMMIT_THIS_DIR"
official_member_list_file = "조합원 리스트 - 조합원 리스트.csv"
upload_submission = "가입 신청서 응답 (업로드) - 설문지 응답 시트1.csv"
online_submission = "가입 신청서 응답 (온라인 제출) - 설문지 응답 시트1.csv"
output_filename = "Phone List (in order of member id).csv"

member_list = []
member_list_from_upload = []
member_list_from_online = []

with open(target_dir + "/" + upload_submission, newline='', encoding='utf-8') as upload_members_csvfile:
    member_reader = csv.reader(upload_members_csvfile)

    for member_row in member_reader:
        member_list_from_upload.append(member_row)

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
        member_name = member_row[1]
        member_birth = member_row[2]
        member_email = member_row[3]
        member_phone = member_row[7]

        written = False

        if (member_email == ''):
            print("End of list")
            break

        total_count += 1

        # Already added
        if member_phone != '':
            already_added_count += 1
            fd.write(member_name + "," + str(member_phone) + "\n")
            continue

        # Check each file using email as key
        for online_member in member_list_from_online:
            if member_email == online_member[3]:
                fd.write(online_member[1] + "," + str(online_member[4]) + "\n")
                written = True
                break

        if not written:
            for upload_member in member_list_from_upload:
                if member_email == upload_member[3]:
                    fd.write(upload_member[1] + "," + str(upload_member[4]) + "\n")
                    written = True
                    break

        if written:
            added_count += 1
        else:
            print("Cannot find:", member_row)
            fd.write(member_name+ ",\n")
            not_found_count += 1

    print('Total: {}, Added: {}, Not found: {}, Already added: {}'.format(total_count, added_count, not_found_count, already_added_count))

