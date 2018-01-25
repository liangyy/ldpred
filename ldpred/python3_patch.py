import numpy as np
def read_decode_hdf5(group):
    out = {}
    known = ['infos', 'nts', 'sids']
    print('wherdsadasd')
    print(list(group.keys()))
    for i in list(group.keys()):
        out[i] = {}
        for j in list(group[i].keys()):
            if j in known:
                out[i][j] =  [ m.decode('utf-8') for m in group[i][j][...] ]
            else:
                out[i][j] = group[i][j]
    return out
