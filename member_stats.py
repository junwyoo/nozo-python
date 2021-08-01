import csv

with open("DO_NOT_COMMIT_THIS_DIR/21년3월.csv", newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    cto_count = 0
    vs_count = 0
    mc_count = 0
    bs_count = 0
    he_count = 0
    sg_count = 0
    ha_count = 0

    for row in csvreader:
        if row[8] != "사무":
            continue

        if row[2] == "CTO부문":
            cto_count += 1

        if row[2] == "VS사업본부":
            vs_count += 1

        if row[2] == "MC사업본부":
            mc_count += 1

        if row[2] == "BS사업본부":
            bs_count += 1

        if row[2] == "HE사업본부":
            he_count += 1

        if row[2] == "생산기술원":
            sg_count += 1

        if row[2] == "H&A사업본부":
            ha_count += 1

    print("cto: ", cto_count)
    print("vs: ", vs_count)
    print("mc: ", mc_count)
    print("bs: ", bs_count)
    print("he: ", he_count)
    print("sg: ", sg_count)
    print("ha: ", ha_count)
