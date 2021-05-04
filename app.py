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

node0 = NodeFromFiles('dane/kryt_U0.csv', 'dane/pref.csv', 0)
node1 = NodeFromFiles('dane/kryt_U1.csv', 'dane/pref.csv', 1)
node3 = NodeFromFiles('dane/kryt_U3.csv', 'dane/pref.csv', 3)
node5 = NodeFromFiles('dane/kryt_U5.csv', 'dane/pref.csv', 5)

conn01 = read_matrix_from_file('dane/U0_U1.csv')
conn13 = read_matrix_from_file('dane/U1_U3.csv')
conn35 = read_matrix_from_file('dane/U3_U5.csv')

feed10 = read_matrix_from_file('dane/spr_zwrot.csv')[0]
feed31 = read_matrix_from_file('dane/spr_zwrot.csv')[1]
feed53 = read_matrix_from_file('dane/spr_zwrot.csv')[2]

an = AnticipatoryNetwork([node0, node1, node3, node5])
an.addConnection(node0, node1, conn01)
an.addConnection(node1, node3, conn13)
an.addConnection(node3, node5, conn35)
an.addFeedback(node1, node0, feed10)
an.addFeedback(node3, node1, feed31)
an.addFeedback(node5, node3, feed53)
an.CreateAdmissibleChains()
an.DisplayChains()
