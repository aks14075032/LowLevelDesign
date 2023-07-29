from SplitwiseDesign.expense import *


class ExpenseFactory:
    @staticmethod
    def create_expense(expense_type, expense_name, total_amount, paid_by, splits_info, notes=None, images=None):
        if expense_type == ExpenseType.EQUAL:
            return EqualExpense(expense_name, total_amount, paid_by, splits_info, notes, images)
        elif expense_type == ExpenseType.EXACT:
            return ExactExpense(expense_name, total_amount, paid_by, splits_info, notes, images)
        elif expense_type == ExpenseType.PERCENT:
            return PercentExpense(expense_name, total_amount, paid_by, splits_info, notes, images)
        else:
            raise ValueError("Invalid expense type.")

