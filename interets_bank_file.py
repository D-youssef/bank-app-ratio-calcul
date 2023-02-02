
from asyncio.windows_events import NULL

# p     =>  percentage transformit to %
# ratio =>  percentage of %
# d     =>  days
# c     => capital

def interest(c=NULL,p=NULL,d=NULL) :
    ratio = p * 0.01  
    for i in range (1,d) :
        c = c + c * ratio
    return c

# result = interest(100,1,30)
# print(result)

