def atmReport():
    import csv
    atmDict = {}
    atmHeaders = ["DATE", "ATM Remaining Amount", "Amount Added", "ATM Amount Dispense", " ",
                  "Number of Withdrawal", "ATM FEE'S"]
    atmValues = []

    try:
        with open('csvFiles/atm.csv', 'r') as f:
            pass
    except FileNotFoundError:
        with open('csvFiles/atm.csv', 'w') as f:
            r1 = csv.DictWriter(f, fieldnames=atmHeaders)
            r1.writeheader()
    try:
        with open('csvFiles/monthly_data.csv', 'r') as f:
            r2 = csv.DictReader(f)
            for row in r2:
                atmValues = [row["DATE"], row["ATM Remaining Amount"], '', row["ATM Amount Dispense"], '',
                             row["Number of Withdrawal"], row["ATM FEE'S"]]
    except FileNotFoundError as e:
        print(e)

    atmDict = {atmHeaders[i]: atmValues[i] for i in range(len(atmHeaders))}

    with open('csvFiles/atm.csv', 'a', newline='') as f1:
        r3 = csv.DictWriter(f1, fieldnames=atmHeaders)
        r3.writerow(atmDict)