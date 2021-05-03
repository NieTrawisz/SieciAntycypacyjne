import numpy as np
class Node:
    ids=0
    def __init__(self,criterion:np.ndarray,preference:np.ndarray):
        self.criterion=criterion
        self.preference=preference
        self.id=Node.ids
        Node.ids+=1

    def getDecision(self,index)->np.ndarray:
        return self.criterion[index,:]

    def getDecisionValue(self,index)->float:
        return self.getDecision(index)@self.preference.T

    def decisionCount(self):
        return self.criterion.shape[0]
