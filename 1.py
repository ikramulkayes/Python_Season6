



    



class DFS_main:
  def __init__(self):
    self.used_elm = []
    #self.dimond = 0
  def DFS(self,graph,u,v,row,column): #row column
    if u < row and v < column and u >=0 and v >= 0:


        self.used_elm.append((u,v))
        #print(u,v)
        #print(self.used_elm)
        #print(graph[u])
        if graph[u][v] != "0":
          if (u-1,v) not in self.used_elm:
            self.DFS(graph,u-1,v,row,column)
          if (u+1,v) not in self.used_elm:
            self.DFS(graph,u+1,v,row,column)
          if (u,v-1) not in self.used_elm:
            self.DFS(graph,u,v-1,row,column)
          if (u,v+1) not in self.used_elm:
            self.DFS(graph,u,v+1,row,column)             
        

class Solution:
    def numIslands(self, grid):
      row = len(grid)
      column = len(grid[0])

          

      




      dimond = 0
      used_elm = []
      for i in range(row):
        for j in range(column):
          g = DFS_main()
          if (i,j) not in used_elm:
            g.DFS(grid,i,j,row,column)
            #print(g.used_elm)
            
            used_elm = used_elm + g.used_elm
            if grid[i][j] =="1":
              dimond += 1
            #print(used_elm)
      return dimond


k = Solution()
print(k.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))




