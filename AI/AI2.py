"""
Project 1
Tile Game
Graph-Search Algorithm using A* SEARCH
By- Asim Satti
"""

import sys

class tree:
    class node:
        def __init__(self,data = None):
            self.level = None
            self.cost = 0
            self.path= None
          
            self.left = None
            self.up = None
            self.right = None
            self.down = None
            self.table = data

        def getIncorrect(self):
            wrong = []
            num = 0
            y_pos = 0
            x_pos = 0
      
            
          
            for i in range(len(self.table)):
                if(self.table[i] != self.goal[i]):
                         g_pos = self.goal.index(self.table[i])
                   
                         if((g_pos//3) != i//3):
                             y_pos = abs(g_pos//3 - i//3)
                         else:
                            y_pos = 0
                         if((g_pos%3) !=  i%3):
                            x_pos = abs(g_pos%3 - i%3)
                         else:
                            x_pos = 0
                else:
                    x_pos=0
                    y_pos=0
                wronger = y_pos + x_pos
                
                num+=wronger

 
            return num
                         
                


         
    def __init__(self, inital,final):
        self.root = None
        self.size = 0
        self.init = inital
        self.goal = final
        self.current = None
        self.visits = 0
        self.visited = []
        self.directions = []
        self.queued = []


    def start(self):
        #Start of algorithm set roo
        
        depth = 0
        self.root = self.newNode()
        self.current = self.root

        #Until current table is not the goal table
        while(self.current.table != self.goal ):
            #keep searching until movment
            self.search()
            depth+=1
            print('size: ',self.size,'depth', depth,self.current.table,"  ", self.goal)
                     
    def search(self):
        #Searchs table finds the blank's position
        zero_pos = -1
         
        for i in range(len(self.current.table)):
            if(int(self.current.table[i]) == 0):
                     zero_pos = i

         
        #Tries to create children
        self.Left(zero_pos)
        self.Up(zero_pos)
        self.Right(zero_pos)
        self.Down(zero_pos)


        #Calculate cheapest cost, prepare to move
        self.calculateCheapestChild()
        
                     

    def Left(self,space):
        #Left Column indexes out
        
        if(space != 0 and space != 3 and space != 6):
            self.current.left = self.newNode()
            
            self.current.left.table[space] = self.current.left.table[space-1]
          
            self.current.left.table[space - 1] = '0'

            
        
        else:
            self.current.left = None

    def Up(self,space):
        #Top row indexes out
        
        if(space != 0 and space != 1 and space != 2 ):
            self.current.up = self.newNode()
            self.current.up.table[space] = self.current.up.table[space -3]
            self.current.up.table[space -3] = '0'
         
        else:
            self.current.up = None

    def Right(self,space):
        #Right Column indexes out
        if(space != 2 and space != 5 and space != 8 ):
            self.current.right = self.newNode()
            self.current.right.table[space] = self.current.right.table[space+1]
            self.current.right.table[space +1 ] = '0'
         
                     
        else:
            self.current.right = None
                     
    def Down (self,space):
        if(space!=6 and space !=7 and space !=8 ):
            self.current.down = self.newNode()
            self.current.down.table[space] = self.current.down.table[space+3]
            self.current.down.table[space+3] = '0'
      
        else:
            self.current.down = None
        
 
        
    def newNode(self, inital = None,theGoal = None):
        #Creates children node
        #Increments level
        #Takes goal from root as they are the same
        
        newNode = self.node()
        if(self.size == 0):
            newNode.goal = theGoal
            newNode.level = 0
            newNode.table = self.init
            self.size+=1
            self.visited.append(self.init)
        else:        
            newNode.level = self.current.level+1
            newNode.goal = self.goal
            newNode.table = self.current.table.copy()
            
        return newNode

    
 

    def getDirection(self,direction):
        #Adds Directions Traversed
        #Updates current
 
       
        if(direction == 0):
            self.directions.append("L")
            self.current = self.current.left
            print('going left')
        elif(direction == 1):
            self.directions.append("U")
            self.current = self.current.up
            print('going up')
        elif(direction == 2):
            self.directions.append("R")
            self.current = self.current.right
            print('going right')
        elif(direction == 3):
            self.directions.append("D")
            self.current = self.current.down
            print('going down')
    
    
        
    def calculateCheapestChild(self):
        #Calculates Manhattan Distance by
        #*Adding all children to array
        #*Calculating thself.queued.append(self.current.left)e cost and position keeps track of LURD
        
        manhattanDistanceCosts = []
        if(self.current.left is not None and self.current.left.table not in self.visited):
 
            wrong = self.current.left.level + self.current.left.getIncorrect()
            self.current.left.cost = wrong
            self.current.left.path ='L'
            self.queued.append(self.current.left)
            self.visited.append(self.current.left.table)
            manhattanDistanceCosts.append(wrong)
            self.size+=1

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        if(self.current.up is not None and self.current.up.table not in self.visited):
            wrong = self.current.up.level + self.current.up.getIncorrect()
            self.current.up.path = "U"
            self.current.up.cost = wrong
            self.queued.append(self.current.up)
            self.visited.append(self.current.up.table)
            manhattanDistanceCosts.append(wrong)
            self.size+=1

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        if(self.current.right is not None and self.current.right.table not in self.visited):
            wrong = self.current.right.level + self.current.right.getIncorrect()
            self.current.right.cost = wrong
            self.current.right.path = "R"
            self.queued.append(self.current.right)
            self.visited.append(self.current.right.table)
            manhattanDistanceCosts.append(wrong)
            self.size+=1

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        if(self.current.down is not None and self.current.down.table not in self.visited):
            wrong = self.current.down.level + self.current.down.getIncorrect()
            self.current.down.cost = wrong
            self.current.down.path = "D"
            self.queued.append(self.current.down)
            self.visited.append(self.current.down.table)
            manhattanDistanceCosts.append(wrong)
            self.size+=1

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        
       
        #Each keeps track of which child then cheapest
        
        cheapest = min(manhattanDistanceCosts)
        cheap = -1
        swap = True
##        for i in range(len(self.queued)):
##            if(self.queued[i].cost<cheapest and swap ):
##                cheap = i 
##                swap = False
##        if(swap==False):
##        
##            self.current = self.queued[cheap]
##            self.directions.append(self.current.path)
##        else:
        print(manhattanDistanceCosts)
        path = manhattanDistanceCosts.index(cheapest)
        self.getDirection(path)
                    
             


def Read(file):
  
    fp = open(file, 'r')
    init = []
    temp = []
    final = []
    with open(file):
        num=0
        for line in fp.readlines():
            for char in line:
                
                if(ord(char)!=32 and ord(char) != 10):
                    init.append(char)
               
        
     
        final = init[9:]
        init = init[:9]


        return init,final
            


if __name__ == "__main__":
   
    #File_name  inital state
    file_name = input("Enter file path: ")
    
    # Goal state
    solved_file = file_name+"_solved"
   
    init,final = Read(file_name)

    #Call Graph search taking in inital and final stages
    GSA = tree(init,final)
    GSA.start()
