budget = int(input())
is_all_bought = True
command = input()

while command != "End":
	price = int(command)
	if budget >= price:
		budget -= price
	else:
		print("You went in overdraft!")
		is_all_bought = False
		break
	command = input()

if is_all_bought:
	print("You bought everything needed.")
