MAX_LINES=3


def deposit():
    while True:
        amount=input("what would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines=input(f"Enter number of lines to bet on(1-{str(MAX_LINES)})?")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter value number of blocks.")
        else:
            print("Please enter a number.")

    return 


def main():
    balance=deposit()   
    number_digits=get_number_of_lines()
    print(balance)


main()