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
            self.parent = None
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
        self.depth = 0
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
            print(self.current.table)
            self.depth+=1
          #  print('size: ',self.size,'depth', depth,self.current.table,"  ", self.goal)
        self.printer()


           
    def printer(self):
        count = 0
        move_once= True
        move_twice =True
        move_third = True
        move_fourth = True
        

        for i in range(len(self.init)):
            row = i//3
            if(row==0):
                print(self.init[i],end=" ")
            elif(row==1):
                if(move_once):
                    print('\n')
                    move_once = False
                print(self.init[i], end=" ")
            else:
                if(move_twice):
                    print('\n')
                    move_twice=False
                print(self.init[i],end = " ")


        print('\n \n')
        for i in range(len(self.current.table)):
            row = i//3
            if(row==0):
                print(self.current.table[i],end=" ")
            elif(row==1):
                if(move_third):
                    print('\n')
                    move_third = False
                print(self.current.table[i], end=" ")
            else:
                if(move_fourth):
                    print('\n')
                    move_fourth=False
                print(self.current.table[i],end = " ")

        print('\n')

        print(self.depth)
        print(self.size)
        print(self.directions)


    
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
            newNode.parent = self.current
            newNode.level = self.current.level+1
            newNode.goal = self.goal
            newNode.table = self.current.table.copy()
            
        return newNode

    
 

    def getDirection(self,chosenNode):
        #Adds Directions Traversed
        #Updates current

        self.directions.append(chosenNode.path)
        self.current = chosenNode

    
        
    def calculateCheapestChild(self):
        #Calculates Manhattan Distance by
        #*Adding all children to array
        #*Calculating thself.queued.append(self.current.left)e cost and position keeps track of LURD
        
        if(self.current.left is not None and self.current.left.table not in self.visited):
 
            wrong = self.current.left.level + self.current.left.getIncorrect()
            self.current.left.cost = wrong
            self.current.left.path ='L'
            self.queued.append(self.current.left)
            self.visited.append(self.current.left.table)
        
            self.size+=1

        if(self.current.up is not None and self.current.up.table not in self.visited):
            wrong = self.current.up.level + self.current.up.getIncorrect()
            self.current.up.path = "U"
            self.current.up.cost = wrong
            self.queued.append(self.current.up)
            self.visited.append(self.current.up.table)
          
            self.size+=1

        if(self.current.right is not None and self.current.right.table not in self.visited):
            wrong = self.current.right.level + self.current.right.getIncorrect()
            self.current.right.cost = wrong
            self.current.right.path = "R"
            self.queued.append(self.current.right)
            self.visited.append(self.current.right.table)
            self.size+=1

        if(self.current.down is not None and self.current.down.table not in self.visited):
            wrong = self.current.down.level + self.current.down.getIncorrect()
            self.current.down.cost = wrong
            self.current.down.path = "D"
            self.queued.append(self.current.down)
            self.visited.append(self.current.down.table)
 
            self.size+=1
 
        #Each keeps track of which child then cheapest

        treeCost =[]
        for i in range(len(self.queued)):
            treeCost.append(self.queued[i].cost)
        print(treeCost)
        posNode= min(treeCost)
        index_que = treeCost.index(posNode)

        print(self.queued[index_que].path)
        
        
        chosenNode = self.queued[index_que]
        self.getDirection(chosenNode)
        self.queued.pop(index_que)

                    
             


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
    print(init)
    #Call Graph search taking in inital and final stages
    GSA = tree(init,final)
    GSA.start()
