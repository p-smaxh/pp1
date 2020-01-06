nr = 2
pozostale = 30-nr 
dni = ["PN", "WT", "SR", "CZ", "PT", "SB", "ND"]
print("|", " | ".join(dni), "|")
for n in range(0,5,1):
    for m in range(1,8):
        if (m+(n*7)-nr<=0):
            print("   "," ",end="")
        else:
            if (m+(n*7)-nr<=30):
                if(m+(n*7)-nr<10):
                    print(" ",m+(n*7)-nr," ",end="")
                else:
                    print(" ",m+(n*7)-nr,"",end="")
    print("")
