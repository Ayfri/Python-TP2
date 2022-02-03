from src.ex7 import fibonacci
from utils.inputs import int_input

__title__ = "Le nombre d’or & Fibonacci"

def sequence(n: int) -> float:
	"""
	Calcule la valeur de la suite O(n).
	:param n: Nombre d'itérations.
	:type n: int
	:return: Valeur de la suite O(n).
	:rtype: float
	"""
	return n if n <= 1 else fibonacci(n + 1) / fibonacci(n)

def ex8() -> None:
	"""
	Soit la suite.
	O(1)=1
	O(n) = F(n+1)/F(n) avec F(n) qui représentante la valeur de Fibonacci à l’ordre n
	Programmer la suite O et comparer le résultat au nombre d’ordre n.
	:return: None
	:rtype: None
	"""
	n: int = int_input("Entrez N : ")
	phi: float = (1 + 5 ** 0.5) / 2
	print(f"Le résultat de O[{n}] est {sequence(n)}.\n"
	      f"Le nombre d'or est égal à {phi}.")

if __name__ == '__main__':
	ex8()
