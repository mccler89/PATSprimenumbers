__author__ = 'Pat McClernan'


def primenumbers(num):
    thisnum = 4
    num = int(num)
    for thisnum in range(2, num + 1, 1):
        if isPrime(thisnum): print(thisnum)

    return 0

def isPrime(num):
    flag = True;
    for i in range(int(num - 1), 1, -1):
        if num%i == 0: flag = False;

    return flag

num = input("Provide an integer to get all primes less than that number:")
primenumbers(num)