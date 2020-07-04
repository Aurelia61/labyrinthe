
# labyrinth_map_y = [""] * 10
# labyrinth_map_x = [""] * 20
# labyrinth_map = [""]

# for abs in range(20) :
#     labyrinth_map[abs] = labyrinth_map_y

# print(labyrinth_map)


# labyrinth_map = [["x_0 y0"],["x_0 y1"]],[["x_1 y1"],["x_1 y1"]]
# print(labyrinth_map)

# lab_y = [["y0"], ["y1"]]
# print(lab_y)

# lab_x = [["x_0"], ["x_1"]]
# print(lab_x)

# lab_x[0] = lab_y[0]
# lab_x[1] = lab_y[1]

# print (lab_x)


lab_x_0 = [[chr(69)], [chr(124)], ["°"]]    # en abs 0
lab_x_1 = [[chr(95)], [chr(95)], [chr(95)]]     # en abs 1

lab_map = [[lab_x_0], [lab_x_1]]

lab_map_print = ''.join(lab_map)
print (lab_map_print)

