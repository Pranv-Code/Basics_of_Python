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


def deposit(u_name, amt):
    if amt > 0:
        users[u_name]['Balance'] += amt
        users[u_name]['log'].append(f"[+] {amt} credited")
        print(f"{amt} deposited successfully")
    else:
        print("Invalid deposit amount")


def withdraw(u_name, amt):
    if amt <= 0:
        print("Invalid withdrawal amount")
        return

    balance = users[u_name]['Balance']

    if amt > balance:
        print("Insufficient Funds")
        users[u_name]['log'].append("[-] Debit failed (Insufficient funds)")
    else:
        users[u_name]['Balance'] -= amt
        users[u_name]['log'].append(f"[-] {amt} debited")
        print(f"{amt} withdrawn successfully")


def show_balance(u_name):
    balance = users[u_name]['Balance']
    print(f"Current Balance : {balance}")
    users[u_name]['log'].append("[*] Balance checked")


def show_logs(u_name):
    print("\n--- Last Transactions ---")
    logs = users[u_name]['log'][-5:]
    if not logs:
        print("No transactions yet")
    else:
        for log in logs:
            print(log)



users = {
    'U1001': {'name': 'John', 'Balance': 1000, 'PIN': 100, 'log': []},
    'U1002': {'name': 'Sova', 'Balance': 1300, 'PIN': 310, 'log': []},
    'U1003': {'name': 'Eden', 'Balance': 2400, 'PIN': 780, 'log': []}
}




if __name__ == '__main__':
    is_valid, u_name = user_auth()

    if is_valid:
        print('\n1. Deposit \t 2. Withdraw \t 3. Check Balance \t 4. Logs \t 5. Exit')
        ch = int(input('Enter Action Number : '))

        while ch != 5:
            match ch:
                case 1:
                    amt = int(input('Enter amount to deposit : '))
                    deposit(u_name, amt)

                case 2:
                    amt = int(input('Enter amount to withdraw : '))
                    withdraw(u_name, amt)

                case 3:
                    show_balance(u_name)

                case 4:
                    show_logs(u_name)

                case _:
                    print("Invalid option")

            print('\n1. Deposit \t 2. Withdraw \t 3. Check Balance \t 4. Logs \t 5. Exit')
            ch = int(input('Enter Action Number : '))

        print("Thank you! Visit again.")
