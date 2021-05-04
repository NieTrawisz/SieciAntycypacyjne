from chain import *
from feedback import *
from data_excel import *


class AnticipatoryNetwork:
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.connections = []
        self.feedbacks = []

    def addConnection(self, startNode, endNode, connections: np.ndarray):
        self.connections.append(Connection(startNode, endNode, connections))

    def addFeedback(self, startNode, endNode, acceptedDecisions: list):
        self.feedbacks.append(Feedback(startNode, endNode, acceptedDecisions))

    def CreateAdmissibleChains(self):
        self.chains = []
        for i in range(self.nodes[0].decisionCount()):
            c = Chain()
            c.addDecision(self.nodes[0], i)
            self.chains.append(c)
        for con in self.connections:
            if con.endNode in self.nodes and con.startNode in self.nodes:
                for chain in self.chains:
                    if chain.nodes[-1] == con.startNode:
                        allConnected = con.getAllConnectedDecisions(
                            chain.decisions[-1])
                        if len(allConnected) > 0:
                            chaincopy = Chain()
                            for i in range(len(chain.nodes)):
                                chaincopy.addDecision(
                                    chain.nodes[i], chain.decisions[i])
                            chain.addDecision(con.endNode, allConnected[0])
                            for i in range(1, len(allConnected)):
                                copy = Chain()
                                for j in range(len(chaincopy.nodes)):
                                    copy.addDecision(
                                        chaincopy.nodes[j], chaincopy.decisions[j])
                                copy.addDecision(con.endNode, allConnected[i])
                                self.chains.append(copy)
        reversed = self.nodes[:]
        reversed.reverse()
        for node in reversed:
            self.chains.sort(
                key=(lambda chain: chain.getDecisionValueAtNode(node)))

    def getAllNodesChain(self) -> list:
        return self.getAllNodesChainStartingAt(self.nodes[0])

    def getAllNodesChainStartingAt(self, startNode):
        nextnodes = self.getNodesIdsConnectedWithThisOne(startNode)
        if len(nextnodes) == 0:
            return [[startNode]]
        nodesChain = []
        for node in nextnodes:
            paths = self.getAllNodesChainStartingAt(node)
            for path in paths:
                nodesChain.append([startNode]+path)
        return nodesChain

    def findAllFeedbacksTargetNodes(self) -> list:
        targetNodes = set()
        for feed in self.feedbacks:
            targetNodes.add(feed.endNode)
        targetSorted = []
        for node in self.nodes:
            if node in targetNodes:
                targetSorted.append(node)
        targetSorted.reverse()
        return targetSorted

    def FindAllFeedbacksSourceNodesForCertainNode(self, endNode) -> list:
        targetNodes = set()
        for feed in self.feedbacks:
            if feed.endNode == endNode and feed.startNode in self.nodes:
                targetNodes.add(feed.startNode)
        targetSorted = []
        for node in self.nodes:
            if node in targetNodes:
                targetSorted.append(node)
        targetSorted.reverse()
        return targetSorted

    def getNodesIdsConnectedWithThisOne(self, node) -> list:
        nodesConnected = set()
        for con in self.connections:
            if con.startNode == node:
                nodesConnected.add(con.endNode)
        return list(nodesConnected)

    def DisplayChains(self):
        for chain in self.chains:
            for i in range(len(chain.nodes)-1):
                print("U%i,%i" %
                      (chain.nodes[i].id, chain.decisions[i]+1), end=' -> ')
            print("U%i,%i" % (chain.nodes[-1].id, chain.decisions[-1]+1))

    def GetAdmissiblePathsBetweenNodeAndElementV(self, startNode, endNode, endDecision):
        paths = []
        for chain in self.chains:
            index = chain.nodes.index(endNode)
            if chain.decisions[index] == endDecision:
                chaincopy = Chain()
                for i in range(len(chain.nodes)):
                    chaincopy.addDecision(chain.nodes[i], chain.decisions[i])
                start = chaincopy.nodes.index(startNode)
                chaincopy.decisions[0:start-1] = -1
                chaincopy.decisions[endNode+1:] = -1
                new = True
                for path in paths:
                    if path.decisions == chaincopy.decisions:
                        new = False
                if new:
                    paths.append(chaincopy)
        return paths

    def GetFeedbackFulfillingChains(self):
        self.CreateAdmissibleChains()
        newChains = []
        for chain in self.chains:
            for i in range(len(chain.nodes)):
                for feed in self.feedbacks:
                    if chain.nodes[i] is feed.endNode and chain.decisions[i] in feed.acceptedDecisions:
                        newChains.append(chain)
        self.chains = newChains

    def FindOptimalPath(self):
        optimalChain = 0
        opt_sum = 0
        for chain in self.chains:
            summ = 0
            for node in chain.nodes:
                summ += chain.getDecisionValueAtNode(node)
            if summ > opt_sum:
                opt_sum = summ
                optimalChain = chain
        return optimalChain

    def GetSumofTwoSetsOfChains(self,chainsA,chainsB):
        firstA=chainsA[0].nodes
        firstB=chainsB[0].nodes
        newChains=[]
        for chainA in chainsA:
            for chainB in chainsB:
                newChain=Chain()
                if len(chainA.nodes)!=len(chainB.nodes):
                    raise Exception("Invalid sets of chains")
                goodToAdd=True
                for k in range(len(chainA.nodes)):
                    if firstA[k]==-1:
                        if firstB[k]==-1:
                            newChain.addDecision(chainA.nodes[k],-1)
                        else:
                            newChain.addDecision(chainA.nodes[k],chainB.decision[k])
                    else:
                        if firstB[k]==-1:
                            newChain.addDecision(chainA.nodes[k],chainA.decision[k])
                        else:
                            if firstA[k]==firstB[k]:
                                newChain.addDecision(chainA.nodes[k],chainA.decision[k])
                            else:
                                goodToAdd=False
                                break
                if goodToAdd:
                    for chain in newChains:
                        if chain.decisions==newChain.decisions:
                            goodToAdd=False
                    if goodToAdd:
                        newChains.append(newChain)
        return newChains
        

                
                    
                        
                            
                
