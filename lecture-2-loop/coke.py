def vendingMachine():
    amount_due = 50
    print(f'Amount due: {amount_due}')
    while amount_due > 0:
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin in [5, 10, 25]:
            amount_due -= inserted_coin
            print(f'Amount due: {amount_due}')
        else:
            print(f'Amount due: {amount_due}')
            continue

vendingMachine()
#