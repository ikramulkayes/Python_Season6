"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    usednodes = []
    adj = {}
    head = None
    def cloneGraph(self,node):
        self.cloneGraph1(node)
        if Solution.head!= None:
            return Solution.head
    def cloneGraph1(self, node,head=None):
        #print(Solution.adj)
        if node != None :
            
            if node.val ==1 and head==None:
                #print("YO")
                head = Node(1)
                Solution.head = head
                
            else:
                pass
            if node.neighbors == None:
                pass
            else:
                if node not in Solution.usednodes:
                    Solution.usednodes.append(node)
                    if node.val not in Solution.adj.keys():
                        if head.neighbors == []:
                            newnode = head
                        else:
                            newnode = Node(node.val)
                        
                        Solution.adj[node.val] = newnode
                    else:
                        newnode = Solution.adj[node.val]
                    for elm in node.neighbors:
                        if elm.val in Solution.adj.keys():
                            newnode.neighbors.append(Solution.adj[elm.val])
                            self.cloneGraph1(elm,head)
                        else:
                            s = Node(elm.val)
                            Solution.adj[elm.val] = s
                            newnode.neighbors.append(Solution.adj[elm.val])
                            self.cloneGraph1(elm,head)
            print("YO")           
            for elm in Solution.adj[1].neighbors:
                print(elm.val)
                pass
            #return head