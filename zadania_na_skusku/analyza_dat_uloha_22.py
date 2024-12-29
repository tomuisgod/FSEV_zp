nums = []
try:
    with open("data.txt", "r") as f:
        for n in f:
            if n.strip():
                nums.append(float(n.strip()))
except FileNotFoundError:
    print("ERROR: Nenansiel sa zadany subor")
    exit(1)
except ValueError:
    print("ERROR: Zvoleny subor neobsahuje cisla")


def median(numers):
    numers = sorted(numers)
    length = len(numers)
    median = length // 2
    if length % 2 == 0:
        return (numers[median - 1] + numers[median]) / 2
    else:
        return numers[median]

def mod(numers):
    pass

med = median(nums)
print(nums)
print(med)
