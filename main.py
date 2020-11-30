import numpy as np


def reshape_arr(l):
    three_d = np.array(l)
    three_d = np.reshape(three_d, (3,3))

    return three_d

def calculate(l):

    try:
        output = {}
        three_d = reshape_arr(l)
        
        mean = [list(three_d.mean(axis=0)), list(three_d.mean(axis=1)), three_d.flatten().mean()]
        variance = [list(three_d.var(axis=0)), list(three_d.var(axis=1)), three_d.flatten().var()]
        std_dev = [list(three_d.std(axis=0)), list(three_d.std(axis=1)), three_d.flatten().std()]
        mx = [list(three_d.max(axis=0)), list(three_d.max(axis=1)), three_d.flatten().max()]
        mn = [list(three_d.min(axis=0)), list(three_d.min(axis=1)), three_d.flatten().min()]
        sm = [list(three_d.sum(axis=0)), list(three_d.sum(axis=1)), three_d.flatten().sum()]

        output['mean'] = mean
        output['variance'] = variance
        output['standard deviation'] = std_dev
        output['max'] = mx
        output['min'] = mn
        output['sum'] = sm

        return output

    except ValueError:
        raise ValueError("List must contain nine numbers.")
  

arr = [0,1,2,3,4,5,6,7,8]
print(calculate(arr))    