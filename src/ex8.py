from src.ex7 import fibonacci
from utils.inputs import int_input
from utils.prints import print_result

__title__ = "Le nombre d’or & Fibonacci"

def sequence(n: int) -> float:
	"""
	Calcule la valeur de la suite O(n).
	:param n: Nombre d'itérations.
	:type n: int
	:return: Valeur de la suite O(n).
	:rtype: float
	"""
	if n <= 1:
		return n
	for i in range(2, n + 1):
		if i % 5 == 0 or i == n:
			print(f"O[{i}] = {fibonacci(i + 1) / fibonacci(i)}")
	return fibonacci(n + 1) / fibonacci(n)

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
	print_result(f"Le résultat de O[{n}] est {sequence(n)}.\n"
	      f"Le nombre d'or est égal à {phi}.")

if __name__ == '__main__':
	ex8()
