#mport pandas as pd
#df = pd.read_csv("data/prog505b", delim_whitespace=True, names=[] )
try:
    with open("data/prog505b", 'r') as f:
        grade = []
        
        for line in f:
            hi = line
            grade.append(hi)

except Exception as e:
    print("Error:", e)