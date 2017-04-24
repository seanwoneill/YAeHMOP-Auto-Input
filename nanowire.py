import numpy as np

dia = 1000 # Angstroms; dia/10 = nm

a = 11.49417 ## x
b = 4.15096 ## y
c = 4.44175 ## z
lattice = {'x':11.49417, 'y':4.15096, 'z':4.44175}

dirIndex = {'x':0, 'y':1, 'z':2}
propagationDir = 'z'
directions = ['x','y','z']
directions.remove(propagationDir)
numCells = [round(dia/a), round(dia/b), round(dia/c)]
numCells.pop(dirIndex[propagationDir])
print(numCells)

unitcell = {'1 Sn':[1.3619442, 1.03774, 0.457367], '2 Se': [1.66401099, 3.11322, 2.30064883], \
            '3 Sn': [4.3851408, 3.11322, 2.678242], '4 Se': [7.41109599, 3.11322, 4.36197617],\
            '5 Sn': [10.1322258, 3.11322, 3.984383], '6 Se': [9.83015901, 1.03774, 2.14110117],\
            '7 Sn': [7.1090292, 1.03774, 1.763508], '8 Se': [4.08307401, 1.03774, 0.07977383]}

atoms = ['1 Sn', '2 Se', '3 Sn', '4 Se', '5 Sn', '6 Se', '7 Sn', '8 Se']

# unitcell = [[1.3619442, 1.03774, 0.457367],[1.66401099, 3.11322, 2.30064883], [4.3851408, 3.11322, 2.678242],\
#             [7.41109599, 3.11322, 4.36197617],[10.1322258, 3.11322, 3.984383], [9.83015901, 1.03774, 2.14110117],\
#             [7.1090292, 1.03774, 1.763508], [4.08307401, 1.03774, 0.07977383]]

f = open('nanowire disc {}nm.txt'.format(int(dia/10)),'w+')

index = 1
def nextRow(index, nCells, initCells, shft):
    """ index:  global index to number atom in YAeHMOP input file
        nCells:  integer of number of current cells to include in the current row of the nanowire cross section
        initCells: integer of the number of cells in the center row (= numCells[0])
        shft:  integer of current row"""
    grossCellShift = (initCells - nCells) / 2
    for cell in range(nCells):
        # f.write('; Unit cell {}\n'.format(int((index-1)/8)))
        for i in range(len(atoms)):
            #read in coordinate for current atom from unit cell
         atomCoords = unitcell[atoms[i]]
            #assign the corrdinate to x, y, z
         holder = {'x':atomCoords[0], 'y': atomCoords[1], 'z': atomCoords[2]}\
            #revise a given atomic corrdinate based on the current row (shft) and cell (cell)
         holder[directions[0]] = atomCoords[dirIndex[directions[0]]] + lattice[directions[0]]* (cell + grossCellShift)
         holder[directions[-1]] = atomCoords[dirIndex[directions[-1]]]+lattice[directions[-1]]*shft
            #set element type
         if index%2 == 0:
             elem = 'Se'
         else: elem = 'Sn'
         f.write('{} {} {} {} {}\n'.format(index, elem, holder['x'], holder['y'], holder['z']))
         index += 1
    return index

def degFree():
    return numCells[0] - \
           ((0.5*np.pi*round(numCells[-1]/2))/(np.arccos((0.1*dia)/(lattice[directions[0]]*numCells[0]))))

def fudge():
    return 0.1*dia/(lattice[directions[0]]*numCells[0]*np.cos(0.5*np.pi*round(numCells[-1]/2)/(numCells[-1])))

DoF = 1
fud = fudge()
print(fud)
## Writing cells in positive y region
for shift in range(round(numCells[-1]/2)):
    adjNumCells = int(fud*round(numCells[0] * np.cos((0.5*np.pi) / (numCells[-1]-DoF) * shift)))
    index = nextRow(index, adjNumCells, numCells[0], shift)

## Writing cells in negative y region
if numCells[-1]%2 == 0:
    # #if even no. of rows, move everything down -1 rows to duplicate 0th row in neg. hemisphere
    for shift in range(round(numCells[-1] / 2)):
        adjNumCells = int(fud*round(numCells[0]*np.cos((0.5*np.pi)/(numCells[-1]-DoF)*shift)))
        index = nextRow(index, adjNumCells, numCells[0], -(1+shift))
else:
    # #if odd no. of rows, start at shift = 1 to not duplicate 0th row
    for shift in range(1,round(numCells[-1] / 2)):
        adjNumCells = int(fud*round(numCells[0] * np.cos((0.5*np.pi) / (numCells[-1]-DoF) * shift)))
        index = nextRow(index, adjNumCells, numCells[0], -1*shift)

print('<< check >>')
print('\tindex: ', (index-1)/8)
print('\tarea ratio: {}'.format((0.25*np.pi*dia**2)/(lattice[directions[0]]*lattice[directions[1]])))

f.close()
