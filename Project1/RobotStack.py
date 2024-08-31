def waysToDistribute(arrange,b,n,k):
    #Base cases
    if b == 0: return 1
    if b < 0 or n == 0: return 0
    
    #Memoization
    if (b,n,k) not in arrange: 
        result = 0
        for i in range(k+1):
            result=result+waysToDistribute(arrange,b-i,n-1,k)
        
        arrange[(b,n,k)]=result
    return arrange[(b,n,k)]

content = open('input.txt', "r")
for line in content:
    inputs = tuple(map(int,line.split(",")))
    memo_dict = {}
    print(inputs,"=", waysToDistribute(memo_dict,inputs[0],inputs[1],inputs[2]))
