while(True):
    n = input()
    if not n:
        break
    else:
        a,b = n.split()
        if 0<int(a)<10 and 0<int(b)<10:
            print (int(a)+int(b))
        else:
            break
        
    
