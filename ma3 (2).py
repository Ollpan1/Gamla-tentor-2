import concurrent.futures as future
import numpy as np
import math
import random


def is_prime(n):
    """ Returns true if n is prime
    """
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime
def sum_prime(x): ##Exercise A5
    lst = [i for i in range(x)]
    res = filter(is_prime, lst)
    res = list(res)
    return sum(res)
def generate_normal(n):
    a = np.random.randint(0,9)
    b = np.random.randint(1, 10)
    return np.random.normal(a,b,n)
def Estimation(arr): ##Exercise A6
    n_p = 10
    reshaped = arr.reshape(n_p, -1)
    with future.ProcessPoolExecutor(n_p) as ex:
        medel = ex.map(np.mean, reshaped)
    medel = list(medel)
    totalmedel = np.mean(medel)
    return totalmedel

def is_even_rounded(sub_frac):
    return np.sum(np.round(sub_frac) % 2 == 0)
def prob_even(n): #Exercice B4
    x = np.random.uniform(0,1,n)
    y = np.random.uniform(0,1,n)
    frac = x/y
    n_p = 10
    chunk_size = n // n_p
    chunks = frac.reshape(n_p, -1)
    with future.ProcessPoolExecutor(max_workers=n_p) as ex:
        res = ex.map(is_even_rounded,chunks)
    res = list(res)
    return sum(res)/n


def main():

    print("Test A5:")
    for x in [4, 5, 6, 7, 100, 1000]:
        print(sum_prime(x), end=" ")
    print("\nTest A6:")
    n = 10**6
    arr = generate_normal(n)
    print(Estimation(arr))
    print("Test B4:")
    n = 10**7
    prob = (prob_even(n))
    print(prob, 5-4*prob)
    print("B4: What is the probability of getting an even number?")
if __name__ == '__main__':
    main()