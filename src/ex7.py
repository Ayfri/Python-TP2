from utils.inputs import int_input

__title__ = "Fibonacci"

def fibonacci(n: int) -> int:
	"""
	Calcule le n-ième nombre de la suite de Fibonacci.
	:param n: Nombre à calculer de la suite de Fibonacci.
	:type n: int
	:return: int
	:rtype: int
	"""
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return a

def ex7() -> None:
	"""
	Écrire une fonction calculant le nombre de Fibonacci d’un nombre.
	:return: None
	:rtype: None
	"""
	number: int = int_input("Entrez n : ")
	result: int = fibonacci(number)
	print(f"Fibonacci de {number} est {result} : F[{number}] = {result}")

if __name__ == '__main__':
	ex7()
