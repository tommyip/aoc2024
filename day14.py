import numpy as np
from tqdm import tqdm

inputs = open("inputs/day14.txt").read().splitlines()

h, w = 103, 101
mid_h, mid_w = (h - 1) // 2, (w - 1) // 2
seconds = h * w
quads = [0] * 4
entropies = np.zeros((seconds,))
img = np.zeros((h, w), dtype=np.int8)

for sec in tqdm(range(seconds)):
    for line in inputs:
        p, v = line.split(" ")
        p = complex(*map(int, p[2:].split(",")))
        v = complex(*map(int, v[2:].split(",")))
        p += v * sec
        x, y = int(p.real) % w, int(p.imag) % h
        img[y, x] += 1

        if sec == 100:
            match (x < mid_w, x > mid_w, y < mid_h, y > mid_h):
                case (True, False, True, False):
                    quads[0] += 1
                case (True, False, False, True):
                    quads[1] += 1
                case (False, True, True, False):
                    quads[2] += 1
                case (False, True, False, True):
                    quads[3] += 1

    # Calculate entropy
    # https://stackoverflow.com/a/45091961
    value, counts = np.unique(img, return_counts=True)
    norm_counts = counts / counts.sum()
    entropy = -(norm_counts * np.log(norm_counts)).sum()
    entropies[sec] = entropy

    img[...] = 0


print(quads[0] * quads[1] * quads[2] * quads[3])
print(np.argmin(entropies))
