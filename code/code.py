import numpy as np
from findPolicy import *
from centre import *
from north import *
from east import *
from west import *
from south import *
from probability import *
stepCost = -10
gamma = 0.999
delta = 0.001

dir = np.array(['C', 'E','W','N','S'])

#state  = (position , material , arrows , ready(1) or dormant(0) , health)

#starting state is = (2 , 0 , 0 , 0 , )

u =   [[[[[0.0]*5]*2]*4]*3]*5
u =  np.array(u)
v =   [[[[[0.0]*5]*2]*4]*3]*5
v =  np.array(v)
bestAction =   [[[[[9]*5]*2]*4]*3]*5
bestAction = np.array(bestAction)
counter = 1
while(1):
    writeFile('Iteration-'+str(counter)+'\n')
    counter+=1
    dif = 0.0
    for mat in range(0,3):
        for arrow in range(0,4):
            for state in range(0,2):
                for health in range(1,5):
                    v , bestAction = findCentre(mat , arrow , state , health , u,v,bestAction)
                    v , bestAction = findEast(mat , arrow , state , health , u,v,bestAction)
                    v , bestAction = findWest(mat , arrow , state , health , u,v,bestAction)
                    v , bestAction = findSouth(mat , arrow , state , health , u,v,bestAction)
                    v , bestAction = findNorth(mat , arrow , state , health , u,v,bestAction)
                    for i in range(0,5):
                     #   if i==0 and mat==0 and state==0 and health==1 and arrow==0:
                      #      print(v[0][0][0][0][1] , u[0][0][0][0][1])
                        dif = max(dif,abs(v[i][mat][arrow][state][health]-u[i][mat][arrow][state][health]))
    for mat in range(0,3):
        for arrow in range(0,4):
            for state in range(0,2):
                for health in range(1,5):
                    for i in range(0,5):
                        u[i][mat][arrow][state][health]=v[i][mat][arrow][state][health]
    if dif<delta:
    	break
print(bestAction)
findPolicy(bestAction , 2 , 0 , 0, 0, 4)
f1 = open("Policy.txt","a")
f1.write("\n\nFor new start State:\n\n")
f1.close()
findPolicy(bestAction , 0, 2 ,0 , 1, 4)
#C, 2, 0, R, 100)
