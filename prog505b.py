#import pandas as pd
#df = pd.read_csv("data/prog505b", delim_whitespace=True, names=[] )
try:
    with open("data/prog505b", 'r') as f:
        grade = []
        person = []
        for line in f:
            name = line + " " + (line + 1)
            line += 2
            g1 = int(line)
            line += 1
            g2 = int(line)
            line += 1
            g3 = int(line)
            line +=1
            g4 = int(line)
            line +=1
            g5 = int(line)
            person.append(name)
            grade.append(g1, g2, g3, g4, g5)

except Exception as e:
    print("Error:", e)