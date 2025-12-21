# ATM System 
#  Methods 

def deposit(amt):
    global balance
    if amt >= 0:
        balance+=amt
        print(f'{amt} deposited in account')
        bank_log.append(f'{amt} credited')
    else : 
        print("Negative amount cannot be deposited ")

def show_balance():
    print(f'Balance : {balance}')
    bank_log.append('Balance Checked')


def withdraw(amt):
    global balance
    if balance<amt:
        print('<Insuffecient Funds !!>')
        bank_log.append('debit failed !')

    else:
        balance-=amt
        print(f'{amt} withdrawn from account')
        bank_log.append(f'{amt} debited')

def show_logs():
    for i in range(5):
        print('\n',bank_log[i])

def user_auth():
    user_name = input('Enter Username : ')
    pin = input('Enter PIN : ')

    if not (user_name.isalnum() and pin.isnumeric()):
        print('Invalid input format')
        return False

    pin = int(pin)

    if user_name in users:
        if pin == users[user_name]['PIN']:
            print(f"Welcome {users[user_name]['name']}!")
            return True,user_name
        else:
            print('Invalid PIN')
            return False,None
    else:
        print('User not found')
        return False,None


users = {
    'U1001': {'name': 'John', 'Balance': 1000, 'PIN': 100},
    'U1002': {'name': 'Sova', 'Balance': 1300, 'PIN': 310},
    'U1003': {'name': 'Eden', 'Balance': 2400, 'PIN': 780}
}

#Main 
if __name__=='__main__':
    is_user_valid,u_name = user_auth()
    if is_user_valid:
        print(u_name)
        balance = 0
        bank_log=[]
        print('1. Deposit \t 2. Withdraw \t 3.Check Balance \t 4. Logs \t 5. Exit ')
        ch = int(input('Enter Action Number : '))

        while ch != 5:
            match ch:
                case 1: 
                    amt = int(input('Enter amount to be diposited : ')) 
                    deposit(amt)
                case 2: 
                    amt = int(input('Enter amount to withdraw : ')) 
                    withdraw(amt)
                case 3: 
                    show_balance()
                case 4:
                    show_logs()
                case 5: 
                    print('Thank You!! Vist Again !')
                    break
            print('\n1. Deposit \t 2. Withdraw \t 3.Check Balance \t 4. Logs \t 5. Exit')
            ch = int(input('Enter Action Number : '))
