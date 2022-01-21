from utils.inputs import float_input

def ex3() -> None:
	"""
	Le but est de résoudre une équation du second degré.
	Résoudre l’équation du second degré : Ax² + Bx + C = 0
	:return:
	:rtype:
	"""
	a = float_input("Entrez A : ")
	b = float_input("Entrez B : ")
	c = float_input("Entrez C : ")

	delta = b ** 2 - 4 * a * c
	if delta < 0:
		print("L'équation n'admet pas de solution.")
	elif delta == 0:
		x: float = -b / (2 * a)
		print(f"L'équation admet une unique solution : {x}")
	else:
		x1: float = (-b - delta ** 0.5) / (2 * a)
		x2: float = (-b + delta ** 0.5) / (2 * a)
		print(f"L'équation admet deux solutions : {x1} et {x2}")


if __name__ == '__main__':
	ex3()
