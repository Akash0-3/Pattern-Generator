def pattern():
    for i in range(len(name)):
        # A
        if name[i] == "A":
            lis_a = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 4)):
                        lis_a[row][col] = "*"
            lis1.append(lis_a)
        # B
        elif name[i] == "B":
            lis_b = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0 or row == 0) and col != 4) or ((col == 4) and row != 0 and row != 5) or (row == 3) or ((row == 5) and col != 4):
                        lis_b[row][col] = "*"
            lis1.append(lis_b)

        # C
        elif name[i] == "C":
            lis_c = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0) and row != 0 and row != 5) or ((row == 0 or row == 5) and col != 0):
                        lis_c[row][col] = "*"
            lis1.append(lis_c)

        # D
        elif name[i] == "D":
            lis_d = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0) or ((col == 4) and row != 0 and row != 5) or (
                            (row == 0 or row == 5) and col != 0 and col != 4):
                        lis_d[row][col] = "*"
            lis1.append(lis_d)


        # E
        elif name[i] == "E":
            lis_e = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 or row == 0 or row == 5 or row == 3):
                        lis_e[row][col] = "*"
            lis1.append(lis_e)
        # F
        elif name[i] == "F":
            lis_f = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 or row == 0 or row == 3):
                        lis_f[row][col] = "*"
            lis1.append(lis_f)

        # G
        elif name[i] == "G":
            lis_g = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 or row == 0) or ((row == 5) and col != 4) or (
                            (col == 3) and row != 1 and row != 2) or ((col == 4) and row == 3) or (
                            (col == 2) and row == 3):
                        lis_g[row][col] = "*"
            lis1.append(lis_g)
        # H
        elif name[i] == "H":
            lis_h = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 or col == 4 or row == 3):
                        lis_h[row][col] = "*"
            lis1.append(lis_h)
        # I
        elif name[i] == "I":
            lis_i = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (row == 0 or row == 5 or col == 2):
                        lis_i[row][col] = "*"
            lis1.append(lis_i)
        # J
        elif name[i] == "J":
            lis_j = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 2 or row == 0) or ((row == 5) and col != 3 and col != 4):
                        lis_j[row][col] = "*"
            lis1.append(lis_j)
        # K
        elif name[i] == "K":
            lis_k = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0) or ((col == 1) and row == 2) or ((col == 2) and row == 1) or (
                            (col == 3) and row == 0) or ((col == 2) and row == 3) or ((col == 3) and row == 4) or (
                            (col == 4) and row == 5):
                        lis_k[row][col] = "*"
            lis1.append(lis_k)
        # L
        elif name[i] == "L":
            lis_l = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if col == 0 or row == 5:
                        lis_l[row][col] = "*"
            lis1.append(lis_l)
        # M
        elif name[i] == "M":
            lis_m = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 or col == 4) or ((col == 1) and row == 1) or ((col == 2) and row == 2) or (
                            (col == 3) and row == 1):
                        lis_m[row][col] = "*"
            lis1.append(lis_m)
        # N
        elif name[i] == "N":
            lis_n = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 or col == 4) or ((col == 1) and row == 1) or (
                            (col == 2) and row == 2 or ((col == 3) and row == 3)):
                        lis_n[row][col] = "*"
            lis1.append(lis_n)
        # O
        elif name[i] == "O":
            lis_o = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 and (row != 0 and row != 5)) or ((col == 4) and row != 0 and row != 5) or (
                            (row == 0) and col != 0 and col != 4) or ((row == 5) and col != 0 and col != 4):
                        lis_o[row][col] = "*"
            lis1.append(lis_o)
        # P
        elif name[i] == "P":
            lis_p = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0) or ((row == 0) and col != 4) or (
                            (col == 4) and row != 0 and row != 3 and row != 4 and row != 5) or (
                            (row == 3) and col != 4):
                        lis_p[row][col] = "*"
            lis1.append(lis_p)
        # Q
        elif name[i] == "Q":
            lis_q = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0 and (row != 0 and row != 5)) or ((col == 4) and row != 0) or (
                            (row == 0) and col != 0 and col != 4) or ((row == 5) and col != 0 and col != 4) or (
                            (col == 3) and row != 1 and row != 2 and row != 3) or (
                            (col == 2) and row != 1 and row != 2 and row != 4):
                        lis_q[row][col] = "*"
            lis1.append(lis_q)
        # R
        elif name[i] == "R":
            lis_r = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0) and row != 0) or ((row == 0) and col != 0 and col != 4) or (
                            (row == 2) and col != 4) or (
                            (col == 4) and row != 0 and row != 3 and row != 4 and row != 5) or (
                            (col == 2) and row == 4) or ((col == 1) and row == 3) or ((col == 3) and row == 5):
                        lis_r[row][col] = "*"
            lis1.append(lis_r)
        # S
        elif name[i] == "S":
            lis_s = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0) and row != 3 and row != 4) or (
                            (col == 1) and row != 1 and row != 2 and row != 4) or (
                            (col == 2) and row != 1 and row != 2 and row != 4) or (
                            (col == 3) and row != 1 and row != 2 and row != 4) or (
                            (col == 4) and row != 1 and row != 2):
                        lis_s[row][col] = "*"
            lis1.append(lis_s)
        # T
        elif name[i] == "T":
            lis_t = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 2 or row == 0):
                        lis_t[row][col] = "*"
            lis1.append(lis_t)
        # U
        elif name[i] == "U":
            lis_u = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0) and row != 5) or ((row == 5) and col != 0 and col != 4) or ((col == 4) and row != 5):
                        lis_u[row][col] = "*"
            lis1.append(lis_u)
        # V
        elif name[i] == "V":
            lis_v = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0) and row != 5 and row != 4) or (
                            (row == 5) and col != 0 and col != 4 and col != 3 and col != 1) or (
                            (col == 4) and row != 4 and row != 5) or (
                            (row == 4) and col != 0 and col != 2 and col != 4):
                        lis_v[row][col] = "*"
            lis1.append(lis_v)
        # W
        elif name[i] == "W":
            lis_w = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if (col == 0) or ((col == 1) and row != 0 and row != 1 and row != 2) or (
                            (col == 2) and row != 0 and row != 1 and row != 3 and row != 4 and row != 5) or (
                            (col == 3) and row != 0 and row != 1 and row != 2) or (col == 4):
                        lis_w[row][col] = "*"
            lis1.append(lis_w)
        # X
        elif name[i] == "X":
            lis_x = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 4)):
                        lis_x[row][col] = "*"
            lis1.append(lis_x)
        # Y
        elif name[i] == "Y":
            lis_y = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0) and row == 0) or ((col == 1) and row == 1) or (
                            (col == 2) and row != 0 and row != 1) or ((col == 3) and row == 1) or (
                            (col == 4) and row == 0):
                        lis_y[row][col] = "*"
            lis1.append(lis_y)
        # Z
        elif name[i] == "Z":
            lis_z = [[" " for i in range(7)] for j in range(7)]
            for row in range(6):
                for col in range(5):
                    if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col != 0 and col != 4)):
                        lis_z[row][col] = "*"
            lis1.append(lis_z)

        else:
            print("INVALID")

    return lis1


name = input("Enter the name:").upper()


lis1 = []
lis2 = pattern()

for i in range(7):
    for j in range(len(lis2)):
        for k in range(6):
            print(lis2[j][i][k], end=" ")
        print(end=" ")
    print()
