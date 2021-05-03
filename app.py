from connection import *
node1=Node(np.array([[5,1,2],[3,2,1],[4,5,6]]))
print(node1.getDecision(0))
print(node1.decisionCount())

node2=Node(np.array([[5,1,2],[3,2,1],[4,5,6],[1,1,1]]))
print(node2.decisionCount())
connections=np.random.rand(3,4)>=0.5
con=Connection(node1,node2,connections)
print(con.isConnected(0,0))

con.startNode.criterion[0,0]=1
print(node1.getDecision(0))