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
def main():
    steps = []
    print("-1 to stop adding or end program")
    print("1. Add to step tracker")
    print("2. get Average steps taken")
    task = int(input("Select an option(0, 1, or 2): "))
    num = 0
    while task != -1:
        if task == 1:
            while num != -1:
                num = int(input("Enter the number of steps you've taken: "))
                if num != -1:
                    steps.append(num)
            task = input("Enter new task number: ")
        elif task == 2:
            if len(steps) == 0:
                print("Cannot take the average without any data!")
            elif len(steps) > 0:
                avg = average(steps)
                if isEnough(avg) == True:
                    print(f"Congrats you have been taking plenty of steps with your average being {avg}")
                else:
                    print(f"Try to get those steps up your average is {avg} try to aim for at least 7000 ")
            print("Enter new task number: ")
if __name__=="__main__":
    main()