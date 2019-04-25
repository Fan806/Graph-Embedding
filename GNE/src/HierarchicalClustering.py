import pandas as pd
import scipy
import scipy.cluster.hierarchy as hcluster
import sklearn as sk
from sklearn import cluster
import itertools
import numpy as np
import csv

pf_node = pd.read_csv("node_list.csv")
pf_edge = pd.read_csv("edge.csv")

pf_node.sort_values(pf_node.columns[0],inplace=True)

n = len(pf_node)

max_node = pf_node.iloc[-1,0]

groundTruth = pf_node["department"].values

label = set(groundTruth)

AdjMatrix = np.zeros((n,n))
# print(AdjMatrix)

key = pf_node.iloc[:,:1].values.flatten().tolist()
value = np.arange(n).tolist()
dic = dict(zip(key, value))
dic_ground_truth = dict(zip(range(len(label)), list(label)))
reverse_dic = dict(zip(value, key))

print(n)
# print(dic)
for i in range(n):
	s = pf_edge.iloc[i, 0]
	t = pf_edge.iloc[i, 1]
	w = pf_edge.iloc[i, 6]

	if s in dic.keys():
		AdjMatrix[dic[s]][dic[t]] = w
		AdjMatrix[dic[t]][dic[s]] = w

clst = cluster.AgglomerativeClustering(len(groundTruth), affinity='euclidean', memory=None, compute_full_tree=True, linkage='ward')
clst.fit(AdjMatrix)

with open('result.csv','w',newline='') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(["node","label"])
	for i in len(clst.labels_):
		li = [reverse_dic[i]]
		li.append(dic_ground_truth[clst.labels_[i]])
		csv_writer.writerow(li)


# filename = "tree.txt"
# f = open(filename, 'w')

# children = clst.children_

# f.write("%d\t%d\n" % (n*2-1, n))

# for i in range(len(children)):
# 	#left child
# 	f.write("%d\t%d\n" % (i+n, children[i][0]))

# 	# if(children[i][0] >= n):
# 	# 	f.write("%d\t%d\n" % (i+n, children[i][0]+max_node+1))
# 	# else:
# 	# 	f.write("%d\t%d\n" % (i+n, reverse_dic[children[i][0]]))

# 	#right child
# 	f.write("%d\t%d\n" % (i+n, children[i][1]))

# 	# if(children[i][1] >= n):
# 	# 	f.write("%d\t%d\n" % (i+max_node+1, children[i][1]+max_node+1))
# 	# else:
# 	# 	f.write("%d\t%d\n" % (i+max_node+1, reverse_dic[children[i][1]]))

# f.close()

