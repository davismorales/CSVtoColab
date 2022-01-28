import csv
import pandas as pd
from matplotlib import pyplot as plt

hunting = pd.read_csv('https://raw.githubusercontent.com/davismorales/graceproject/main/hunting.csv')
agriculture = pd.read_csv('https://raw.githubusercontent.com/davismorales/graceproject/main/agriculture.csv')
weight = pd.read_csv('https://raw.githubusercontent.com/davismorales/graceproject/main/weight.csv')

society = weight['society_xd_id'].tolist()
weightpoints = weight['code'].tolist()
value = [None]*34

huntingcheck = hunting['society_xd_id'].tolist()
agriculturecheck = agriculture['society_xd_id'].tolist()
huntingvalues = hunting['code'].tolist()
agriculturevalues = agriculture['code'].tolist()

sindex = 0
for sname in society:
    hindex = -1
    for hname in huntingcheck:
      hindex = hindex + 1
      if hname == sname:
        value[sindex] = 0 - huntingvalues[hindex]
        hindex = 0
        break
    sindex = sindex + 1

sindex = 0
for sname in society:
    aindex = -1
    for aname in agriculturecheck:
      aindex = aindex + 1
      if aname == sname:
        print(aname)
        value[sindex] = value[sindex] + agriculturevalues[aindex]
        aindex = 0
        break
    sindex = sindex + 1

plt.scatter(value, weightpoints)
plt.show()