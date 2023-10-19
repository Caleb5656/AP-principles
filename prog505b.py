try:
    with open("data/prog505b", 'r') as f:
        for line in f:
            print()
except Exception as e:
    print("Error:", e)