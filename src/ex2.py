import math

from utils.inputs import int_input

def ex2() -> None:
	horses_participating: int = int_input("Combien de chevaux participent : ")
	horses_played: int = int_input("Combien de chevaux sont joués : ")
	# ! is factorial
	# x = n ! / (n - p) !
	# y = n ! / (p ! * (n – p) !)
	x = math.factorial(horses_participating) / math.factorial(horses_participating - horses_played)
	y = math.factorial(horses_participating) / (
				math.factorial(horses_played) * math.factorial(horses_participating - horses_played))
	print(f"""• Dans l’ordre : une chance sur {int(x)} de gagner.
• Dans le désordre : une chance sur {int(y)} de gagner.""")

if __name__ == "__main__":
	ex2()