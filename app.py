from anticipatoryNetwork import *
# node1=Node(np.array([[5,1,2],[3,2,1],[4,5,6]]),np.array([0.2,0.5,0.3]))
# print(node1.getDecision(0))
# print(node1.getDecisionValue(0))
# print(node1.decisionCount())

# node2=Node(np.array([[5,1,2],[3,2,1],[4,5,6],[1,1,1]]),np.array([0.2,0.5,0.3]))
# print(node2.decisionCount())

# an=AnticipatoryNetwork([node1,node2])
# connections=np.random.rand(3,4)>=0.5
# an.addConnection(node1,node2,connections)
# an.addFeedback(node1,node2,[1,2])
# print(an.getNodesIdsConnectedWithThisOne(node1)[0]==node2)
# an.CreateAdmissibleChains()
# an.DisplayChains()


# con=Connection(node1,node2,connections)
# print(con.isConnected(0,0))

# con.startNode.criterion[0,0]=1
# print(node1.getDecision(0))


node0 = Node(np.array([[3, 1, 3], [5, 2, 2], [5, 4, 5], [3, 5, 4], [
             3, 4, 3], [5, 3, 5], [4, 5, 3]]), np.array([0.3, 0.2, 0.5]))
node1 = Node(np.array([[4, 3, 2], [3, 3, 2], [4, 1, 5], [3, 3, 4], [2, 2, 2], [
             4, 5, 1], [1, 4, 5], [3, 3, 1], [5, 5, 1]]), np.array([0.3, 0.2, 0.5]))

an = AnticipatoryNetwork([node0, node1])
connections = np.array([[1, 0, 1, 1, 0, 0, 0, 1, 0], 
                [1, 0, 1, 0, 1, 0, 0, 1, 0], 
                [1, 1, 1, 0, 0, 0, 0, 0, 1], 
                [1, 0, 1, 0, 1, 0, 1, 0, 0], 
                [1, 0, 1, 1, 1, 1, 0, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 0, 1], 
                [1, 1, 0, 1, 0, 0, 1, 1, 1]])
an.addConnection(node0, node1, connections)
an.addFeedback(node1, node0, [1,2,3,4,5])
# an.CreateAdmissibleChains()
# an.DisplayChains()
a = np.array([[1,2,3],[4,5,6]])
print(np.max(a[:,0]))