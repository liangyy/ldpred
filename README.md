This repository is forked from https://github.com/bvilhjal/ldpred
It works on python3 instead of python2

# Test

```
# coordinate.py
ython ldpred/coord_genotypes.py --gf test_data/LDpred_cc_data_p0.001_train_0 --ssf test_data/LDpred_cc_data_p0.001_ss_0 --N 10000 --out test_data/LDpred_cc_data_p0.001_coord.hdf5

# LDpred.py
$ python ldpred/LDpred.py --coord=test_data/LDpred_cc_data_p0.001_coord.hdf5 --N=10000 --out=test_data/LDpred_cc_data_p0.001_ldpred --ld_radius=3
```
