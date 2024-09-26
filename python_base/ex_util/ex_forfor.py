







def test():
    for i in range(10000):
        for j in range(10000):
            print(f"{i} {j}")
            if j ==100:
                return
test()