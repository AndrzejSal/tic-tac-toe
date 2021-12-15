#o = x = ([1,2],(1,2))
#for i in range(10):
    #tem = input("?")
#x.append('1')
x = ["-","-","-"]
y = ["-","-","-"]
z = ["-","-","-"]

def plansza():
    print('\n',x,'\n',y,'\n',z)
#plansza()
#k = print ("Podaj koordynaty pola")
def ustaw(co,gdzie):
    gdzie -= 1
    if gdzie > 5:
        gdzie-= 6
        x[gdzie] = co
    elif gdzie > 2:
        gdzie -=3
        y[gdzie] = co
    else:
        z[gdzie] = co
        #print(z)
ustaw("X",1)
#print(y)
plansza()

def przeczytaj(gdzie):
    print(" ")
przeczytaj(5)



ustaw("X",2)
plansza()
ustaw("X",3)
plansza()
ustaw("X",4)
plansza()
ustaw("X",5)
plansza()
ustaw("X",6)
plansza()
ustaw("X",7)
plansza()
ustaw("X",8)
plansza()
ustaw("X",9)
plansza()






















#.