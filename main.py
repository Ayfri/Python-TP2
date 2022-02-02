import sys
from typing import Callable

from inputs import int_input

def get_exercice(number: int) -> tuple[str, str, Callable[[], None]]:
	file = __import__(f"src.ex{number}")
	module = getattr(file, f"ex{number}")
	function = getattr(module, f"ex{number}")
	return getattr(module, "__title__"), str(function.__doc__), function

def get_instructions_from_docstring(function: tuple[str, str, Callable[[], None]]) -> str:
	return function[1].split(':return:')[0].strip().replace('\t', '')

def menu(exercices: list[tuple[str, str, Callable[[], None]]]) -> str:
	result = '\n'.join([f"Exercice {i + 1} - {exercices[i][0]}" for i in range(len(exercices))])
	return result

def print_menu() -> None:
	exercices = [get_exercice(i) for i in range(1, 9)]
	terminal_menu = menu(exercices)
	print(terminal_menu)

def main() -> None:
	while True:
		print_menu()
		try:
			input1: int = int_input("Veuillez choisir un exercice :", 1, lambda i: 8)
			exercice = get_exercice(input1)
			print(f"Consigne: {get_instructions_from_docstring(exercice)}\n")
			exercice[2]()
			input("Appuyez sur ENTRÉE pour continuer...")
		except:
			print("\nAu revoir :)")
			sys.exit(1)

if __name__ == '__main__':
	main()
