import sys, csv
from day_report import dayReport
from atm_sales import atmReport
from monthly_sales import monthlyReport


# Checks to see if done is typed, then exits the program
def check_input(el):
    if el.lower() == 'done':
        sys.exit(0)


while True:
    data = []
    print('To quit the program at anytime, Enter "DONE":')

    questions = ["DATE", "ATM Remaining Amount", "Number of Withdrawal", "ATM Amount Dispense",
                 "ATM FEE'S", "EBT", "Reg Volume", "Plus Volume", "Pre Volume",
                 "Reg $ Amount", "Plus $ Amount", "Premium $ Amount",
                 "Fuel Discounts", "Total Non Fuel Sales", "Network Revenue",
                 "Tax Collected", "Taxable Sales", "Lottery Sales", "Non-Tax"]

    for q in questions:
        if not q == "Non-Tax":
            el = input("Enter {}: \n".format(q))
            check_input(el)
            data.append(el)

    print()

    try:
        date = data[0]
        nReg = float(data[6]) + (0.60 * float(data[7]))
        vPower = float(data[8]) + (0.40 * float(data[7]))
        nonTax = round(float(data[-5]) - float(data[-6]) - float(data[-2]) - float(data[-1]),2)
        taxable = data[-2]
        lottery = data[-1]
    except ValueError:
        pass

    try:
        data.append(nonTax)
        dayReport(date, nReg, vPower, nonTax, taxable, lottery)
        print("Final Data Output:")
        print("---------------------------")
        print("DATE : {}".format(date))
        print("Regular: {:.2f}".format(nReg))
        print("V.Power: {:.2f}".format(vPower))
        print("Non Tax: {:.2f}".format(nonTax))
        print("Taxable: {}".format(taxable))
        print("Lottery: {}".format(lottery))
        print("---------------------------")
    except NameError:
        pass

    try:
        d = {questions[i]: data[i] for i in range(len(questions))}
    except IndexError:
        pass

    try:
        with open('csvFiles/monthly_data.csv', 'r') as f:
            pass
    except FileNotFoundError:
        with open('csvFiles/monthly_data.csv', 'w') as f:
            r1 = csv.DictWriter(f, fieldnames=questions)
            r1.writeheader()

    try:
        with open('csvFiles/monthly_data.csv', 'a', newline='') as f:
            r2 = csv.DictWriter(f, fieldnames=questions)
            r2.writerow(d)
    except NameError:
        pass

    atmReport()
    monthlyReport()

    print("---------------------------")
    print("Data Successfully Written to File")
    print("---------------------------")
    print()

    v = input('Enter "DONE" to Quit! \n')
    check_input(v)
