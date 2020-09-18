import numpy as np
import numpy.random as npr

def ApxMedian(A,k,e=False):
    """
    Fast approximate median of A, using k samples. If e=True, finds a k such
    that the approximate median will be returned with error bounded by
    max(ne, |1-ne|).
    """
    num_samples = k
    if e:
        num_samples = np.ceil(2/(k**2)).astype(int)
    I = npr.randint(low=0, high=A.size-1, size=num_samples)
    sample = np.array(A)[I]
    return np.sort(sample)[num_samples//2]

if __name__ == "__main__":
    test = npr.randint(low=1, high=20000, size=20000)
    print("Array Size: ", 20000)
    print("Number of Samples: ", np.ceil(2/(0.1**2)).astype(int))
    print("Approx: ", ApxMedian(test, 0.1, e=True))
    print("Actual: ", np.median(test))
