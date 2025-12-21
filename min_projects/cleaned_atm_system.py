# ATM System

def user_auth():
    user_name = input('Enter Username : ')
    pin = input('Enter PIN : ')

    if not (user_name.isalnum() and pin.isnumeric()):
        print('Invalid input format')
        return False, None

    pin = int(pin)

    if user_name in users:
        if pin == users[user_name]['PIN']:
            print(f"Welcome {users[user_name]['name']}!")
            return True, user_name
        else:
            print('Invalid PIN')
            return False, None
    else:
        print('User not found')
        return False, None


def deposit(balance, amt):
    if amt > 0:
        print(f"{amt} deposited successfully")
        return balance + amt
    else:
        print("Invalid deposit amount")
        return balance


def withdraw(balance, amt):
    if amt <= 0:
        print("Invalid withdrawal amount")
        return balance

    if amt > balance:
        print("Insufficient Funds")
        return balance
    else:
        print(f"{amt} withdrawn successfully")
        return balance-amt

def show_logs(u_name):
    print("\n--- Last Transactions ---")
    logs = users[u_name]['log'][-5:]
    if not logs:
        print("No transactions yet")
    else:
        for log in logs:
            print(log)
def transaction_summary(logs):
    credited = 0
    debited = 0 
    failed = 0

    for log in logs:
        if log.startswith("[+]"):
            credited += int(log.split()[1])
        elif log.startswith("[-]") and 'debited' in log:
            debited += int(log.split()[1])
        elif "failed" in log:
            failed += 1

    print("\n--- Transaction Summary ---")
    print(f"Total Credited : {credited}")
    print(f"Total Debited  : {debited}")
    print(f"Failed Txns   : {failed}")
    print(f"Net Change    : {credited - debited}")


def load_menu():
        print('\n1. Deposit \t 2. Withdraw \t 3. Check Balance \t 4. Logs \t 5.Transaction Summary \t6. Exit')
        ch = int(input('Enter Action Number : '))
        return ch

users = {
    'U1001': {'name': 'John', 'Balance': 1000, 'PIN': 100, 'log': []},
    'U1002': {'name': 'Sova', 'Balance': 1300, 'PIN': 310, 'log': []},
    'U1003': {'name': 'Eden', 'Balance': 2400, 'PIN': 780, 'log': []}
}




if __name__ == '__main__':
    is_valid, u_name = user_auth()

    if is_valid:
        ch = load_menu()

        while ch != 6:
            match ch:
                case 1:
                    amt = int(input('Enter amount to deposit : '))
                    old_balance=users[u_name]['Balance']
                    
                    new_balance=deposit(old_balance,amt)

                    if new_balance != old_balance:
                        users[u_name]['log'].append(f"[+] {amt} credited")
                    if amt <= 0:
                        users[u_name]['log'].append(f"[-] Credit Failed Invalid amount")
                    users[u_name]['Balance'] = new_balance
                        


                case 2:
                    amt = int(input('Enter amount to withdraw : '))
                    old_balance = users[u_name]['Balance']
                    new_balance = withdraw(old_balance,amt)
                    
                    if old_balance == new_balance:
                        reason = "Invalid amount" if amt<= 0 else "Insufficient funds"
                        users[u_name]['log'].append(f"[-] Debit Failed {reason}")
                        
                    else:
                        users[u_name]['log'].append(f"[-] {amt} debited")
                    users[u_name]['Balance'] = new_balance

                case 3:
                    balance = users[u_name]['Balance']
                    print(f"Current Balance : {balance}")
                    users[u_name]['log'].append("[*] Balance checked")

                case 4:
                    print("\n--- Last Transactions ---")
                    logs = users[u_name]['log'][-5:]
                    if not logs:
                        print("No transactions yet")
                    else:
                        for log in logs:
                            print(log)

                case 5:
                    transaction_summary(users[u_name]['log'])
                case _:
                    print("Invalid option")

            ch = load_menu()
            

        print("Thank you! Visit again.")
