"""
Write a program that reads an integer number representing a budget.
On the following lines,
it reads integer numbers representing the
prices of each product you should buy until it receives
the command "End".
During the iterations, if there is not enough budget left to buy
the next product, it prints
"You went in overdraft!" and end the program.
Otherwise, if you accomplished to buy all products
before receiving "End", it prints "You bought everything needed."
"""

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
