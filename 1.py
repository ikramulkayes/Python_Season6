#Task6
f = open("/content/input6_7.txt","r")
f_out = open("/content/output6_7.txt","w")
k = f.readline()
row,column = k.split()
row = int(row)
column = int(column)
#print(row,column)
word = f.readlines()
#print(word)
lst = []
for elm in word:
  lst.append(elm.rstrip("\n"))
#print(lst)
#print(lst[0][2])

#loop to travarse:
#pass


    



class DFS_main:
  def __init__(self):
    self.used_elm = []
    self.dimond = 0
  def DFS(self,graph,u,v,row,column): #row column
    if u < row and v < column and u >=0 and v >= 0:


        self.used_elm.append((u,v))
        #print(u,v)
        #print(self.used_elm)
        #print(graph[u])
        if graph[u][v] != "#":
          if graph[u][v]=="D":
            self.dimond += 1
          if (u-1,v) not in self.used_elm:
            self.DFS(graph,u-1,v,row,column)
          if (u+1,v) not in self.used_elm:
            self.DFS(graph,u+1,v,row,column)
          if (u,v-1) not in self.used_elm:
            self.DFS(graph,u,v-1,row,column)
          if (u,v+1) not in self.used_elm:
            self.DFS(graph,u,v+1,row,column)             
        






dimond = 0
for i in range(row):
  for j in range(column):
    g = DFS_main()
    g.DFS(lst,i,j,row,column)
    if g.dimond > dimond:
      dimond = g.dimond
print(dimond)

f_out.write(str(dimond))
f_out.close()

