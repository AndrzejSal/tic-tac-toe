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
    if gdzie > 6:
        gdzie-= 6
        x.insert(gdzie, 'X')
        x.remove(z[gdzie+1])
    elif gdzie > 3:
        gdzie -= 3
        y.insert(gdzie, 'X')
        y.remove(z[gdzie+1])
    else:
        z.insert(gdzie-1, 'X')
        print(z)
        #print(len(z))
        z.insert(z[gdzie],gdzie)
#        print(gdzie+1)
        print(z)
ustaw("X",3)
print(z)

def przeczytaj(gdzie):
    print(" ")
przeczytaj(5)




























#.