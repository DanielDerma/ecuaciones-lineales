import numpy as np

def gssjrdn(A,B):
    a=np.array(A, float)
    b=np.array(B, float)
    n = len(b)
    
    for k in range(n):
         #pivote
            if np.fabs(a[k,k]) < 1.0e-12: # < 0
                for i in range(k+1, n):
                    if np.fabs(a[i,k]):
                        if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                            for j in range(k,n):
                                a[k,j],a[i,j] = a[i,j],a[k,j]
                            b[k],b[i] = b[i], b[k]
                            break
                                        
            # divide el pivote
            pivot = a[k,k]
            for j in range(k,n):
                a[k,j] /= pivot
            b[k] /= pivot
            
            #Eliminacion
            for i in range(n):                
                if i == k or a[i,k] == 0: continue
                factor = a[i,k]
                for j in range(k,n):
                    a[i,j] -= factor * a[k,j]
                b[i] -= factor * b[k]    
            print(np.column_stack((a,b)), 'Opearcion')
    
    return b









                        