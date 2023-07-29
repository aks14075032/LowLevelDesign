from enum import Enum, auto
from abc import ABC, abstractmethod
import math


class ExpenseType(Enum):
    EQUAL = auto()
    EXACT = auto()
    PERCENT = auto()


class Expense(ABC):
    def __init__(self, expense_name, total_amount, paid_by, splits, notes=None, images=None):
        self.expense_name = expense_name
        self.expense_type = None
        self.total_amount = total_amount
        self.paid_by = paid_by
        self.splits_info = splits
        self.notes = notes
        self.images = images

    def get_expense_type(self):
        return self.expense_type

    def get_paid_by_user(self):
        return self.paid_by

    def get_splits(self):
        return self.splits_info

    def verify_splits(self):
        # Verify the splits_info dictionary based on the type of expense
        if self.expense_type == ExpenseType.EQUAL:
            # Check if the number of participants matches the number of users
            total_share = sum(self.splits_info.values())
            if not math.isclose(total_share, self.total_amount, rel_tol=1e-9):
                raise ValueError("Invalid splits: Total share does not match the total amount")

        elif self.expense_type == ExpenseType.EXACT:
            # Check if the total amount specified in splits_info matches the total amount of the expense
            total_split_amount = sum(self.splits_info.values())
            if total_split_amount != self.total_amount:
                raise ValueError("ExactExpense total split amount does not match the total expense amount.")

        elif self.expense_type == ExpenseType.PERCENT:
            # Check if the sum of percentage shares is 100
            total_percent = sum(self.splits_info.values())
            if total_percent != 100:
                raise ValueError("PercentExpense total percentage shares must add up to 100.")

        else:
            raise ValueError("Invalid expense type.")

    def add_split(self, user, amount):
        self.splits_info[user] = amount

    @abstractmethod
    def split_expense(self):
        pass

    def get_involved_users(self):
        return set(self.splits_info.keys())


class EqualExpense(Expense):
    def __init__(self, expense_name, total_amount, paid_by, participants, notes=None, images=None):
        super().__init__(expense_name, total_amount, paid_by, None, notes, images)
        self.participants = participants
        self.expense_type = ExpenseType.EQUAL

    def split_expense(self):
        share_amount = self.total_amount/len(self.participants)
        self.splits_info = {user: share_amount for user in self.participants}
        self.verify_splits()


class ExactExpense(Expense):
    def __init__(self, expense_name, total_amount, paid_by, splits_info, notes=None, images=None):
        super().__init__(expense_name, total_amount, paid_by, splits_info, notes, images)
        self.expense_type = ExpenseType.EXACT

    def split_expense(self):
        self.verify_splits()


class PercentExpense(Expense):
    def __init__(self, expense_name, total_amount, paid_by, splits_info, notes=None, images=None):
        super().__init__(expense_name, total_amount, paid_by, splits_info, notes, images)
        self.expense_type = ExpenseType.PERCENT

    def split_expense(self):
        total_percent = sum(self.splits_info.values())
        if total_percent != 100:
            raise ValueError("Total percentage shares must be 100.")

        for user, percent_share in self.splits_info.items():
            self.add_split(user, percent_share)

        self.verify_splits()
