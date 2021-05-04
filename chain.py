from connection import *
class Chain:
    def __init__(self):
        self.nodes=[]
        self.decisions=[]

    def addDecision(self,node,decision):
        self.nodes.append(node)
        self.decisions.append(decision)

    def getDecisionValueAtNode(self,node)->float:
        index=self.nodes.index(node)
        return node.getDecisionValue(self.decisions[index])

    def createOptimalChain(self, startNode, endNode):
        decision_vals = []
        for i in range(startNode.criterion.shape):
            decision_vals.append(np.array([i,startNode.getDecisionValue(i)]))
        maxVal = np.max(decision_vals[:,0])
        
        