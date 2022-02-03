from utils.inputs import float_input, int_input

__title__ = "Calcul de Surface"

def integrate(x1: float, x2: float, dx: float) -> float:
	"""
	Calcule l'intégrale de f(x) entre x1 et x2.
	:param x1: Valeur de x1.
	:type x1: float
	:param x2: Valeur de x2.
	:type x2: float
	:param dx: Pas de calcul.
	:type dx: float
	:return: L'intégrale de f(x) entre x1 et x2.
	:rtype: float
	"""
	i: float = x1
	surface: float = 0
	while i <= x2:
		surface += function(i) * dx
		i += dx
	return surface

def function(x: float) -> float:
	"""
	Fonction à intégrer.
	:param x: Valeur de x.
	:type x: float
	:return: f(x).
	:rtype: float
	"""
	return x * x

def ex5() -> None:
	"""
	Faire un script qui calcule la surface sous la courbe de la fonction y = x * x
	avec des rectangles avec x appartient à [a,b] et un pas p*.
	:return: None
	:rtype: None
	"""
	a: float = int_input("Entrez a : ")
	b: float = int_input("Entrez b : ")
	p: float = float_input("Entrez p : ")

	print(f"Calcul de l'intégrale avec la fonction f(x) = x * x avec {a} <= x et b < {5} et p = {0.4}.\n"
	      f"Résultat: {integrate(a, b, p)}")

if __name__ == '__main__':
	ex5()
