from SplitwiseDesign.user import User
from SplitwiseDesign.ExpenseFactory.expenseFactory import *


# Create some users
user1 = User("AK")
user2 = User("VK")
user3 = User("PK")

equal_splits = [user1, user2, user3]

equal_expense = ExpenseFactory.create_expense(ExpenseType.EQUAL, "Groceries", 1800, user1, equal_splits)

user1.add_expense(equal_expense)

# print(user1.calculate_balance()) -800
# print(user2.calculate_balance())  400
# print(user3.calculate_balance())  400

exact_splits = {user1: 400, user2: 500, user3: 300}
exact_expense = ExpenseFactory.create_expense(ExpenseType.EXACT, "Party", 1200, user2, exact_splits)

user2.add_expense(exact_expense)

# print(user1.calculate_balance()) # -400
# print(user2.calculate_balance()) # -300
# print(user3.calculate_balance()) # 700

# Create a PERCENT expense using the factory
percent_splits = {user1: 40, user2: 30, user3: 30}
percent_expense = ExpenseFactory.create_expense(ExpenseType.PERCENT, "Trip", 2000, user1, percent_splits)

# Add the expense to the user's list of expenses
user1.add_expense(percent_expense)


equal_expense_1 = ExpenseFactory.create_expense(ExpenseType.EQUAL, "Movie", 1500, user2, equal_splits)

user1.add_expense(equal_expense_1)

print(user1.calculate_balance())  # -400 + 800 - 1200
print(user2.calculate_balance())  # -300 + 600
print(user3.calculate_balance())  # 700+600

user1.show_passbook()

simplified_debts = user1.simplify_debts(equal_splits, [user1.calculate_balance(), user2.calculate_balance(), user3.calculate_balance()])

# Determine minimum transactions for each user
for debtor, lender, amount in simplified_debts:
    debtor_user = equal_splits[debtor]
    lender_user = equal_splits[lender]
    print(f"{debtor_user.name} owes {lender_user.name} ${amount:.2f}")


