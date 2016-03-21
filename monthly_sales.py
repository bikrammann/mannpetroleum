def monthlyReport():
    import csv

    mDict = {}
    mHeaders = ["DATE", "Reg Volume", "Plus Volume", "Pre Volume", "Reg $ Amount", "Plus $ Amount",
                "Premium $ Amount", "Non-Tax", "Taxable Sales", "Lottery Sales", "Tax Collected",
                " "," "," "," "," ","Network Revenue"," "," "," ","EBT"]

    mValues = []

    try:
        with open('csvFiles/monthly_sales.csv', 'r') as f:
            pass
    except FileNotFoundError:
        with open('csvFiles/monthly_sales.csv', 'w') as f:
            r1 = csv.DictWriter(f, fieldnames=mHeaders)
            r1.writeheader()
    try:
        with open('csvFiles/monthly_data.csv', 'r') as f:
            r2 = csv.DictReader(f)
            for row in r2:
                mValues = [row["DATE"], row["Reg Volume"], row["Plus Volume"],
                           row["Pre Volume"], row["Reg $ Amount"], row["Plus $ Amount"],
                           row["Premium $ Amount"], row["Non-Tax"], row["Taxable Sales"],
                           row["Lottery Sales"], row["Tax Collected"], '','','','','',
                           row["Network Revenue"], '','','',row["EBT"]]

    except FileNotFoundError as e:
        print(e)


    mDict = {mHeaders[i]: mValues[i] for i in range(len(mHeaders))}

    with open('csvFiles/monthly_sales.csv', 'a', newline='') as f1:
        r3 = csv.DictWriter(f1, fieldnames=mHeaders)
        r3.writerow(mDict)
