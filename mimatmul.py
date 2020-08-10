def mimatmul(A, B, N):                                        
    C= zeros((N,N))    
    
    for i in range(N):
        for j in range(N):
            for k in range(N):            
                C[i][j] = C[i][j] + A[i][j]* B[k][j]
                
                
    return (C)
