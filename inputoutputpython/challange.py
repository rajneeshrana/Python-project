with open("sample2.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} in {2}". format(i, j, i * j ), file=tables)
        print("-" * 40, file=tables)