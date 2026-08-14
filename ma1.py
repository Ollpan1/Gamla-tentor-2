import math

def sum_prime(x): ##Exercise A1
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
    if x == 1:
        return 0
    else:
        if is_prime(x):
            return x + sum_prime(x-1)
        else:
            return sum_prime(x-1)
    pass

def base11(x): ##Exercise B1
    if x < 11:
        if x == 10:
            return 'A'
        return str(x)
        return str(x)
    elif x % 11 == 10:
        return str(base11(x // 11)) + 'A'
    else:
        return str(base11(x // 11)) + str(x % 11)
def main():
    print("Test A1:")
    for x in [4,5,6,7,100]:
        print(sum_prime(x), end=" ")
    print("")
    print("Your answer to A2: what is the problem of recursive implementation of A1?")
    print("")
    print("Test B1:")
    for x in [0,9, 44, 120, 1000,1111]:
        print(base11(x), end=" ")
if __name__ == '__main__':
    main()
