import time
import searching_algorithms
def main():
  try:
    data = []
    with open("Data/prog408b.dat", 'r') as f:
      data = [int(line) for line in f]

    hello = int(input("Enter an Integer to be searched for: "))
    start = time.perf_counter()
    hi = searching_algorithms.LinearSearch(data, hello)
    end = time.perf_counter()
    tot = end - start
    print(f"Linear search in unsorted list: {hi} took {tot:.8f} seconds")

    data.sort()
    start = time.perf_counter()
    hi = searching_algorithms.LinearSearch(data, hello)
    end = time.perf_counter()
    tot = end - start
    print(f"Linear search in sorted list: {hi} took {tot:.8f} seconds")
    start = time.perf_counter()
    hi = searching_algorithms.BinarySearch(data, hello)
    end = time.perf_counter()
    tot = end - start
    print(f"Binary search: {hi} took {tot:.8f} seconds")
  except Exception as e:
    print("Error:", e)
  pass


if __name__ == "__main__":
  main()

# Enter an Integer to be searched for: 338
# Linear search in unsorted list: 83 took 0.00001440 seconds
# Linear search in sorted list: 67 took 0.00000540 seconds
# Binary search: 67 took 0.00000460 seconds
