vis = [[0] * 16 + [1] for _ in range(8)] + [[1] * (16 + 1)]

# print(vis)


ver = [["|  "] * 16 + ['|'] for _ in range(8)] + [[]]

# print(ver)



hor = [["+--"] * 16 + ['+'] for _ in range(8 + 1)]

# print(hor)


d = [(16 - 1, 8), (16, 8 + 1), (16 + 1, 8), (16, 8 - 1)]
# shuffle(d)

# print(d)


for (xx, yy) in d:
    
    if xx == 16: 
        hor[max(8, yy)][16] = "+  "
    if yy == 8:
        ver[8][max(16, xx)] = "   "
    walk(xx, yy)