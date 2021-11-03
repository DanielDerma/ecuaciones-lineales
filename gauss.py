from numpy import array, zeros, column_stack

def gauss_init(A,B):
    a = array(A,float)
    b = array(B,float)   
    
    n = len(b)
    x = zeros(n, float)
    
    #Eliminacion
    for k in range(n-1):
        for i in range(k+1, n):
            if a[i,k] == 0: continue 
            factor = a[k,k]/a[i,k] 
            for j in range(k,n):
                a[i,j] = a[k,j] - a[i,j]*factor
            b[i] = b[k] - b[i]*factor
        print("Operacion ",k+1)
        print(column_stack((a,b)))
        
    #Sustitucion hacia atras
    x[n-1] = b[n-1] / a[n-1,n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += a[i,j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i,i]
    return x;

    