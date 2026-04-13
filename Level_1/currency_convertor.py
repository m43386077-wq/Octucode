import os
from time import sleep

DOLLAR = r""" ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||

"""

EXCHANEG_RATES = {
    "": DOLLAR,
    "USD": 1.0,
    "EUR": 0.87,
    "EGP": 52.70,
    "EMB": 6.91
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_rates():
    clear_screen()
    print("Welcome to 'Currency Converter'!\n")
    for currency in EXCHANEG_RATES:
        print(f"{currency}: {EXCHANEG_RATES[currency]}")

def currency_converter():
    display_rates()
    from_currency = input("\nChoose a currency to convert from: ").upper()

    while True:
        amount = float(input("Enter the amount: "))
        confirmation = input(f"You entered {amount} from. Confirm? (Y/N): ").upper()
        if confirmation == "Y":
            break

    display_rates()
    to_currency = input("\nChoose a currency to convert to: ").upper()
    print("\nAnalyzing your request .....Please wait.")
    sleep(2)
    print(f"Getting a discount price for {from_currency} .....Please wait.")
    sleep(3)

    if (from_currency not in EXCHANEG_RATES) or (to_currency not in EXCHANEG_RATES):
        print("Invalid currency. Conversion canceled.")
        sleep(2)
        currency_converter()

    new_rate = EXCHANEG_RATES[to_currency] / EXCHANEG_RATES[from_currency]
    converted_amount = amount * new_rate

    clear_screen()
    print(f"Preparing the deal from {from_currency} to {to_currency} .....Please wait.\n")
    sleep(2)
    print(f"Exchange rate: 1 {from_currency} = {new_rate} {to_currency}\n \n")
    sleep(2)
    print(f"{amount} {from_currency} is equal to {round(converted_amount, 2)} {to_currency}.\n")
    sleep(1)

    if input("\nDo you accept this transaction? (Y/N): ").upper() == "Y":
        print("Transaction Successful!")
    else:
        print("Transaction Canceled.")

    if input("\nDo you want to perform another conversion? (Y/N): ").upper() == "Y":
        currency_converter()

    else:
        print("\nThanks for using currency converter!")

currency_converter()
