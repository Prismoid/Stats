# 統計検定１級理工学、2022年大問４より
import random
import numpy as np
import matplotlib.pyplot as plt

def f(_x):
    return 60 * np.power(_x, 3) * np.power(1 - _x, 2)

def getRnd(_c, _rn1, _rn2):
    cond = lambda x, y: x < f(y)

    retArr = _rn2[cond(_c * _rn1, _rn2)]
    
    return retArr
    
def main(): 
    # 一様乱数を100個生成
    rn1, rn2 = np.random.uniform(0, 1, 10000), np.random.uniform(0, 1, 10000) 
    c0 = np.power(6/5, 4)
    c1, c2 = c0 + 0.1, c0 -0.1 # 0.05など極端な値で実験すると良い。

    for c in [c0, c1, c2]: 
        arr = getRnd(c, rn1, rn2)
        plt.hist(arr, bins=200, edgecolor='black')
        plt.show()
        print(len(arr))
main()
    
    
    

    

