def deposit(amt):
    global balance
    balance+=amt
    print(f'\n{amt} deposited in account')
    show_balance()

def show_balance():
    print(f'Balance : {balance}')

def withdraw(amt):
    global balance
    if balance<amt:
        print('Insuffecient Funds')
    else:
        balance-=amt
        print(f'\n{amt} withdrew from account')
        show_balance()
    
balance = 0
print('1. Deposit \t 2. Withdraw \t 3.Check Balance \t 4. Exit ')
ch = int(input('Enter Action Number : '))

while ch != 4:
    match ch:
        case 1: 
            depo = int(input('Enter amount to be diposited : ')) 
            deposit(depo)
        case 2: 
            amt = int(input('Enter amount to withdraw : ')) 
            withdraw(amt)
        case 3: 
            show_balance()
        case 4: 
            break
    print('1. Deposit \t 2. Withdraw \t 3.Check Balance \t 4. Exit')
    ch = int(input('Enter Action Number : '))
