from scipy.stats import ks_2samp
import numpy as np
import random

def run_ks(lst1, lst2):
    data1 = np.array(lst1, np.int32)
    data2 = np.array(lst2, np.int32)

    #returns first index of tuple: (p-value, test-statistic)
    return ks_2samp(data1, data2)

def test_ks():
    rand_lst1 = [random.randint(0,1000) for r in xrange(1000)]
    rand_lst2 = [random.randint(0,1000) for r in xrange(1)]
    print "RANDOM LIST 1", rand_lst1
    print "RANDOM LIST 2", rand_lst2
    print "P-VALUE OF KS TEST", run_ks(rand_lst1, [0] + rand_lst1[1:])

if __name__ == '__main__':
    test_ks();
