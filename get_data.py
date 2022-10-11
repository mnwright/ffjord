
import numpy as np
import datasets

# bsds300
dat = datasets.BDS300()

np.savetxt('data_export/bsds300_trn.csv', dat.trn.x, delimiter=",")
np.savetxt('data_export/bsds300_tst.csv', dat.tst.x, delimiter=",")
np.savetxt('data_export/bsds300_val.csv', dat.val.x, delimiter=",")

# gas
dat = datasets.GAS()

np.savetxt('data_export/gas_trn.csv', dat.trn.x, delimiter=",")
np.savetxt('data_export/gas_tst.csv', dat.tst.x, delimiter=",")
np.savetxt('data_export/gas_val.csv', dat.val.x, delimiter=",")

# hepmass
dat = datasets.HEPMASS()

np.savetxt('data_export/hepmass_trn.csv', dat.trn.x, delimiter=",")
np.savetxt('data_export/hepmass_tst.csv', dat.tst.x, delimiter=",")
np.savetxt('data_export/hepmass_val.csv', dat.val.x, delimiter=",")

# Miniboone
dat = datasets.MINIBOONE()

np.savetxt('data_export/miniboone_trn.csv', dat.trn.x, delimiter=",")
np.savetxt('data_export/miniboone_tst.csv', dat.tst.x, delimiter=",")
np.savetxt('data_export/miniboone_val.csv', dat.val.x, delimiter=",")

# power
dat = datasets.POWER()

np.savetxt('data_export/power_trn.csv', dat.trn.x, delimiter=",")
np.savetxt('data_export/power_tst.csv', dat.tst.x, delimiter=",")
np.savetxt('data_export/power_val.csv', dat.val.x, delimiter=",")