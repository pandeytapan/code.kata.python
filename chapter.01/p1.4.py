# A program that prints the balance of an account after the first, second, and third year. 
# The account has an initial balance of $1,000 and earns 5 percent interest per year.

account_balance = 10_000
interest_rate = 0.05

#1
account_balance += account_balance * interest_rate
print(f"Acccount balance after year 1 is {account_balance}") 

#2
account_balance += account_balance * interest_rate
print(f"Acccount balance after year 2 is {account_balance}") 

#3
account_balance += account_balance * interest_rate
print(f"Acccount balance after year 3 is {account_balance}") 

# Another way

account_balance = 10_000

for i in range (3):
    account_balance += account_balance * interest_rate
    print(f"Account balance after year {i + 1} is {account_balance}")