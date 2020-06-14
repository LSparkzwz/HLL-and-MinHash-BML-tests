def true_inclusion_coeff(SX,SY):
    print("Python Intersection:")
    
    intersection = SY.intersection(SX)
    len_SX = len(SX)
    len_intersection = len(intersection)
    print("Size of SX:",len_SX)
    print("Size of SY:",len(SY))
    print("Size of Intersection:", len_intersection)
    print("True inclusion coefficient:", len_intersection / len_SX)
    
    return
