#o = x = ([1,2],(1,2))
#for i in range(10):
    #tem = input("?")
#x.append('1')
x = ["-","-","-"]
y = ["-","-","-"]
z = ["-","-","-"]

def plansza():
    print('\n',*x,'\n',*y,'\n',*z,sep=" ") #,end="").
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
#print("",end="")
#print(y)
plansza()

def przeczytaj(gdzie):
    print(" ")
przeczytaj(5)


for i in range(1,10):
    #print("i {}".format(i))
    ustaw("X",i)
    plansza()



















#.