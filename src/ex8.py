from src.ex7 import fibonacci
from utils.inputs import int_input

def sequence(n: int) -> float:
	if n == 1:
		return 1
	return fibonacci(n + 1) / fibonacci(n)

def ex8() -> None:
	n: int = int_input("Entrez N : ")
	phi: float = (1 + 5 ** 0.5) / 2
	print(f"Le résultat de O[{n}] est {sequence(n)}.\n"
	      f"Le nombre d'or est égal à {phi}.")

if __name__ == '__main__':
	ex8()
