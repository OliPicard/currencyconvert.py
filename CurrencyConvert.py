__author__ = 'OliPicard'
import math

#Full Source code can be found at http://github.com/olipicard/currencyconvert.py
#A basic Currency Converter. Note before use you should edit the currency's current exchange rate.
#You can do this by using the open exchange API (https://openexchangerates.org/) alternatively doing a simple google search
#should lead you to the base rate.

#----------------------------------------------------#
#Configuration (Enter your exchange rate data below.)#
#----------------------------------------------------#
def usd_to_gbp(a):
    b = 0.649382 #GBP Current Exchange Rate. (Please update this over time.) in the .json file you should see a "GBP" followed by the current exchange amount.
    c = a * b
    return (a,float (c))
def usd_to_btc(a):
    b = 0.0040918439 #BTC (Bitcoin) Exchange Rate (Update this over time!)
    c = a * b
    return (a,float(c))







#---------------#
#User Interface #
#---------------#
def menu(): #Navigation Menu.
    print("-" * 25)
    print("CurrencyConvert.py")
    print("Note: The exchange rate may be different. Create an account at https://openexchangerates.org to get the latest rates.")
    print("-" * 25)
    print("1. USD to GBP")
    print("2. USD to Bitcoin")
    print("3. Quit CurrencyConvert.Py")


def check_input(user_input): #Checking for inputs.
    try:
        converted_number = float (user_input)
    except ValueError:
        return -1
    return converted_number

#-------------------------------------#
# The Magic Stuff (Programming)       #
#-------------------------------------#

loop = True
while loop:
    menu()
    choice=int(input("Awaiting for your command. Pick which conversion you want next."))
    if choice not in [1,2,3,4,5]:
        print(choice, " is not a vaild input. please try again.")
        menu()
        choice=int(input("Awaiting for your next command."))
    if choice == 1:
        print("Let's convert USD to GBP.")
        usd = check_input(input("$"))
        result = usd_to_gbp(usd)
        print('$ {}  = £ {}'.format(*result))
    if choice == 2:
        print("Let's convert USD into BTC (Bitcoin)")
        usd = check_input(input("$"))
        result = usd_to_btc(usd)
        print('$ {} to Ƀ {}'.format(*result))
    if choice == 3:
        print("Thank you for using the CurrencyConvert.Py script.\nIf you have any questions or bugs to report feel free to visit http://github.com/olipicard/currencyconvert.py")
        loop = False













