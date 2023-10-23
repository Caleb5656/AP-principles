#import pandas as pd
#df = pd.read_csv("data/prog505b", delim_whitespace=True, names=[] )
try:
    with open("data/prog505b", 'r') as f:
        grade = []
        person = []
        for line in f:

except Exception as e:
    print("Error:", e)