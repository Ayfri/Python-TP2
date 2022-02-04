import math
from utils.inputs import float_input, int_input
from utils.prints import print_result

__title__ = "Développement limité"

nMax: int = 50

def f(x: float, n: int) -> float:
	"""
	Calcule la valeur de la fonction f(x, n) pour la fonction cosinus.
	:param x: Valeur de x.
	:type x: float
	:param n: Valeur de n.
	:type n: int
	:return: La valeur de la fonction f(x, n) pour la fonction cosinus.
	:rtype: int
	"""
	return (x ** n) / math.factorial(n)

def exp(x: float) -> float:
	"""
	Calcule l'exponentielle de x.
	:param x: Valeur de x.
	:type x: float
	:return: L'exponentielle de x.
	:rtype: int
	"""
	n = 0
	result = f(x, n)
	while n < nMax:
		if n != 0:
			result += f(x, n)
		n += 1
	return result

def f2(x: float, n: int) -> float:
	"""
	Calcule la valeur de la fonction f(x, n) pour la fonction sinus.
	:param x: Valeur de x.
	:type x: float
	:param n: Valeur de n.
	:type n: int
	:return: La valeur de la fonction f(x, n) pour la fonction sinus.
	:rtype: int
	"""
	first_product: float = (-1) ** (n - 1)
	nominator: float = (x ** (2 * n - 1))
	denominator: float = math.factorial((2 * n) - 1)
	return first_product * (nominator / denominator)

def sinus(x: float) -> float:
	"""
	Calcule le sinus de x.
	:param x: Valeur de x.
	:type x: float
	:return: Le sinus de x.
	:rtype: int
	"""
	n: int = 1
	result: float = x
	while n < nMax:
		n += 1
		result += f2(x, n)
	return result

def ex6() -> None:
	"""
	Algorithme de calcul de l'exponentielle et du sinus comparé avec la librairie math.
	:return: None
	:rtype: None
	"""
	while True:
		try:
			i: float = float_input("Entrez un nombre entier : ")
			print_result(f"Via l'algorithme : e^{i} = {exp(i)}")
			print(f"math.exp(i) = {math.exp(i)}")
			print_result(f"Via l'algorithme : sin({i}) = {sinus(i)}")
			print(f"math.sin(i) = {math.sin(i)}")
			break
		except OverflowError:
			print("Valeur trop grande.")

if __name__ == "__main__":
	ex6()
