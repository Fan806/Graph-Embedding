import pandas as pd
import numpy as np

pf = pd.read_csv("edge.csv")
pf_node = pd.read_csv("node_list.csv")
# print(pf.columns)
pf.sort_values(pf.columns[0], inplace=True)
pf_node.sort_values(pf_node.columns[0], inplace=True)

key = pf_node.iloc[:,0].values.flatten().tolist()

value = np.arange(len(pf_node)).tolist()

valuezero = np.zeros(len(pf_node)).tolist()

dic = dict(zip(key, value))

emptydic = dict(zip(value, valuezero))

reverse_dic = dict(zip(value, key))

filename = "edges.txt"

f = open(filename, 'w')

data = pf.iloc[:,:2].values
s = pf.iloc[:,0].values.tolist()

f.write("%d\n" % len(pf_node))

# print(len(value))

for (source, target) in pf.iloc[:,:2].values:
	f.write("%d\t%d\n" % (dic[source], dic[target]))
	emptydic[dic[source]] = 1
	emptydic[dic[target]] = 1

for key in emptydic.keys():
	if emptydic[key] < 1:
		f.write("%d\n" % (key))

f.close()
