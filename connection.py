from node import *
class Connection:
    def __init__(self,startNode,endNode,connections:np.ndarray):
        if startNode.decisionCount()!=connections.shape[0]:
            raise AttributeError("Dimension 1 of connections incorrect")
        if endNode.decisionCount()!=connections.shape[1]:
            raise AttributeError("Dimension 2 of connections incorrect")
        self.startNode=startNode
        self.endNode=endNode
        self.connections=connections

    def isConnected(self,decision1,decision2):
        return self.connections[decision1,decision2]==1
    
    