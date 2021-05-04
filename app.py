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

node0 = NodeFromFiles('dane/kryt_U1.csv','dane/pref.csv')
node1 = NodeFromFiles('dane/kryt_U2.csv','dane/pref.csv')
node2 = NodeFromFiles('dane/kryt_U3.csv','dane/pref.csv')
node3 = NodeFromFiles('dane/kryt_U4.csv','dane/pref.csv')

conn01 = read_matrix_from_file('dane/U0_U1.csv')
conn12 = read_matrix_from_file('dane/U1_U2.csv')
conn23 = read_matrix_from_file('dane/U2_U3.csv')

feed10 = read_matrix_from_file('dane/spr_zwrot.csv')[0]
feed21 = read_matrix_from_file('dane/spr_zwrot.csv')[1]
feed32 = read_matrix_from_file('dane/spr_zwrot.csv')[2]

an = AnticipatoryNetwork([node0, node1, node2, node3])
an.addConnection(node0, node1, conn01)
an.addConnection(node1, node2, conn12)
an.addConnection(node2, node3, conn23)
an.addFeedback(node1, node0, feed10)
an.addFeedback(node2, node1, feed21)
an.addFeedback(node3, node2, feed32)
an.CreateAdmissibleChains()
an.DisplayChains()
