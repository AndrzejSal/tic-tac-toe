import os#o = x = ([1,2],(1,2))
#for i in range(10):
    #tem = input("?")
#x.append('1')
x = ["-","-","-"]
y = ["-","-","-"]
z = ["-","-","-"]

def plansza():
    #print('\n','\n','\n','\n','\n','\n','\n','\n')
    #os.system("clear")
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
    global x,y,z
    g = {1:z,2:z,3:z,4:y,5:y,6:y,7:x,8:x,9:x,}
    #print("[A]",gdzie)
  #  print("[B]",g[gdzie])
   # print("D",str(g[gdzie]))
    if gdzie < 4:
        return (g[int(gdzie)])[int(gdzie-1)]
    elif gdzie < 7:
        return (g[int(gdzie)])[int(gdzie-4)]
    elif gdzie < 10:
        return (g[int(gdzie)])[int(gdzie-7)]
    else:
        return ('\033[91m'"Z")
    #if [7,8,9].count(gdzie) == 1:
     #   if gdzie == 7:
      #      return(x[0])
       # elif gdzie == 8:
        #    return
    #elif [4,5,6].count(gdzie) == 1:
    #elif [1, 2, 3].count(gdzie) == 1:
#for i in range(10):
 #   print(przeczytaj(i+1))
#for i in range(1,10):
    #print("i {}".format(i))
 #   ustaw("X",i)
  #  plansza()
#ustaw("XDDDDDDD",4)
#plansza()


















#.