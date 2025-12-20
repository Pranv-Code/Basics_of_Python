# ATM System 
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
        print(f'{amt} withdrew from account')
        bank_log.append(f'{amt} debited')

def show_logs():
    for i in bank_log:
        print('\n',i)
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
