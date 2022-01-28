import math
import sys

__title__ = "Développement limité"

nMax: int = sys.maxsize

def f(x: int, n: int) -> int:
	return x ** n / math.factorial(n)

def exp(x: int) -> int:
	n = 0
	result = f(x, n)
	while result < nMax:
		result += f(x, n)
		n += 1
	return result

def ex6() -> None:
	"""
	>>> ex6()
	:return: None
	:rtype: None
	"""
	pass

if __name__ == "__main__":
	ex6()
