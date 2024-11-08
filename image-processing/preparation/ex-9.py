#arithmetic coding
#range = high - low
#high = low + range*high
#low = low+range*low
#sym_low<e<sym_high
import random
data = list(map(int,input('enter the sequence').split()))

def calc_prob(data):
    prob = {}
    for i in data:
        prob[i] = prob.get(i,0)+1
        
    for i in prob:
        prob[i] = prob[i]/len(data)
    print(prob)
    return prob

def calc_cum(data,prob):
    cum = {}
    ptr = 0
    for sym,pr in prob.items():
        cum[sym] = (ptr,pr+ptr)
        ptr += pr
        
    print(cum)
    return cum
def encode(data,cum):
    low = 0
    high = 1
    ranges = []
    for sym in data:
        range_ = high-low
        high = low + range_ * cum[sym][1]
        low = low + range_ * cum[sym][0]
        ranges.append((low,high))
    print(ranges)
    
    return random.uniform(ranges[-1][0],ranges[-1][1])

def decode(e,cum,n):
    high = 1
    low = 0
    data = []
    
    for i in range(n):
        range_ = high - low
        sym_code = (e-low)/range_
        
        for sym,(sym_low,sym_high) in cum.items():
            if sym_low<=sym_code<=sym_high:
                data.append(sym)
                high = low+range_ * sym_high
                low = low+range_ * sym_low
                break
                
    print(data)
                
cum = calc_cum(data,calc_prob(data))
e = encode(data,cum)
print(e)

decode(e,cum,len(data))