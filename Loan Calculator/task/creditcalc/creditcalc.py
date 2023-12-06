import math
import argparse


def calculate_principal(mo_payment, i, num_payments):
    principal = math.floor(mo_payment / ((i * pow(1 + i, num_payments)) / (pow(1 + i, num_payments) - 1)))
    print(f"Your loan principal = {principal}!")
    calculate_overpayment(mo_payment * num_payments, principal)


def calculate_num_payments(principal, mo_payment, i):
    num_payments = math.ceil(math.log(mo_payment / (mo_payment - i * principal), 1 + i))
    years = num_payments // 12
    if num_payments == 1:
        print("It will take 1 month to repay the loan")
    elif num_payments == 12:
        print("It will take 1 year to repay the loan")
    elif num_payments % 12 == 0:
        print(f"It will take {years} years to repay the loan")
    else:
        if num_payments - years * 12 == 1:
            print(f"It will take {years} years and 1 month to repay the loan")
        else:
            print(f"It will take {years} years and {num_payments - years * 12} months to repay the loan")
    calculate_overpayment(mo_payment * num_payments, principal)


def calculate_monthly_payment(t, principal, i, num_payments):
    if t.lower() == "annuity":
        mo_payment = math.ceil(principal * ((i * pow(1 + i, num_payments)) / (pow(1 + i, num_payments) - 1)))
        print(f"Your annuity payment = {mo_payment}!")
        calculate_overpayment(mo_payment * num_payments, principal)
    elif t.lower() == "diff":
        s = 0
        for m in range(1, num_payments + 1):
            mo_payment = math.ceil(principal / num_payments + i * (principal - principal * (m - 1) / num_payments))
            print(f"Month {m}: payment is {mo_payment}")
            s += mo_payment
        print()
        calculate_overpayment(s, principal)
    else:
        print("Incorrect parameters")


def calculate_overpayment(paid, principal):
    overpayment = math.ceil(paid - principal)
    print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
num_parameters = sum(1 for value in vars(args).values() if value is not None)

if (
        not args.type
        or not args.interest or float(args.interest) < 0
        or (args.type == "diff" and args.payment)
        or (args.payment is not None and float(args.payment) < 0)
        or (args.principal is not None and float(args.principal) < 0)
        or (args.periods is not None and int(args.periods) < 0)
        or num_parameters < 4
):
    print("Incorrect parameters")
else:
    interest_rate = float(args.interest) / (12 * 100)
    if not args.principal:
        calculate_principal(float(args.payment), interest_rate, int(args.periods))
    if not args.payment:
        calculate_monthly_payment(args.type, float(args.principal), interest_rate, int(args.periods))
    if not args.periods:
        calculate_num_payments(float(args.principal), float(args.payment), interest_rate)