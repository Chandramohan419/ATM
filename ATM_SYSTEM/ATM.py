import time
from datetime import datetime

##---------------
#bank database (simulated)
##---------------
accounts = {
    "1001": {
        "pin": "1234",
        "balance": 5000,
        "history" : [],
        "locked": False,
        "failed_attempts": 0,
        "daily_limit": 3000
    },
     "1002": {
        "pin": "4321",
        "balance": 10000,
        "history" : [],
        "locked": False,
        "failed_attempts": 0,
        "daily_limit": 3000
    },
    "1003": {
        "pin": "4321",
        "balance": 15000,
        "history": [],
        "locked": True,
        "failed_attempts": 0,
        "daily_limit": 3000
    },
}

##-----------------
#helper functions
##-----------------
def log_transaction(acc, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc]["history"].append(f"{timestamp}| {message}")

def authentication():
    while True:
        acc = input("\n Account number (or exit): ")
        if acc == "exit":
            return None
        if acc not in accounts:
            print("Account not found")
            continue
        if accounts[acc]["locked"]:
            print("Account locked")
            continue
        pin = input("Enter PIN : ")
        if pin == accounts[acc]["pin"]:
            accounts[acc]["failed_attempts"] = 0
            return acc
        else:
            accounts[acc]["failed_attempts"] += 1
            print("PIN not valid, Try again:")

            if accounts[acc]["failed_attempts"] >= 3:
                accounts[acc]["locked"] = True
                print("Account locked due to multiple failed attempts")

def atm_menu(acc):
      while True:
        print("""
1. Balance
2. Deposit
3. Withdraw
4. Mini statement
5. Fund transfer
6. Logout
        """)
        choice = input("Choose: ")
        if choice == "1":
            print("Balance:",accounts[acc]["balance"])

        elif choice =="2":
            amt = input("Enter Amount To Deposit: ")
            if not amt.isdigit():
                print("Invalid Amount, Try again")
                continue
            amt = int(amt)
            accounts[acc]["balance"] += amt
            print(f"Account balance: {accounts[acc]['balance']}")
            log_transaction(acc,f"deposit {amt}")
            print("Deposit successful")
            continue

        elif choice =="3":
            amt = input("Enter Amount To Withdraw: ")
            if not amt.isdigit():
                print("Invalid Amount, Try again")
                continue
            amt = int(amt)
            if amt > accounts[acc]["daily_limit"]:
                print("Daily withdraw limit exceeded")
            elif amt > accounts[acc]["balance"]:
                print("Insufficient Funds")
            else :
              accounts[acc]["balance"] -= amt
              accounts[acc]["daily_limit"] -= amt
              print(f"Account balance: {accounts[acc]['balance']}")
              log_transaction(acc,f"withdraw {amt}")
              print("Collect Cash")
        elif choice == "4":
            print("\nLast Transactions:")
            history = accounts[acc]["history"][-5:] #last 5
            if not history:
                print("No Transactions History")
            for h in history:
                print("-", h)
        elif choice == "5":
            target = input("Transfer to account")
            if target not in accounts:
                print("Transfer account not found")
                continue
            amt = input("Enter Amount Transfer: ")
            if not amt.isdigit():
                print("Invalid Amount, Try again")
                continue
            amt = int(amt)
            if amt > accounts[acc]["balance"]:
                print("Insufficient funds")
                continue
            accounts[acc]["balance"] -= amt
            accounts[target]["balance"] -= amt
            log_transaction(acc, f"Transferred {amt} to {target}")
            log_transaction(target, f"Received {amt} from {acc}")

            print("Transfer successful")

        elif choice == "6":
            print("Logging out...")
            time.sleep(1)
            break

        else:
            print("Invalid option")
# -------------------------
# Main ATM Loop
# -------------------------
def atm():
    print("🏧 Welcome to Secure ATM System")

    while True:  # ATM running loop
        acc = authentication()
        if acc is None:
            print("Thank you for using ATM")
            break

        atm_menu(acc)

atm()








