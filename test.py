spnsh = {"mirar":"to watch","sacar":"to take","esperar":"to wait or to hope","invitar":"to invite","buscar":"to look for","predicar":"to preach","ensenar":"to teach","tocar":"to play(intrument,etc.)","jugar":"to play(game,etc.)","senular":"to signal","reservar":"to reserve"}
word = ""
definiton = ""
choice = ""
while True:
    print("enter 'quit' to quit")
    choice = input()
    if choice=="new":
        print("Please enter the word you wish to add")
        word = input()
        print("Please enter the definition of "+word)
        definition = input()
        spnsh[word] = [definition]
    elif choice=="print":
        for i in spnsh:
            print(i)
    elif choice=="definition":
        print("Which word would you like the definition of?")
        word = input()
        definition = spnsh[word]
        print(definition)
    elif choice=="quit":
        break
    else:
        print("Invalid option")
        

