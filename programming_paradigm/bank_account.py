"""Simple BankAccount class for basic OOP practice.

Provides deposit, withdraw and display_balance methods.
"""

class BankAccount:
	"""A very small bank account model.

	Attributes:
		_balance (float): the current account balance (encapsulated).
	"""

	def __init__(self, initial_balance: float = 0.0):
		"""Initialize the account with an optional starting balance.

		Raises ValueError if initial_balance is negative.
		"""
		if initial_balance < 0:
			raise ValueError("Initial balance cannot be negative.")
		self._balance = float(initial_balance)

	def deposit(self, amount: float) -> None:
		"""Deposit a positive amount into the account.

		Raises ValueError for non-positive amounts.
		"""
		if amount <= 0:
			raise ValueError("Deposit amount must be positive.")
		self._balance += float(amount)

	def withdraw(self, amount: float) -> bool:
		"""Attempt to withdraw amount from the account.

		Returns True and deducts the amount when sufficient funds exist.
		Returns False and leaves the balance unchanged otherwise.
		Raises ValueError for non-positive amounts.
		"""
		if amount <= 0:
			raise ValueError("Withdraw amount must be positive.")
		if amount <= self._balance:
			self._balance -= float(amount)
			return True
		return False

	def display_balance(self) -> None:
		"""Print the current balance in a user friendly format."""
		print(f"Current Balance: ${self._balance:.2f}")
