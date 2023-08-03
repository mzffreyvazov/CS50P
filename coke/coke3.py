first_due = 50
import sys
def main():
    while True:
        if first_due > 0:
            amount_due()
            insert_coin()
        elif first_due == 0:
            sys.exit("Change Owed: 0")
        elif first_due < 0:
            sys.exit(f"Change Owed: {abs(first_due)}")

def amount_due():
    print("Amount Due:", first_due)

def insert_coin():
    global first_due
    while True:
        global x
        x = int(input("Insert Coin: "))
        if x in [25, 10, 5]:
            first_due -= x
            return abs(first_due)
        else:
            print("Amount Due:", abs(first_due))
            
main()