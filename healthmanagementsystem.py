a = int(input("Do you want to log an entry or retrieve entries \n press 1 to log or 2 to retrieve :"))
n1 = int(input("press 1 for Execersies and 2 for food"))
n2 = int(input("Press 1 for name1, Press 2 for name2 and 3 for name3"))


def getdate():
    import datetime
    return datetime.datetime.now()

if a ==1 :
    if n1==1 and n2==1 :
        f= open("name1e","a")
        inp =input("Enter the execerses performed by harry \n ")
        time = str(getdate())
        f.write(inp+ "[" + time + "]" +"\n")
        f.close()
    elif n1==2 and n2==1:
        f1=open("name1f","a")
        inp1=input("Enter the meals taken by harry \n")
        time = str(getdate())
        f1.write(inp1+ "[" + time+ "]" +"\n")
        f1.close()
    elif n1==1 and n2==2:
        f3=open("name2e","a")
        inp2=input("Enter the exercises done by rohan \n")
        time = str(getdate())
        f3.write(inp2+ "[" + time + "]" +"\n")
        f3.close()
    elif n1==2 and n2==2:
        f4=open("name2f","a")
        inp3=input("Enter the  meals taken by rohan \n")
        time = str(getdate())
        f4.write(inp3+ "[" + time + "]" +"\n")
        f4.close()
    elif n1==1 and n2==3:
        f5=open("name3e","a")
        inp4=input("Enter the exercises done by hammad \n")
        time = str(getdate())
        f5.write(inp4+ "[" + time + "]" +"\n")
        f5.close()
    elif n1==2 and n2==3:
        f6=open("name3f","a")
        inp5=input("Enter the meals taken by hammad \n")
        time = str(getdate())
        f6.write(inp5+ "[" + time + "]" +"\n")
        f6.close()
    else:
        print("enter valid details")
if a==2:
    if n1==1 and n2==1:
        f=open("name1e","rt")
        print(f.read())
        f.close()
    elif n1==2 and n2==1:
        f1=open("name1f")
        print(f1.read())
        f1.close()
    elif n1==1 and n2==2:
        f2=open("name2e")
        print(f2.read())
        f2.close()
    elif n1==2 and n2==2:
        f3=open("name2f")
        print(f3.read())
        f3.close()
    elif n1==1 and n2==3:
        f4=open("name3e")
        print(f4.read())
        f4.close()
    elif n1==2 and n2==3:
        f5=open("name3f")
        print(f5.read())
        f5.close()