hours = 0
pay_rate = 0
grosspay = 0
def read():
    global hours
    global pay_rate
    hours = int(input("Enter you hours: "))
    pay_rate = int(input("Enter you pay_rate: "))


def cal(pay_rate,hours):
    return pay_rate * hours


def print_1():
    global hours
    global pay_rate
        
    print(cal(pay_rate,hours)) 

def main():
    do_you_want = 'y'
    while do_you_want.lower() == 'y':
        read()
        print_1()
        do_you_want = input('do you want to cal Again: ')

main()
