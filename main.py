import pygame
import queue
import random
import time
from queue import PriorityQueue
from tkinter import messagebox, Tk

#pygame initialisation
pygame.init()

#setting up pygame constants and variables
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Algorthim Visualizer")
pygame_icon = pygame.image.load("images/AVicon.png")
pygame.display.set_icon(pygame_icon)

#color codes 
RED = (255, 0 , 0)                 #Closed
GREEN = (0, 255, 0)                #Open
YELLOW = (255,255,0)               #Path
WHITE = (255,255,255)              #Default
BLACK = (0,0,0)                    #Barrier
ORANGE = (255,165,0)               #Start
GREY = (128,128,128)               #Grid lines
TURQUOISE = (64,224,208)           #End


#individual spot or each square (block) is defined here
class Spot:
    def __init__(self,row,col,width,total_rows ) :
        self.row = row 
        self.col = col
        #actual coordinates to draw the cubes 800/no.of rows or cols = width of one side of the spot
        self.x = row * width  
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col  

    def is_closed(self):
         return self.color == RED
    
    def is_open(self):
         return self.color == GREEN
    
    def is_barrier(self):
         return self.color == BLACK

    def is_start(self):
         return self.color == ORANGE
    
    def is_end(self):
         return self.color == TURQUOISE
    
    def is_path(self):
         return self.color == YELLOW
    
    def reset(self):
         self.color = WHITE

    def make_start(self):
         self.color = ORANGE

    def make_closed(self):
         self.color = RED

    def make_open(self):
         self.color = GREEN
    
    def make_barrier(self):
         self.color = BLACK
    
    def make_end(self):
         self.color = TURQUOISE

    def make_path(self):
         self.color = YELLOW
    
    def drawSpot(self,win):
         pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def update_neighbours(self,grid):
         self.neighbours = []

         if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #checking DOWN neighbours
              self.neighbours.append(grid[self.row + 1][self.col])

         if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #checking UP neighbours
              self.neighbours.append(grid[self.row - 1][self.col])
         
         if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #checking LEFT neighbours
              self.neighbours.append(grid[self.row][self.col - 1])
         
         if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1 ].is_barrier(): #checking RIGHT neighbours
              self.neighbours.append(grid[self.row][self.col + 1])
         
    #magic function in python
    #to compare two spot instances
    def __lt__(self,other):
         return False
    

#Heuristic function
#using manhattan distance would be better than euclidean distance here since diagonals are not important (hypotenuase)
#taxicab distance can't use diagonals

def h(p1,p2):
    x1 , y1 = p1
    x2 , y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


#function to generate random mazes
def make_maze(draw,grid,rows):
     value = (rows*rows)//3

     for k in range(value):
          i = random.randint(0,rows-1)
          j = random.randint(0,rows-1)
          grid[i][j].make_barrier()
     draw()

     return

#Time taken by each algortihm to come to a conclusion
def TimeTaken(startTime,stopTime):
     Total_time = " Time = "+ str(round(stopTime - startTime,3)) + " seconds"
     return Total_time

#statistics and comparison of different algorithms via factors like time taken and number of comparisions done to be shown to the user
def stat(name,flag,time,comparisons):

     if flag == False:
          value = name + " :" + "No solution exists ," + time +" , Comparisons made  = "+ str(comparisons) +" blocks"+"\n"
          return value
     else:
          value = name + " :" + time + " , Comparisons made = "+ str(comparisons) + " blocks" + "\n"
     
     return value

#reset environment after running an algorithm in the series of all the algorithms to be run for comparison purposes
#start ,end and the barriers remain same rest of the spots are reset to default i.e WHITE

def compReset(grid,ROWS,start,end):
     
     for row in grid:
          for spot in row:
               spot.update_neighbours(grid)

     for i in range(ROWS):
          for j in range(ROWS) :
               if grid[i][j].is_barrier() or grid[i][j].is_start() or grid[i][j].is_end() or grid[i][j].color == WHITE:
                    continue

               elif grid[i][j].is_closed() or grid[i][j].is_open() or grid[i][j].is_path():
                    grid[i][j].reset()

     return


# function to compare the algorithms and display visually
def compare(win,grid,ROWS,width,start,end):

     compReset(grid,ROWS,start,end)
     flag1 , time1 ,comp1 = Astar( lambda : draw(win,grid,ROWS,width),grid,start,end )
     value1 = stat("Astar",flag1,time1,comp1)
     time.sleep(2)
     compReset(grid,ROWS,start,end)

     flag2 , time2 , comp2 = BFS( lambda : draw(win,grid,ROWS,width),grid,start,end )
     value2 = stat("BFS",flag2,time2,comp2)
     time.sleep(2)
     compReset(grid,ROWS,start,end)

     flag3 , time3 , comp3  = DFS( lambda : draw(win,grid,ROWS,width),grid,start,end )
     value3 = stat("DFS",flag3,time3,comp3)
     time.sleep(2)
     compReset(grid,ROWS,start,end)

     flag4 , time4 , comp4 = Dijkstra( lambda : draw(win,grid,ROWS,width),grid,start,end )
     value4 = stat("Dijkstra",flag4,time4,comp4)
     time.sleep(2)
     compReset(grid,ROWS,start,end)

     flag5 , time5 , comp5 = GBFS( lambda : draw(win,grid,ROWS,width),grid,start,end )
     value5 = stat("GBFS",flag5,time5,comp5)
     time.sleep(2)

     #using tinkter messagebox to display the information 

     if flag1 == False or flag2 == False or flag3 == False or flag4 == False or flag5 == False :
          Tk().wm_withdraw()
          messagebox.showinfo("No Solution", value1 + value2 + value3 + value4 + value5)
     else :
          Tk().wm_withdraw()
          messagebox.showinfo("Statistics", value1 + value2 + value3 + value4 + value5)
     return


#reconstruct the found path from start to end via the algorithm used
def reconstruct_path(came_from,current,start,draw):
     current.make_end()

     while current in came_from and current != start:
          current = came_from[current]
          current.make_path()
          draw()     
     start.make_start()
     draw() 

#A star algortihm
def Astar(draw,grid,start,end):
     comparisons = 0
     count = 0
     open_set = PriorityQueue()
     open_set.put((0,count,start))
     came_from = {}

     #f(x) = g(x) + h(x) where g is the cost and h is the heuristics
     
     g_score = {spot: float("inf") for row in grid for spot in row }
     g_score[start] = 0
     
     f_score = {spot: float("inf") for row in grid for spot in row }
     f_score[start] = h(start.get_pos(),end.get_pos())

    #for tracking since there is no feature of tracking in priority queue
     open_set_hash = {start}

     #start timer to note the time taken
     startTime = time.time()

     while not open_set.empty():
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
            
          current = open_set.get()[2]
          open_set_hash.remove(current)

          comparisons += 1
          if current == end:  
               reconstruct_path(came_from,end,start,draw)
               end.make_end()
               
               #stop timer
               stopTime = time.time()

               return True , TimeTaken(startTime,stopTime) ,comparisons
          
          for neighbour in current.neighbours:
               temp_g_score = g_score[current] + 1 #since it is not a weighted graph ,all paths cost same , ie. 1

               if temp_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_g_score + h(neighbour.get_pos(),end.get_pos())
                    if neighbour not in open_set_hash:
                         count += 1
                         open_set.put((f_score[neighbour],count,neighbour))
                         open_set_hash.add(neighbour)
                         neighbour.make_open()
         
          draw()    
          if current != start:
              current.make_closed()
    
     stopTime = time.time()
     return False , TimeTaken(startTime,stopTime) ,comparisons


#Breadth first search algorithm
def BFS(draw,grid,start,end):
    
    #queue is used to implement bfs
    comparisons = 0
    q = queue.Queue()
    q.put((start,[start]))
    visited = set()
    came_from = {}

    startTime = time.time()

    while not q.empty():
         current , path = q.get()
         start.make_start()
         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
         comparisons += 1

         if current == end:
               reconstruct_path(came_from,end,start,draw)
               stopTime = time.time()
               return True , TimeTaken(startTime,stopTime), comparisons
         
         for neighbour in current.neighbours:
              if neighbour in visited:
                   continue
              else:
                   new_path = path + [neighbour]
                   neighbour.make_open()
                   came_from[neighbour] = current
                   q.put((neighbour,new_path))
                   visited.add(neighbour)

         draw()    

         if current != start:
               current.make_closed()      

    stopTime = time.time()
    return False , TimeTaken(startTime,stopTime) ,comparisons


#Depth first seaech algorithm
def DFS(draw,grid,start,end):

     #stack is used to implement dfs we use list to implemnt stack
     comparisons = 0
     stack = []
     came_from = {}
     visited = set()

     stack.append(start)

     startTime = time.time()

     while len(stack) != 0 :
          current = stack.pop()

          start.make_start()
          
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
          comparisons += 1

          if current == end :
               reconstruct_path(came_from,end,start,draw)
               stopTime = time.time()
               return True , TimeTaken(startTime,stopTime),comparisons
          
          for neighbour in current.neighbours:
               if neighbour in visited:
                    continue
               else:
                    stack.append(neighbour)
                    came_from[neighbour] = current
                    if neighbour == end:
                         neighbour.make_end()
                    else:
                         neighbour.make_open()
                    visited.add(neighbour)
          draw()

          if current != start:
               current.make_closed()

     stopTime = time.time()

     return False , TimeTaken(startTime,stopTime),comparisons

#Dijkstra algorithm
def Dijkstra(draw,grid,start,end):
     comparisons = 0
     open_set = PriorityQueue()
     open_set.put((0,start))
     camefrom = {}

     shortest_path = {spot: float("inf") for row in grid for spot in row}
     shortest_path[start] = 0

     startTime = time.time()

     while not open_set.empty():
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    
          current_distance,current = open_set.get()
          comparisons += 1

          if current == end:
               reconstruct_path(camefrom,end,start,draw)
               stopTime = time.time()
               return True , TimeTaken(startTime,stopTime),comparisons
          if current_distance > shortest_path[current]:
               continue
          else:
               for neighbour in current.neighbours:
                    distance = current_distance + 1 #sicne its not a weighted graph ,all paths cost same ie. 1
                    if distance < shortest_path[neighbour]:
                         shortest_path[neighbour] = distance
                         camefrom[neighbour] = current
                         neighbour.make_open()
                         open_set.put((distance,neighbour))

          draw()

          if current != start:
               current.make_closed()

     stopTime = time.time()
     return False , TimeTaken(startTime,stopTime),comparisons

#Greedy best first search algorithm
def GBFS(draw,grid,start,end):
     comparisons = 0
     count = 0
     open_set = PriorityQueue()
     open_set.put((0,count,start))
     came_from = {}

     #only heuristics function is used 
     h_score = {spot: float("inf") for row in grid for spot in row }
     h_score[start] = h(start.get_pos(),end.get_pos())

    #for tracking since there is no feature of tracking in priority queue
     open_set_hash = {start}

     startTime = time.time()

     while not open_set.empty():
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
            
          current = open_set.get()[2]
          open_set_hash.remove(current)

          comparisons += 1

          if current == end:  
               reconstruct_path(came_from,end,start,draw)
               end.make_end()
               stopTime = time.time()
               return True , TimeTaken(startTime,stopTime),comparisons
          
          for neighbour in current.neighbours:
               temp_h_score = h(neighbour.get_pos(),end.get_pos())
               if temp_h_score < h_score[neighbour]:
                    came_from[neighbour] = current
                    h_score[neighbour] = h(neighbour.get_pos(),end.get_pos())

                    if neighbour not in open_set_hash:
                         count += 1
                         open_set.put((h_score[neighbour],count,neighbour))
                         open_set_hash.add(neighbour)
                         neighbour.make_open()
         
          draw()    
          if current != start:
              current.make_closed()
     
     stopTime = time.time()
     return False , TimeTaken(startTime,stopTime),comparisons


#construct the grid (skeleton) using a 2D list
def make_grid(rows,width):
    grid = []
    lengthOfSpotSide = width//rows

    for i in range(rows):              
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,lengthOfSpotSide,rows)
            grid[i].append(spot)
        
    return grid   
    

#function to draw the grid lines on the screen
def draw_grid(win,rows,width):
    lengthOfOneSide = width//rows

    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i * lengthOfOneSide), (width,i * lengthOfOneSide))
        for j in range(rows):
            pygame.draw.line(win,GREY,(j * lengthOfOneSide , 0),(j * lengthOfOneSide,width))


#function to draw the entire screen : fill the screen,draw the grid lines,draw each spot according to thier current status or value
def draw(win,grid,rows,width):
     win.fill(WHITE)

     for row in grid:
          for spot in row:
               spot.drawSpot(win)

     draw_grid(win,rows,width)
     pygame.display.update()
         
#returns position in terms of rows and cols in the grid
def get_clicked_pos(pos,rows,width):
     gap = width//rows
     y,x = pos
     row = y//gap
     col = x//gap
     return row,col

#the initial page which shows up on screen
def introPage():

     intro = pygame.image.load("images/intro.png")
     introrect = intro.get_rect(topleft=(0,0))
     
     WIN.fill(WHITE)
     WIN.blit(intro,introrect)
     pygame.display.update()
     time.sleep(2.5 )
     return
     
#the instructions or information screen
def infoPage():
     run = True
     
     instructions = pygame.image.load("images/instructions.png")
     instructionsrect = instructions.get_rect(topleft=(0,0))

     while run:
        WIN.fill(WHITE)
        WIN.blit(instructions,instructionsrect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return


#no solution found screen
def noSolutionPage():
     time.sleep(2)
     run = True
     
     noSolution = pygame.image.load("images/noSolution.png")
     noSolutionrect = noSolution.get_rect(topleft=(0,0))

     while run:
        WIN.fill(WHITE)
        WIN.blit(noSolution,noSolutionrect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return
     

#the main function
def main(win,width):
     ROWS = 50
     grid = make_grid(ROWS,width)
     start = None
     end = None
     run = True

     #intro page is displayed on screen
     introPage()

     #information or instructions page is displayed
     infoPage()  

     #all keyboard and mouse events are handled here
     while run:
          draw(win, grid, ROWS, width)

          for event in pygame.event.get(): #quit button on top
               if event.type == pygame.QUIT:
                    run = False

               if pygame.mouse.get_pressed()[0]: #left click
                    pos = pygame.mouse.get_pos()
                    row , col = get_clicked_pos(pos , ROWS , width)
                    spot = grid[row][col]
                    if not start and spot != end:
                         start = spot
                         start.make_start()
                    elif not end and spot!= start:
                         end = spot
                         end.make_end()
                    elif spot != start and spot != end :
                         spot.make_barrier()   
                     

               elif pygame.mouse.get_pressed()[2]: #right click
                    pos = pygame.mouse.get_pos()
                    row , col = get_clicked_pos(pos , ROWS , width)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                         start = None
                    elif spot == end:
                         end = None
                
               if event.type == pygame.KEYDOWN:   #keyboard events
                    if event.key == pygame.K_a and start and end:
                         for row in grid:
                              for spot in row:
                                   spot.update_neighbours(grid)
                         flag , timetaken , comparisons = Astar( lambda : draw(win,grid,ROWS,width),grid,start,end )
                         if flag == False:
                                noSolutionPage()
                    
                    elif event.key == pygame.K_b and start and end:
                         for row in grid:
                              for spot in row:
                                   spot.update_neighbours(grid)
                         flag , timetaken ,comparisons = BFS( lambda : draw(win,grid,ROWS,width),grid,start,end )
                         if flag == False:
                                noSolutionPage()

                    elif event.key == pygame.K_d and start and end:
                         for row in grid:
                              for spot in row:
                                   spot.update_neighbours(grid)
                         flag , timetaken , comparisons = DFS( lambda : draw(win,grid,ROWS,width),grid,start,end )
                         if flag == False:
                                noSolutionPage()
                    
                    elif event.key == pygame.K_j and start and end:
                         for row in grid:
                              for spot in row:
                                   spot.update_neighbours(grid)
                         flag , timetaken , comparisons = Dijkstra( lambda : draw(win,grid,ROWS,width),grid,start,end )
                         if flag == False:
                                noSolutionPage()

                    elif event.key == pygame.K_g and start and end:
                         for row in grid:
                              for spot in row:
                                   spot.update_neighbours(grid)
                         flag , timetaken , comparisons = GBFS( lambda : draw(win,grid,ROWS,width),grid,start,end )
                         if flag == False:
                                noSolutionPage()

                    elif event.key == pygame.K_m and not start and not end:
                         make_maze( lambda : draw(win,grid,ROWS,width),grid,ROWS)
                       
                    elif event.key == pygame.K_w and start and end:
                         compare(win,grid,ROWS,width,start,end)
                        
                    elif event.key == pygame.K_h or event.key == pygame.K_ESCAPE:
                         infoPage()  

                    elif event.key == pygame.K_k and start and end:
                         compReset(grid,ROWS,start,end)

                    elif event.key == pygame.K_c:
                         start = None
                         end = None
                         grid = make_grid(ROWS,width)     

     pygame.quit()

#the main function is called
main(WIN,WIDTH)