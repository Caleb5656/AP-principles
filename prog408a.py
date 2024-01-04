from SortingAlgorithms import Sort
from cl408a import allsort
import time

# Import time, your sorting library, and your helper class


def main():
  try:
    data = []
    with open("Data/prog408a", 'r') as f:
      lines = f.readlines()
      for lcv in range(len(lines), 2):
        id = int(lines[lcv])
        score = int(lines[lcv+1])
        # Make helper class objects and add to data
        hello = allsort(id, score)
        data.append(hello)
    pass
    # Your code here
    bubble = Sort(data)
    start = time.perf_counter()
    Sort.bubble(bubble)
    data.reverse()
    end = time.perf_counter()
    bubble_time = end - start
    print("Bubble sorts time: ", bubble_time)
    print(data)

  except Exception as e:
    print("Error:", e)
  pass


if __name__ == "__main__":
  main()

