import numpy as np


def get_well_id(Designs, drug, concentration):
    try:
        arr = Designs[drug].values
    except KeyError:
        print "queried drug not in plate"
    ind = np.where(arr == concentration)
    wells = []
    if len(ind[0]) > 0:
        for i in range(len(ind[0])):
            pos = '%s%s' % (chr(65+ind[0][i]), ind[1][i]+1)
            wells.append(pos)
    return wells


def wellid2index(id, plate_dims):

    row_num = ord(id[0]) - 65
    col_num = int(id[1:]) - 1
    ind = row_num*plate_dims[1] + col_num
    return ind