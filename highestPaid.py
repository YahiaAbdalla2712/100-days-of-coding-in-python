paid_dic={}
print("welcome to highest paid game")
name = input("what is your name?")
paid_money = int(input("how much do u get paid?"))
paid_dic[name] = paid_money
max = paid_dic[name]
printed_name = name
yes_or_no = input("is there another player?")
print("\n"*100)

while(yes_or_no == "yes"):
    name = input("what is your name?")
    paid_money = int(input("how much do u get paid?"))
    paid_dic[name] = paid_money
    yes_or_no = input("is there another player?")
    print("\n" * 100)

for key in paid_dic:
    if paid_dic[key] > max:
        max = paid_dic[key]
        printed_name = key

print(f"the highest paid is {printed_name} which got paid {max}")

