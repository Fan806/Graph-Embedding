import sys
import os
import networkx as nx
import sys   
sys.setrecursionlimit(1000000)

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(FILE_DIR, '..'))
from utils.env import *
from utils.data_handler import DataHandler as dh
from shared_types import Node

def dfs(u, tree):
    print(u, tree[u].childst)
    if len(tree[u].childst) == 0:
        tree[u].coverst = set([u])
        return
    for v in tree[u].childst:
        print("-----------------------------------------")
        print(v)
        dfs(v, tree)
        print("END!")
        tree[u].coverst = tree[u].coverst | tree[v].coverst

def extract_hierarchy(G, params):
    g, n, m = dh.load_tree(os.path.join(DATA_PATH, params["file_path"]))
    tree = [None] * n
    print(n)
    print(len(g))
    # print(int[g])
    c = 0
    for u in g:
        tree[u] = Node(u, set(g[u].keys()), set())
        # print("parent:",u," child:",g[u].keys())
    # exit()
    dfs(n - 1, tree)
    return tree
