import numpy as np

# x = 0.0
# y = 0.0
# z = 0.5
#
# one = [x,y,z]
# two = [0.5-x, 0.5+y, 0.5+z]
# three = [x, 0.5-y, z]
# four = [0.5+x, y, 0.5-z]
# five = [-x, -y, -z]
# six = [0.5+x, 0.5-y, 0.5-z]
# seven = [-x, 0.5+y, -z]
# eight = [0.5-x, -y, 0.5+z]
#
# out = [one, two, three, four, five, six, seven, eight]
#
# lattice = [11.493, 4.152, 4.438]
# # lattice = [1,1,1]
#
# for i in range(len(out)):
#     for j in range(3):
#         out[i][j] = out[i][j]*lattice[j]
#     print(out[i])

a = 11.49417
b = 4.15096
c = 4.44175

xSn = 0.11849
ySn = 0.25
zSn = 0.10297
xSe = 0.85523
ySe = 0.25
zSe = 0.48204
# xSn = 0.118
# zSn = 0.103
# xSe = -0.145
# zSe = 0.479

# one = [x,y,z]
# two = [0.5-x, 0.5+y, 0.5+z]
# five = [-x, -y, -z]
# four = [0.5+x, y, 0.5-z]
# seven = [-x, 0.5+y, -z]
# three = [x, 0.5-y, z]
# six = [0.5+x, 0.5-y, 0.5-z]

# eight = [0.5-x, -y, 0.5+z]

u1 = [[xSn], [ySn], [zSn]] ## 1 Sn
u2 = [[0.5-xSn], [0.5+ySn], [0.5+zSn]] ## 3 Sn
u3 = [[1-xSn], [1-ySn], [1-zSn]] ##5 Sn
u4 = [[0.5+xSn], [ySn], [0.5-zSn]] ## 7 Sn
u5 = [[1-xSe], [0.5+ySe], [1-zSe]] ## 2 Se
u6 = [[1.5-xSe], [0.5+ySe], [0.5+zSe]] ## 4 Se
u7 = [[xSe], [0.5-ySe], [zSe]] ## 6 Se
u8 = [[-0.5+xSe], [0.5-ySe], [0.5-zSe]]## 8 Se

vects = [u1, u2, u3, u4, u5, u6, u7, u8]

for i in range(len(vects)):
    print(np.matrix([[a,0,0],[0, b, 0],[0, 0, c]])*vects[i])