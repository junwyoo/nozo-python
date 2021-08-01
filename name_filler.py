from constants import DIRNAME

google_form_upload = "가입 신청서 응답 (업로드).csv"
google_form_github_submission = "가입 신청서 응답 (온라인 제출).csv"
compressed_list = open(DIRNAME + "/" + "간이 리스트.csv", newline='', encoding='utf-8')

# def find_by_email(email):
#     print("Searching for email: " + email)

#     csvreader = csv.reader(comporessed_list)
#     matches = []

#     for index, row in enumerate(csvreader):
#         if (row[1] == email):
#             matches.append(row)

#     comporessed_list.seek(0)

#     return matches

# # If either name or birthday is missing, try finding them by email
# if (not name or not bday):
#     match = find_by_email(row[3])
#     print(match)
#     replaceCount += 1

#     if (len(match) > 0):
#         print(row[0] + "," + match[0][0] + "," + match[0][2] + "\n")
#         fd.write(row[0] + "," + match[0][0] + "," + match[0][2] + "\n")
#         continue