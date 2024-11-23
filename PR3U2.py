def recursion(l):
    if(l!=[]):
        print(l[0],end=" ")
        recursion(l[1:])       
list1=[]
while True:

    print("\n1.insert")
    print("2.recursively print")
    print("3.Exit")
    choice=int(input("enter your choice"))
    if(choice==1):
        v=int(input("Enter value : "))
        list1.append(v)
    elif(choice==2):
        recursion(list1)
    else:
        break;
