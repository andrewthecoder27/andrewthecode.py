griffindor = 0
ravenclaw = 0
slythern = 0
hufflepuff = 0

name = input("Hello student what is your name? ")
if name == 'godric gryffindor':
    griffindor += 100
elif name == 'rowena ravenclaw':
    ravenclaw += 100
elif name == 'salazar slytherin':
    slythern += 100
elif name == 'helga hufflepuff':
    hufflepuff += 100
age = input ("what is your age wizard? ")
if age == 71:
    slythern += 100
elif age == 150:
    griffindor += 100
elif age == 993:
    ravenclaw += 100
elif age == 0:
    hufflepuff += 1
q9 = input(f" {name}, do you belong in hogwarts? y/n ")

if q9 == "y":
    print ("welcome to the sorting hat! ")
elif q9 == "teacher":
    print(" you may get your classroom ready ")
else:
    print (" you should not be here, you are a muggle! ")
qg = input(f'{name}, do you have an account at Gringotts? ')
if qg == 'y':
    print("wecome to another magical year! ")
if qg == 'p':
    print("you are you know who you are bannished! ")
if qg == 'im you know who':
    print ("the ministry of magic is on there way to catch you once and for all")
    slythern += 1000
else:
    print ("are you a muggle?\n")
print(f"{name.title()}, here are the houses: [G]riffindor, [R]avenclaw, [S]lythern, [H]huuflepuff")

q1 = input('Which is your favorite house ')

if q1 == "G":
    griffindor += 1

elif q1 == "R":
    ravenclaw += 1

elif q1 == "S":
    slythern += 1

else:
    hufflepuff += 1

    q2 =input(f"{name.title()}, are you he who shall not be named? y/n ")

    if q2 == 'y':
        slythern += 20
        print (" We know who you are now ")
    else:
        print (" you are free to go ")

        q3 = input(f"{name.title()}, which color do you prefer? [R]ed, [Y]ellow, [B]lue, [G]reen ")
        if q3 == "R":
            griffindor += 1
        elif q3 == 'Y':
         hufflepuff += 1
        elif q9 == 'B':
         ravenclaw += 1
        else:
         slythern +=1
         
         q4 = input (f"{name.title()}, What is your favorite pet? [T]oad, [C]at, [O]wl, if other press [A] ")
        if q4 == 'T':
             hufflepuff += 10
        elif q4 == 'C':
             ravenclaw += 10
        elif q4 == 'O':
             griffindor += 10
        else:
             slythern += 10
            
    q5 = input (f"{name.title()}, What is your favorite Harry Potter caricter? [H]arry Potter,[L]una Lovegood,[S]nape, [C]edric") 
            if q5 == 'H':
            griffindor += 10
             elif q5 == 'L':
            ravenclaw += 10
             elif q5 == 'S':
            slythern += 10
             else:
            hufflepuff += 10
     q6 = input (f"{name.title()}, would you like to continue? y/n
        if q6 == 'n':
            exit()
       else:
           continue
        q7 = input (f"{name.title()}, what is your favorite Harry Potter food [B]utterbeer, [C]hoclate frogs, c[O]ldren cakes")
        if q7 == 'B':
            print ("if you are above 21 you can drink butter beer. your age is"+age)
            
        
        
    
