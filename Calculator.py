def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

number1 = float(input("Enter the first number: "))
operation = input("choose an operation: \n"
                  "+\n"
                  "-\n"
                  "*\n"
                  "/")
number2 = float(input("Enter the second number: "))
acc = operations[operation](number1,number2)
print(acc)
yes_or_no = input(f"type yes if you want to continue on {acc} type no to start new calc")

while(yes_or_no == "yes"):
    operation = input("choose an operation: \n"
                      "+\n"
                      "-\n"
                      "*\n"
                      "/\n")
    number = float(input("enter number"))
    acc = operations[operation](acc,number)
    print(acc)
    yes_or_no = input(f"type yes if you want to continue on {acc} type no to start new calc")

print(f"final result is {acc}")