gradebook = {"Seth Morris":{"HW1":"100","HW2":"98","HW3":"97"}}
student = ""
assignment = ""
assignments = {}
grade = ""
choice = ""
while True:
    print("new - new students and assignments")
    print("print - print students")
    print("assignments - print assignments of a student")
    print("update - update an existing grade")
    print("enter 'quit' to quit")
    choice = input()
    if choice=="new":
        print("New student or new assignment?")
        choice = input()
        if choice=="student":
            print("Please enter the student you would like to add.")
            student = input()
            gradebook[student]={}
        elif choice=="assignment":
            print("Please enter the name of the assignment.")
            assignment = input()
            print("Which student would you like to add this assignment to?")
            student = input()
            print("What is the grade for "+assignment)
            gradebook[student][assignment] = input()
    elif choice=="print":
        for i in gradebook:
            print(i)
    elif choice=="update":
        print("Whose grade would you like to update?")
        student = input()
        print("Which assignment do you want to update?")
        assignment = input()
        print("What is the new grade for "+assignment)
        gradebook[student][assignment] = input()
    elif choice=="grade":
        print("Which student's grade would you like?")
        student = input()
        grade = gradebook[student]
        print(grade)
    elif choice=="quit":
        break
    else:
        print("Invalid option")
        

