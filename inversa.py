import numpy as np


def inversa(A,B):
    a=np.array(A, float)
    b=np.array(B, float)
    InversaA = np.linalg.inv(a)
    print("Inversa de la matriz: A^-1" )
    print(InversaA )
    Solucion = np.matmul(InversaA, b)
    print("Se saca el producto AB:" )
    print(np.column_stack((InversaA,b)))
    print("Resultado: ")
    print(np.squeeze(Solucion))
    
    return(np.squeeze(Solucion))