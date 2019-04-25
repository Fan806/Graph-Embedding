# -*- coding=utf-8 -*-
from sklearn.manifold import SpectralEmbedding
from sklearn.cluster import KMeans, AgglomerativeClustering, MiniBatchKMeans
import pandas as pd
import numpy as np

pf_node = pd.read_csv("node_list.csv", encoding="gb18030")
pf_edge = pd.read_csv("edge.csv")


pf_edge.sort_values(pf_edge.columns[0], inplace=True)
pf_node.sort_values(pf_node.columns[0], inplace=True)

ID = pf_node.iloc[:,0].values.flatten().tolist()

department = pf_node.iloc[:, 5].tolist()

id2number = dict(zip(ID, np.arange(len(pf_node)).tolist()))

number2id = dict(zip(np.arange(len(pf_node)).tolist(), ID))

id2department = dict(zip(ID, department))

graph = np.zeros((len(pf_node), len(pf_node)))

for row in range(len(pf_edge)):
	source = pf_edge.iloc[row, 0]
	target = pf_edge.iloc[row, 1]
	weight = pf_edge.iloc[row, 6]
	n1 = id2number[source]
	n2 = id2number[target]
	
	graph[n1][n2] = weight
	graph[n2][n1] = weight
	
embedding = SpectralEmbedding(n_components=100)
embeddedGraph = embedding.fit_transform(graph[:])

#---------------------kmeans-----------------------
kmeans = KMeans(n_clusters=50).fit(embeddedGraph)
print("KMeans...")
filename1 = "Kmeans.txt"
f1 = open(filename1,'w')
for i in range(len(kmeans.labels_)):
	i_ID = number2id[i]
	i_department = id2department[i_ID]
	f1.write("id: %d category: %d department: %s\n" % (number2id[i], kmeans.labels_[i], i_department))
	# print("id: ", number2id[i], " category: ", kmeans.labels_[i], " department:", i_department)
f1.close()

#---------------------AgglomerativeClustering-----------------
agglomerative = AgglomerativeClustering(n_clusters=50).fit(embeddedGraph)
print("agglomerative...")
filename2 = "Agglomerative.txt"
f2 = open(filename2,'w')
for i in range(len(agglomerative.labels_)):
	i_ID = number2id[i]
	i_department = id2department[i_ID]
	f2.write("id: %d category: %d department: %s\n" % (number2id[i], kmeans.labels_[i], i_department))

f2.close()	

#--------------------MiniBatchKmeans-------------------
minibatch = MiniBatchKMeans(n_clusters=50).fit(embeddedGraph)
print("MiniBatchKmeans...")
filename3 = "MiniBatchKmeans.txt"
f3 = open(filename3,'w')
for i in range(len(agglomerative.labels_)):
	i_ID = number2id[i]
	i_department = id2department[i_ID]
	f3.write("id: %d category: %d department: %s\n" % (number2id[i], kmeans.labels_[i], i_department))

f3.close()	

