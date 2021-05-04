from node import *
from connection import *
import pandas as pd

def read_matrix_from_file(filename):
    return pd.read_csv(filename, sep=".", delimiter=";", header=None).to_numpy()

import numpy as np
class NodeFromFiles:
    def __init__(self,filename_criterion:str,filename_preference:str, node_num:int):
        self.criterion=read_matrix_from_file(filename_criterion)
        self.preference=read_matrix_from_file(filename_preference)[node_num]
        self.id=node_num

    def getDecision(self,index)->np.ndarray:
        return self.criterion[index,:]

    def getDecisionValue(self,index)->float:
        return self.getDecision(index)@self.preference.T

    def decisionCount(self):
        return self.criterion.shape[0]
    
#node1 = NodeFromFiles(CSVX, CSVY)
#node2 = NodeFromFiles(...)
#an=AnticipatoryNetwork([node1,node2])
#connections= read_matrix_from_file(CSV_CONN)
#an.addConnection(node1,node2,connections)
#decisions = read_matrix_from_file(CSV_DECISIONS)
#an.addFeedback(node1,node2,decisions)
#print(an.getNodesIdsConnectedWithThisOne(node1)[0]==node2)
#an.CreateAdmissibleChains()
#an.DisplayChains()
        
