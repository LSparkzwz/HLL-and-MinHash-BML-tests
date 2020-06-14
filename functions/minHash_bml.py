from datasketch import MinHash

def lookup(P,minInc,maxInc,nx,ny,error,m,num_perm,l,previousProb,previousPhi):
    nt = (minInc + maxInc) / 2
    phi = nt/nx
    prob = 0
    
    if nt == nx and nt == ny:
        prob = 1.0
    elif nt == 0:
        prob = eq_six(m,num_perm,nx,ny,l)
    elif nx > ny and nt == ny:
        prob = eq_seven(m,num_perm,nx,nt,l)
    else:
        prob = eq_eight(m,num_perm,nx,ny,nt,l)

	#print("nx:", nx) 
	#print("ny:", ny) 
    #print("nt:", nt)    
    #print("P:", P)
    #print("prob:", prob)
    #print("phi:", phi)  
    #print()
    
    if prob == previousProb:
        return previousPhi
    elif abs(prob - P) <= error:
        return phi
    elif prob < P:
        return lookup(P,nt,maxInc,nx,ny,error,m,num_perm,l,prob,phi)
    elif prob > P:
        return lookup(P,minInc,nt,nx,ny,error,m,num_perm,l,prob,phi)      
       
def eq_six(m,num_perm,nx,ny,l):
    pr = 0
    
    for k in range (0,l-m+1):
        pr = pr + pow(1 - 1/pow(2,k),nx/num_perm) * (pow(1 - 1/pow(2,k),ny/num_perm) - pow(1 - 1/pow(2,max(k-1,0)),ny/num_perm))
        
    return pr
    
def eq_seven(m,num_perm,nx,nt,l):
    pr = 0
        
    for k in range (0,l-m+1):
        pr = pr + pow(1 - 1/pow(2,k),nx/num_perm) * (pow(1 - 1/pow(2,k),nt/num_perm) - pow(1 - 1/pow(2,max(k-1,0)),nt/num_perm))
        
    return pr
    
def eq_eight(m,num_perm,nx,ny,nt,l):
    pr = 0
        
    for k in range (0,l-m+1):
        pr = (
             pr 
             + pow(1 - 1/pow(2,k),nx/num_perm) * pow(1 - 1/pow(2,max(k-1,0)),nt/num_perm) * (pow(1 - 1/pow(2,k),ny/num_perm) - pow(1 - 1/pow(2,max(k-1,0)),ny/num_perm))
             + pow(1 - 1/pow(2,k),nx/num_perm) * (pow(1 - 1/pow(2,k),nt/num_perm) - pow(1 - 1/pow(2,max(k-1,0)),nt/num_perm)) * pow(1 - 1/pow(2,max(k-1,0)),ny/num_perm)
             + pow(1 - 1/pow(2,k),nx/num_perm) * (pow(1 - 1/pow(2,k),nt/num_perm) - pow(1 - 1/pow(2,max(k-1,0)),nt/num_perm)) * (pow(1 - 1/pow(2,k),ny/num_perm) - pow(1 - 1/pow(2,max(k-1,0)),ny/num_perm))
             )                        
    return pr   


def minHash_bml(SX,SY):
    print()
    print("MinHash BML")

    l = 32
    m = 8
    num_perm = pow(2,m)
    error = pow(10,-5)

    print("Number of permutations is ", num_perm)

    m1 = MinHash(num_perm)
    m2 = MinHash(num_perm)
    
    for d in SX:
        m1.update(d.encode('utf8'))
    for d in SY:
        m2.update(d.encode('utf8'))
  
    nx = m1.count()  
    ny = m2.count()
    print("Estimated nx is ", nx)
    print("Estimated ny is ", ny)
    
    Vx = m1.digest()
    Vy = m2.digest()

    z = 0
    for i in range(0, num_perm):
        if Vx[i] >= Vy[i]:
            z = z + 1
    P = z / num_perm

    print("P is: ", P)
    print("Inclusion Coefficient: ", lookup(P,0,min(nx,ny),nx,ny,error,m,num_perm,l,0,0))
    
    return
