def isEnough(num):
    if num < 7000:
        return False
    else:
        return True

def average(step):
    avg = 0
    for i in step:
        avg += i
    avg = int(avg/len(step))
    return avg
def main():
    steps = []
    print("-1 to stop adding or end program")
    print("1. Add to step tracker")
    print("2. get Average steps taken")
    task = int(input("Select an option(-1, 1, 2): "))

    while task != -1:
        num = 0
        if task == 1:
            while num != -1:
                num = int(input("Enter the number of steps you've taken: "))
                if num == -1:
                    task = int(input("Enter new task number: "))
                    num = -1
                steps.append(num)
        if task == 2:
            if len(steps) == 0:
                print("Cannot take the average without any data!")
                task = int(input("Enter new task number: "))
            elif len(steps) > 0:
                avg = average(steps)
                if isEnough(avg):
                    print(f"Congrats you have been taking plenty of steps "
                          f"with your average being {avg}")
                else:
                    print(f"Try to get those steps up your average is "
                          f"{avg} try to aim for at least 7000 ")
                task = int(input("Enter new task number: "))
if __name__=="__main__":
    main()