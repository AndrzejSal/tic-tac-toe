
x = ["-","-","-"]
y = ["-","-","-"]
z = ["-","-","-"]

def plansza():
    #print('\n','\n','\n','\n','\n','\n','\n','\n')
#    #os.system("clear")
    print('\n',*x,'\n',*y,'\n',*z,sep=" ") #,end="").
def ustaw(co,gdzie):
    g = [z,y,x][(gdzie-1)//3]
    g[gdzie-1)%3] = co
plansza()

def przeczytaj(gdzie):
    global x,y,z
    g = [z,y,x][(gdzie-1)//3]
    return g[(gdzie-1)%3]
    #else:
    #    return ("Błąd adresu")
def check():
    for i in range(3):
        if przeczytaj(3*i)==przeczytaj(3*i+1)==przeczytaj(3*i+2)!="-":
            return przeczytaj(3*i)
        if przeczytaj(i)==przeczytaj(i+3)==przeczytaj(i+6)!="-":
            return przeczytaj(i)
    for i in range(2):
        if przeczytaj(i)==przeczytaj(1-i)==przeczytaj(2-i)!="-":
            return przeczytaj(i)
    return "-"
    
        
        











#.
