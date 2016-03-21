def dayReport(date, nReg, vPower, nonTax, taxable, lottery):
    import csv
    newData = [date, nReg, vPower, nonTax, taxable, lottery]
    dayreport = ["DATE", "Regular", "V.Power", "Non-Tax", "Tax", "Lottery"]

    try:
        with open('csvFiles/day_report.csv', 'r') as f:
            pass
    except FileNotFoundError:
        with open('csvFiles/day_report.csv', 'w') as f:
            r1 = csv.DictWriter(f, fieldnames=dayreport)
            r1.writeheader()
    try:
        dayreportDict = {dayreport[i]: newData[i] for i in range(len(dayreport))}

        with open('csvFiles/day_report.csv', 'a', newline='') as f1:
            r3 = csv.DictWriter(f1, fieldnames=dayreport)
            r3.writerow(dayreportDict)
    except FileNotFoundError as e:
        print(e)

    print("Day Report Created Successfully")
