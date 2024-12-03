m1 = m2 = open("inputs/day03.txt").read().replace("'", "")
enabled = {0}


def run(m, sum):
    mul = lambda x, y: sum.add(sum.pop() + len(enabled) * x * y)
    while m:
        try:
            line = m[: m.index(")") + 1]
            if line.startswith("mul") or line.startswith("do"):
                eval(line)
                m = m[len(line) :]
                continue
        except:
            pass
        m = m[1:]
    print(sum.pop())


run(m1, {0})
do = lambda: enabled.add(0)
dont = lambda: enabled.clear()
run(m2, {0})
