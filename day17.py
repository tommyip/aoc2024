regs = [45483412, 0, 0]
instrs = [2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0]
ptr = 0
out = []
while ptr < len(instrs):
    opcode, literal = instrs[ptr : ptr + 2]
    combo = literal if literal <= 3 else regs[literal - 4]

    match opcode:
        case 0:
            regs[0] = regs[0] // (2**combo)
        case 1:
            regs[1] = regs[1] ^ literal
        case 2:
            regs[1] = combo % 8
        case 3:
            if regs[0] != 0:
                ptr = literal
                continue
        case 4:
            regs[1] = regs[1] ^ regs[2]
        case 5:
            out.append(str(combo % 8))
        case 6:
            regs[1] = regs[0] // (2**combo)
        case 7:
            regs[2] = regs[0] // (2**combo)
    ptr += 2

print(",".join(out))


def invert(out, bit):
    states = set()
    window = min(48 - bit, 10)
    for a in range(2**window):
        shift = (a & 0b111) ^ 0b011
        c = (a >> shift) & 0b111
        b = shift ^ c ^ 0b101
        if b == out:
            states.add((c, shift, a & 0b111))
    return states


possible = {0}
for i in reversed(range(16)):
    states = invert(instrs[i], i * 3)
    next_possible = set()
    for A in possible:
        for c, shift, a in states:
            A_ = A << 3 | a
            if (A_ >> shift) & 0b111 == c:
                next_possible.add(A_)
    possible = next_possible

print(min(possible))
