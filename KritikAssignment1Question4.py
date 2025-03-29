def ApproxArctanFunc(x):
    n=0
    if x<=1 and x>=0:
        outputnum=0
        while ((x**(2*n+1))/(2*n+1))>=0.0001:
            outputnum+=(((-1)**n)*(x**(2*n+1)))/((2*n)+1)
            n+=1
        if n==0:
            pass
        else:
            n-=1
        finaltuple = (outputnum, n, ((x**(2*n+1))/(2*n+1)))
        return finaltuple
    else:
        ErrMsg="Error!"
        return ErrMsg
x = float(input(" "))
print(ApproxArctanFunc(x))
#print(ApproxArctanFunc(-1))
#print(ApproxArctanFunc(0))
#print(ApproxArctanFunc(0.25))
#print(ApproxArctanFunc(0.5))
#print(ApproxArctanFunc(0.75))
#print(ApproxArctanFunc(1))