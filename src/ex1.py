from utils.inputs import int_input

def ex1() -> None:
	array = [int_input(f"Entrez le nombre n°{i} : ") for i in range(1, 11)]
	print(f"""Le plus grand de ces nombres est : {max(array)}
Son index est : {array.index(max(array))}""")

if __name__ == "__main__":
	ex1()