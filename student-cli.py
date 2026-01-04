while True:
    print("-----Student Management-----")
    print("\nMenu")
    print("1. Add student")
    print("2. View students")
    print("3. Remove student")
    print("4. Course operations")
    print("5. Exit")
    ch=int(input("Enter ur choice: "))
    students={}
    if ch==1:
        id=int(input("Enter Id of student: "))
        name=input("Enter Name of student: ")
        age=int(input("Enter age of student: "))
        sub=input("Enter Subjects (seperated by commas): ").split(",")
        student=(id,name,age,set(sub))
        students[id]=student
        print("Student record added!")
    elif ch==2:
        if students=={}:
            print("No records")
        else:
            for i in students:
                print(i)
    else:
        print("Invalid Option")
    op=input("Do u want to continue(y/n): ")
    if op=='n' or op=="N":
        break