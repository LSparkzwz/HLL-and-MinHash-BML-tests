from datasketch import HyperLogLog

def lookup(P,minInc,maxInc,nx,ny,error,m,buckets,l,previousProb,previousPhi):
    nt = (minInc + maxInc) / 2
    phi = nt/nx
    prob = 0
    
    if nt == nx and nt == ny:
        prob = 1.0
    elif nt == 0:
        prob = eq_six(m,buckets,nx,ny,l)
    elif nx > ny and nt == ny:
        prob = eq_seven(m,buckets,nx,nt,l)
    else:
        prob = eq_eight(m,buckets,nx,ny,nt,l)

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
        return lookup(P,nt,maxInc,nx,ny,error,m,buckets,l,prob,phi)
    elif prob > P:
        return lookup(P,minInc,nt,nx,ny,error,m,buckets,l,prob,phi)      
       
def eq_six(m,buckets,nx,ny,l):
    pr = 0
    for k in range (0,l-m+1):
        pr = pr + pow(1 - 1/pow(2,k),nx/buckets) * (pow(1 - 1/pow(2,k),ny/buckets) - pow(1 - 1/pow(2,max(k-1,0)),ny/buckets))
        
    return pr
    
def eq_seven(m,buckets,nx,nt,l):
    pr = 0   
    for k in range (0,l-m+1):
        pr = pr + pow(1 - 1/pow(2,k),nx/buckets) * (pow(1 - 1/pow(2,k),nt/buckets) - pow(1 - 1/pow(2,max(k-1,0)),nt/buckets))
        
    return pr
    
def eq_eight(m,buckets,nx,ny,nt,l):
    pr = 0 
    for k in range (0,l-m+1):
        pr = (
             pr 
             + pow(1 - 1/pow(2,k),nx/buckets) * pow(1 - 1/pow(2,max(k-1,0)),nt/buckets) * (pow(1 - 1/pow(2,k),ny/buckets) - pow(1 - 1/pow(2,max(k-1,0)),ny/buckets))
             + pow(1 - 1/pow(2,k),nx/buckets) * (pow(1 - 1/pow(2,k),nt/buckets) - pow(1 - 1/pow(2,max(k-1,0)),nt/buckets)) * pow(1 - 1/pow(2,max(k-1,0)),ny/buckets)
             + pow(1 - 1/pow(2,k),nx/buckets) * (pow(1 - 1/pow(2,k),nt/buckets) - pow(1 - 1/pow(2,max(k-1,0)),nt/buckets)) * (pow(1 - 1/pow(2,k),ny/buckets) - pow(1 - 1/pow(2,max(k-1,0)),ny/buckets))
             )                        
    return pr   

def hll_bml(SX,SY):
    print()
    print("HLL BML")
    
    m = 8
    l = 32
    buckets = pow(2,m)
    error = pow(10,-5)
    print("Number of buckets is ", buckets)

    h1 = HyperLogLog(p=m)
    for d in SX:
        h1.update(d.encode('utf8'))
    
    h2 = HyperLogLog(p=m)
    for d in SY:
        h2.update(d.encode('utf8')) 
  
    nx = h1.count()  
    ny = h2.count()
    print("Estimated nx is ", nx)
    print("Estimated ny is ", ny)

    Vx = h1.digest()
    Vy = h2.digest()

    z = 0
    for i in range(0, buckets):
        if Vx[i] <= Vy[i]:
            z = z + 1
    P = z / buckets
    
    print("P is: ", P)
    
    print("Inclusion Coefficient: ", lookup(P,0,min(nx,ny),nx,ny,error,m,buckets,l,0,0))
    
    return
