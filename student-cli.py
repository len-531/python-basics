print("-----Student Management-----")
print("\nMenu")
print("1. Add student")
print("2. View students")
print("3. Remove student")
print("4. Course operations")
print("5. Exit")
ch=int(input("Enter ur choice: "))
if ch==1:
    id=int(input("Enter Id of student: "))
    name=input("Enter Name of student: ")
    age=int(input("Enter age of student: "))
    sub=input("Enter Subjects (seperated by commas): ").split(",")
    student=(id,name,age,set(sub))
    print(student)
elif ch==2:
    for i in student:
        print(i)
else:
    print("Invalid Option")