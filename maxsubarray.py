def maxsubarray(a):
        maxsofar=a[0]
        maxhere=0
        for i in range(0,len(a)):
                maxhere=maxhere+a[i]
                if(maxhere<0):
                        maxhere=0
                elif(maxhere>maxsofar):
                        maxsofar=maxhere
        return(maxsofar)


a=[int(x) for x in input().split()]
print(maxsubarray(a))

