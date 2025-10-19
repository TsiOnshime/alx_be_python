"""Robust division helper.

Provides safe_divide which handles non-numeric input and division by zero.
"""

def safe_divide(numerator, denominator):
	"""Attempt to divide numerator by denominator safely.

	Parameters may be strings or numbers. Returns a user-friendly string
	describing the result or the error.
	"""
	try:
		num = float(numerator)
		den = float(denominator)
	except ValueError:
		return "Error: Please enter numeric values only."

	try:
		result = num / den
	except ZeroDivisionError:
		return "Error: Cannot divide by zero."

	return f"The result of the division is {result}"
