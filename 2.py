



    



class DFS_main:
  def __init__(self):
    self.used_elm = []
    #self.dimond = 0
    self.not_one = []
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
        else:
            self.not_one.append((u,v))       
        

class Solution:
    def numIslands(self, grid):
      self.grid = grid
      self.row = len(grid)
      self.column = len(grid[0])

          

      




      self.dimond = 0
      self.used_elm = []
      self.func(0,0)
      return self.dimond
    def func(self,i,j):
          g = DFS_main()
          
          if (i,j) not in self.used_elm:
            g.DFS(self.grid,i,j,self.row,self.column)
            
            
            self.used_elm = self.used_elm + g.used_elm
            if self.grid[i][j] =="1" and len(g.used_elm) >=1:
              self.dimond += 1
              #print(g.used_elm)
            for elm in g.not_one:
               if elm[0]+1 <self.row and elm[1] < self.column:
                  self.func(elm[0]+1,elm[1])
               if elm[0] <self.row and elm[1]+1 < self.column:
                  self.func(elm[0],elm[1]+1)
               if elm[0]-1 <self.row and elm[1] < self.column:
                  self.func(elm[0]-1,elm[1])
               if elm[0] <self.row and elm[1]-1 < self.column:
                  self.func(elm[0],elm[1]-1)                          
      


k = Solution()
print(k.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))




