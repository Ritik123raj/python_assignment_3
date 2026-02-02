# factorial of number using recurssion

def fact(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact(num-1)
        return factorial

a = int(input("Enter the number for factorial: "))

print(f"The factorial of number {a} is {fact(a)}")