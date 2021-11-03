import numpy as np

result = []

def cramer(A,B):
    result.clear()
    a=np.array(A, float)
    b=np.array(B, float)
    
    n=len(b)
    D=np.linalg.det(a)
    x=np.zeros(n)
    
    for k in range(n):
        Ak=a.copy()
        Ak[:,k]=b
        Dk=np.linalg.det(Ak)
        x[k]=Dk/D
        print("Se va sacando cada determinante")
        print(Ak, 'determinante')
        print('resultado: ', round(x[k],10))
        print()
        result.append(round(x[k],10))
        
    return result