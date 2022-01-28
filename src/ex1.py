from utils.inputs import int_input

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
	array = [int_input(f"Entrez le nombre n°{i} : ") for i in range(1, 11)]
	print(f"Le plus grand de ces nombres est : {max(array)}\n"
	      f"C'était le numéro {array.index(max(array))}")

if __name__ == "__main__":
	ex1()
