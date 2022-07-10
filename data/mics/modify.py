with open("data.csv",'r') as a:
    with open("trial.csv", 'w') as b:
        for data in a.readlines():
            w = data.split(',')
            line = f"{w[0]},{w[1]},{w[2]}"
            b.writelines(line)
            for num in w[3]:
                if num =="\n":
                    continue
                b.writelines(f",{num}")
            b.writelines("\n")