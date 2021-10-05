import time

print('Please Insert your card')

time.sleep(4)

password = 12345

pin = int(input("ENTER YOUR ATM PIN"))

balance = 5000

if pin == password:
    while True:
        print("""
		1 == Balance
		2 == withdrawn balance 
		3 == deposit balance 
		4 == exit """)
        try:
            option = int(input("Please enter your choice"))
            if option == 1:
                print(f"Your current balance is {balance}")
            if option == 2:
                withdrawn_amt = int(input("Please enter withdrawn amount "))
                balance = balance - withdrawn_amt
                print(f"Your {withdrawn_amt} is debited from your account")
                print(f"Your current balance is {balance}")
            if option == 3:
                deposit_amt = int(input("Please enter a amount do you want to deposit !"))
                balance = balance + deposit_amt
                print(f"Your Amount is Updated of Rs {deposit_amt}")
                print(f"Your current balance is {balance}")

            elif option == 4:
                break
        except:
            print("Please enter valid option")

else:
    print("You enter a wrong pin")
