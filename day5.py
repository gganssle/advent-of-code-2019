import numpy as np

with open('day5_inpt.txt', 'r') as f:
    inpt = f.read()

#print(len(inpt))

inpt = list(inpt)

uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pairs = []
for ele in zip(uppers, lowers):
    pairs.append(ele[0] + ele[1])
    pairs.append(ele[1] + ele[0])

pass_number = 1

paired = [inpt[i] + inpt[i+1] for i in range(0, len(inpt)-1, 2)]

for i in range(500):
    print(f'pass number {pass_number}, input is length {len(paired)*2}')

    # this is for the even numbered splits
    for j, ele in enumerate(paired):
        if ele in pairs:
            del paired[j]

    # this is for the odd numbered splits
    paired = ''.join(paired)
    first = paired[0]; last = paired[-1]
    paired = [paired[k] + paired[k+1] for k in range(1, len(paired)-2, 2)]
    paired.append(last)
    paired.insert(0, first)

    for j, ele in enumerate(paired):
        if ele in pairs:
            del paired[j]

    paired = ''.join(paired)
    paired = [paired[k] + paired[k+1] for k in range(0, len(paired)-1, 2)]

    pass_number += 1

paired = ''.join(paired)
with open('day5_otpt.txt', 'w') as f:
    f.write(paired)
