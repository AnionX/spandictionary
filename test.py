gradebook = {"Seth Morris":"A"}
student = ""
assignment = ""
grade = ""
choice = ""
while True:
    print("enter 'quit' to quit")
    choice = input()
    if choice=="new":
        print("Please enter name of the student you wish to add")
        student = input()
        print("Please enter the assignment for "+student)
        assignment = input()
        gradebook[student] = [assignment]
    elif choice=="print":
        for i in gradebook:
            print(i)
    elif choice=="grade":
        print("Which student's grade you like?")
        student = input()
        grade = gradebook[student]
        print(grade)
    elif choice=="quit":
        break
    else:
        print("Invalid option")
        

