import math

from utils.inputs import int_input

def ex2() -> None:
	"""
	Écrire un algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté
	et autres impôts volontaires.
	On demande à l’utilisateur le nombre de chevaux partants et le nombre de chevaux joués.

	:return: None
	:rtype: None
	"""
	horses_participating: int = int_input("Combien de chevaux participent : ")
	horses_played: int = int_input("Combien de chevaux sont joués : ")
	x = math.factorial(horses_participating) / math.factorial(horses_participating - horses_played)
	y = math.factorial(horses_participating) / (math.factorial(horses_played) * math.factorial(horses_participating - horses_played))
	print(f"• Dans l’ordre : une chance sur {int(x)} de gagner.\n"
	      f"• Dans le désordre : une chance sur {int(y)} de gagner.")

if __name__ == "__main__":
	ex2()
