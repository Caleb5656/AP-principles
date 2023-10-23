def isPrime(num):
    prime = True
    for i in range (2, round(num/2)):
        if num % i == 0:
            prime = False
            return prime

    return prime
def main():
    num = int(input("Enter a number: "))
    prime = isPrime(num)
    print("Is the number prime: ", prime)
if __name__ == "__main__":
    main()
# Enter a number: 16754
# Is the number prime:  False
# Enter a number: 11
# Is the number prime:  True