



    
#Leet code: Number of island


class DFS_main:
  def __init__(self,graph):
    #self.used_elm = []
    #self.dimond = 0
    self.graph = graph
  def DFS(self,u,v,row,column): #row column
    if u < row and v < column and u >=0 and v >= 0:


        #self.used_elm.append((u,v))
        #self.graph[u][v]
        #print(u,v)
        #print(self.used_elm)
        #print(graph[u])
        if self.graph[u][v] != "0" and self.graph[u][v] != "2":
          self.graph[u][v] = "2"
          if u-1 >= 0:
            if self.graph[u-1][v] != "2":
                self.DFS(u-1,v,row,column)
          if u+1 < row:
            if self.graph[u+1][v] != "2":
                self.DFS(u+1,v,row,column)
          if v-1 >=0:
            if self.graph[u][v-1] != "2":
              self.DFS(u,v-1,row,column)
          if v+1 <column:
            if self.graph[u][v+1] != "2":
              self.DFS(u,v+1,row,column)             
        

class Solution:
    def numIslands(self, grid):
      row = len(grid)
      column = len(grid[0])

          

      




      dimond = 0
      #used_elm = []
      for i in range(row):
        for j in range(column):
          g = DFS_main(grid)
          grid = g.graph

          if grid[i][j] != "2":
            g.DFS(i,j,row,column)
            #print(g.used_elm)
            #print(grid)
            #used_elm = used_elm + g.used_elm
            if grid[i][j] =="2":
              dimond += 1
            #print(used_elm)
      return dimond


k = Solution()
print(k.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))




