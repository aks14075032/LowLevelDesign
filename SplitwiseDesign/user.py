from SplitwiseDesign.expense import *


class User:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    @staticmethod
    def add_expense(expense):
        expense.split_expense()
        for user in expense.get_involved_users():
            user.expenses.append(expense)

    def get_user(self):
        return self.name

    def get_expenses(self):
        return self.expenses

    def calculate_balance(self):
        balance = 0
        for expense in self.expenses:
            if expense.expense_type == ExpenseType.EQUAL:
                num_participants = len(expense.splits_info)
                individual_pay = expense.total_amount / num_participants
                if self == expense.paid_by:
                    balance -= (expense.total_amount - individual_pay)
                else:
                    balance += individual_pay
            elif expense.expense_type == ExpenseType.EXACT:
                user_share = expense.splits_info.get(self, 0)
                if self == expense.paid_by:
                    balance -= (expense.total_amount - user_share)
                else:
                    balance += user_share
            elif expense.expense_type == ExpenseType.PERCENT:
                user_share_percent = expense.splits_info.get(self, 0)
                user_share = expense.total_amount * (user_share_percent / 100)

                if self == expense.paid_by:
                    balance -= (expense.total_amount - user_share)
                else:
                    balance += user_share
            else:
                raise ValueError("Invalid expense type")
        return balance

    def show_passbook(self):
        for expense in self.expenses:
            if self == expense.paid_by:
                for user in expense.get_involved_users():
                    if user == self: continue
                    print(f'{user.name} owes {self.name} {expense.splits_info.get(user, 0)} in {expense.expense_name}')
            else:
                for user in expense.get_involved_users():
                    if user != expense.paid_by: continue
                    print(f'{self.name} owe {user.name} {expense.splits_info.get(user, 0)} in {expense.expense_name}')

    @staticmethod
    def simplify_debts(users, balances):
        num_users = len(users)

        # Create a directed graph to represent the debts
        graph = {i: {} for i in range(num_users)}

        # Populate the graph with debts
        for i, balance in enumerate(balances):
            if balance < 0:  # If user owes money (lender)
                for j, debtor_balance in enumerate(balances):
                    if debtor_balance > 0 and i != j:  # If user is owed money (debtor) and not the same user
                        amount = min(-balance, debtor_balance)
                        if amount > 0:
                            graph[i][j] = amount

        # Perform DFS to simplify debts
        def dfs(node, visited, path):
            visited.add(node)
            for next_node, amount in graph[node].items():
                if next_node not in visited:
                    result = dfs(next_node, visited, path + [(next_node, amount)])
                    if result:
                        return result

            return path

        simplified_debts = []

        for lender in range(num_users):
            if balances[lender] < 0:  # If user owes money (lender)
                visited = set()
                while True:
                    debtor, amount = min(graph[lender].items(), key=lambda x: x[1], default=(None, None))
                    if debtor is None:
                        break

                    path = dfs(debtor, visited, [(debtor, amount)])
                    for next_debtor, next_amount in path:
                        if next_amount == graph[lender][next_debtor]:
                            del graph[lender][next_debtor]
                        else:
                            graph[lender][next_debtor] -= next_amount

                    # Add lender's index to each tuple in the path
                    path_with_lender = [(debtor, lender, amount) for debtor, amount in path]
                    simplified_debts.extend(path_with_lender)

        # Simplified debts now contain tuples with three values: debtor, lender, and amount
        return simplified_debts





