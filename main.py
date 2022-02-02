import sys
from typing import Callable

from inputs import int_input

def get_exercice(number: int) -> tuple[str, str, Callable[[], None]]:
	"""
	Retourne le tuple contenant le nom, la consigne et la fonction à exécuter.
	:param number: Le numéro de l'exercice.
	:type number: int
	:return: Le tuple contenant le nom, la consigne et la fonction à exécuter.
	:rtype: tuple[str, str, Callable[[], None]]
	"""
	file: object = __import__(f"src.ex{number}")
	module: object = getattr(file, f"ex{number}")
	function: object = getattr(module, f"ex{number}")
	return getattr(module, "__title__"), str(function.__doc__), function

def get_instructions_from_docstring(function: tuple[str, str, Callable[[], None]]) -> str:
	"""
	Retourne la consigne de l'exercice.
	:param function: L'exercice.
	:type function: tuple[str, str, Callable[[], None]]
	:return: La consigne de l'exercice depuis le docstring.
	:rtype: str
	"""
	return function[1].split(':return:')[0].strip().replace('\t', '')

def menu(exercices: list[tuple[str, str, Callable[[], None]]]) -> str:
	"""
	Renvoie le menu de sélection des exercices.
	:param exercices: La liste des exercices.
	:type exercices: list[tuple[str, str, Callable[[], None]]]
	:return: La liste des exercices dans le format "Exercice [nombre] - [consigne]".
	:rtype: str
	"""
	result: str = '\n'.join([f"Exercice {i + 1} - {exercices[i][0]}" for i in range(len(exercices))])
	return result

def print_menu() -> None:
	"""
	Affiche le menu de sélection des exercices.
	:return: None
	:rtype: None
	"""
	exercices: list[tuple[str, str, Callable[[], None]]] = [get_exercice(i) for i in range(1, 9)]
	terminal_menu: str = menu(exercices)
	print(terminal_menu)

def main() -> None:
	"""
	Lance le programme.
	:return: None
	:rtype: None
	"""
	while True:
		print_menu()
		try:
			input1: int = int_input("Veuillez choisir un exercice :", 1, lambda i: 8)
			exercice: tuple[str, str, Callable[[], None]] = get_exercice(input1)
			print(f"Consigne: {get_instructions_from_docstring(exercice)}\n")
			exercice[2]()
			input("Appuyez sur ENTRÉE pour continuer...")
		except:
			print("\nAu revoir :)")
			sys.exit(1)

if __name__ == '__main__':
	main()
