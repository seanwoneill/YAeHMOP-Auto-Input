##script to write 3D orthorhombic brillouin zone

f = open('brillouin.txt','w+')

start = 0
stop = 500
step = 50

# f.write('0 0 0 1\n')
for z in range(start, stop+step, step):
    for y in range(start, stop+step, step):
        for x in range (start, stop+step, step):
            f.write('{} {} {} 1\n'.format(x/1000, y/1000, z/1000))
f.close()