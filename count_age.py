import csv

birthday_list = []
age_list = []

with open("DO_NOT_COMMIT_THIS_DIR/조합원 리스트 - 조합원 리스트.csv", newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        bday_len = len(row[2])
        bday_digit_only = ''

        for char in row[2]:
            if char.isdigit():
                bday_digit_only += char

        if bday_len >= 6:
            birthday_list.append(bday_digit_only[-6:])

    for birthday in birthday_list:
        first_two = int(birthday[:2])

        if first_two < 30 and first_two > 1:
            continue

        age_list.append(121 - int(birthday[:2]))

with open("DO_NOT_COMMIT_THIS_DIR/무기명 나이.csv", 'w', newline='', encoding='utf-8') as csvfile:
    for age in age_list:
        csvfile.write(str(age) + '\n')
