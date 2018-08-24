



#A Test to access your willpower
import time


print("******This is Quiz  by Prof.Manikant Roy******")

print("\n")
print("******This is Demo for the class CAP930*********")
print("\n")
print("******This is quiz based game for knowing your will power*********")
print("******Answer just nine question and you can know about your Will power !  *********")
print("****** Be Honest ! *********")

print("\n\n")
Score= 0 
def change():
    print("Q1.Do you embrace change ?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

def planing():
    print("Q2.Do you like planning ?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")


def assertive():
    print("Q3.Do you describe yourself as assertive?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")




def projects():
    print("Q4.Do you see projects throgh to fruition?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

def disciplined():
    print("Q5.Do you consider yourself disciplined?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

def concentrate():
    print("Q6.Do you find it easy to concentrate?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

def feel():
    print("Q7.Do you feel generally relaxed in  your life?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

def keep():
    print("Q8.Do you usually keep  your New Year's resolutions ?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

def mental():
    print("Q9.Do you believe we have unlimited mental resources ?")
    print("Press 1 for 'YES' ")
    print("Press 2 for 'SOMETIME'")
    print("Press 3 for 'RARELY'")
    print("Press 4 for 'NO'")
    S1= int(input("Your Choice "))
    if S1==1:
        return 4
    elif S1==2:
        return 3
    elif S1==3:
        return 2
    elif S1==4:
        return 1
    else:
        return print("Wrong Input")

         
        
#Score= Score +change() + planing()+ assertive()+projects()+disciplined()+concentrate()+keep()+mental()+feel()


Score = Score + change()
time.sleep(3)
print("\n")
Score = Score + planing()
time.sleep(3)
print("\n")
Score = Score + assertive()
time.sleep(3)
print("\n")

Score = Score + projects()
time.sleep(3)
print("\n")
Score = Score + disciplined()
time.sleep(3)
print("\n")
Score = Score + concentrate()
time.sleep(3)
print("\n")
Score = Score + keep()
time.sleep(3)
print("\n")
Score = Score +mental()
time.sleep(3)
print("\n")
Score = Score +feel()
time.sleep(3)

print("\n")

if Score >= 30:
    print("Your will power is very strong, Keep It Up")
    time.sleep(5)
elif Score >=20:
    print("Your will power is medium, Keep on improving")
    time.sleep(5)
else: 
    print("Your will power is Weak ! but nothing to be dissaponited .")
    time.sleep(5)
    
    


    

            

        
    
          


