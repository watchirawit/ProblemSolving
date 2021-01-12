import time 

def SequencesV1(n):
    total = 0
    for i in range(n):
        total += (i+1)
    return total
def SequencesV2(n):
    #return int(n/2*(2+(n-1)))
    return n * (n + 1)/2
n = int(input('Input Value: '))

start = time.time()
print('Answer1: ',SequencesV1(n))
print('time1',(time.time()-start)*1000)

start1 = time.time()
print('Answer2: ',SequencesV2(n))
print('time2',(time.time()-start1)*1000)