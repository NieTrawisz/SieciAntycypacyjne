from anticipatoryNetwork import *
node1=Node(np.array([[5,1,2],[3,2,1],[4,5,6]]),np.array([0.2,0.5,0.3]))
print(node1.getDecision(0))
print(node1.getDecisionValue(0))
print(node1.decisionCount())

node2=Node(np.array([[5,1,2],[3,2,1],[4,5,6],[1,1,1]]),np.array([0.2,0.5,0.3]))
print(node2.decisionCount())

an=AnticipatoryNetwork([node1,node2])
connections=np.random.rand(3,4)>=0.5
an.addConnection(node1,node2,connections)
an.addFeedback(node1,node2,[1,2])
print(an.getNodesIdsConnectedWithThisOne(node1)[0]==node2)
an.CreateAdmissibleChains()
an.DisplayChains()

#con=Connection(node1,node2,connections)
#print(con.isConnected(0,0))

#con.startNode.criterion[0,0]=1
#print(node1.getDecision(0))