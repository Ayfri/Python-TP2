import math

from utils.inputs import int_input

def ex4() -> None:
	"""
	Faire un programme qui calcule la suite (Rn) définie par les conditions suivantes :
	R1 = sqrt(2)
	Rn+1 = sqrt(2 + Rn)

	:return: None
	:rtype: None
	"""

	n = int_input()
	r1 = math.sqrt(2)
	rn = r1
	length = int(math.log10(n))
	print(f"R1 = {r1}")
	for i in range(1, n +1):
		if i % 10**length == 0 and i > 1:
			print(f"R{i} = {rn}")
		rn = math.sqrt(2 + rn)
	print(f"Le résultat de R[{n}] est {rn}.")

if __name__ == "__main__":
	ex4()
