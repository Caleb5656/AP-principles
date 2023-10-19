try:
    with open("data/prog505a", 'r') as f:
        for line in f:
            print()
except Exception as e:
    print("Error:", e)