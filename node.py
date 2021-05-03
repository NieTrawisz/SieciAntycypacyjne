import numpy as np
class Node:
    def __init__(self,criterion:np.ndarray):
        self.criterion=criterion

    def getDecision(self,index):
        return self.criterion[index,:]

    def decisionCount(self):
        return self.criterion.shape[0]
