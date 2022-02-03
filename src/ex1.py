from typing import List

from utils.inputs import int_input
from utils.prints import print_result

__title__ = "Le plus grand"

def ex1() -> None:
	"""
	Écrire un algorithme qui demande successivement 10 nombres à
	l’utilisateur, et qui lui dise ensuite quel était le plus grand parmi
	ces 10 nombres.
	Modifiez ensuite l’algorithme pour que le programme affiche de
	surcroît en quelle position avait été saisie ce nombre.

	:return: None
	:rtype: None
	"""
	array: List[int] = [int_input(f"Entrez le nombre n°{i} : ") for i in range(1, 11)]
	print_result(f"Le plus grand de ces nombres est : {max(array)}\n"
	      f"C'était le numéro {array.index(max(array))}")

if __name__ == "__main__":
	ex1()
