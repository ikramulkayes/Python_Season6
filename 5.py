
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    usednodes = []
    adj = {}
    head = None
    def cloneGraph(self,node):
        self.DFS(node)
        return Solution.head
    def DFS(self,node,head=None):
        if node != None:
            if head == None:
                head = Node(node.val)
                Solution.head = head
                Solution.adj[node.val] = head
            for elm in node.neighbors:
                if elm.val in Solution.adj.keys():
                    
                    head.neighbors.append(Solution.adj[elm.val])
                else:
                    newnode = Node(elm.val)
                    Solution.adj[elm.val] = newnode
                    head.neighbors.append(newnode)
                    self.DFS(elm,newnode)

