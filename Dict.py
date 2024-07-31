DIP={'A':1,'B':1,'C':2,'D':3,'E':2,'F':2,'G':3,'H':4,'I':3}

DOP={}

for i in DIP.values():
    if i in DOP.keys():
        DOP[i]=DOP[i]+1
    else:
        DOP[i]=1
print(DOP)
    
