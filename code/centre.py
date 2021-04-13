import numpy as np
from probability import *
from probability import  Centre as c 
def findCentre(mat , arrow , state , health , u,v,bestAction):
    #print(u)
    ut = -1e18
    strState = '(Centre , ' + str(mat)+' , '+str(arrow)+' , '+stateName[state]+' , '+str(health*healthMultiple)+')'
    strAction = 'None'
    if state==1:
        
        xt = (1-c.pAttack)*(c.pMove*(stepCost+gamma*u[0][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health])) + c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
        if ut<xt:
        	strAction = 'Stay'
        	ut = xt
        
        xt= (1-c.pAttack)*(c.pMove*(stepCost+gamma*u[1][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health])) + c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
        if ut<xt:
        	strAction = 'Right'
        	ut = xt
        
        xt= (1-c.pAttack)*(c.pMove*(stepCost+gamma*u[2][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health])) + c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
        if ut<xt:
        	strAction = 'Left'
        	ut = xt
        
        xt= (1-c.pAttack)*(c.pMove*(stepCost+gamma*u[3][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health])) + c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
        if ut<xt:
        	strAction = 'Up'
        	ut = xt
        
        xt= (1-c.pAttack)*(c.pMove*(stepCost+gamma*u[4][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health])) + c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
        if ut<xt:
        	strAction = 'Down'
        	ut = xt
        reward = 0.0
        if health<2:
        	reward = c.profit
        if arrow>0:
            xt= (1-c.pAttack)*(c.pShoot*(reward+ (stepCost+gamma*u[0][mat][arrow-1][1][max(health+shootDamage,0)]))+(1-c.pShoot)*(stepCost+gamma*u[0][mat][arrow-1][1][health]))+c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
            if ut<xt: 
            	strAction = 'Shoot'
            	ut = xt
        if health==2:
            reward = c.profit
        
        xt= (1-c.pAttack)*(c.pBlade*(reward
            + (stepCost+gamma*u[0][mat][arrow][1][max(health+c.bladeDamage,0)]))+(1-c.pBlade)*(stepCost+gamma*u[0][mat][arrow][1][health]))+c.pAttack*(c.loss + (stepCost+gamma*u[0][mat][0][0][min(health+1,4)]))
        if ut<xt:
        	strAction = 'Hit'
        	ut = xt
        v[0][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[0][mat][arrow][state][health] = actionIndex[strAction]
    else:
        
        xt= c.pReady*(c.pMove*(stepCost+gamma*u[0][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health]))+1.0*(1-c.pReady)*(c.pMove*(stepCost+gamma*u[0][mat][arrow][0][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][0][health]))
        if ut<xt:
        	strAction = 'Stay'
        	ut = xt
        
        xt= c.pReady*(c.pMove*(stepCost+gamma*u[1][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health]))+1.0*(1-c.pReady)*(c.pMove*(stepCost+gamma*u[1][mat][arrow][0][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][0][health]))
        if ut<xt:
        	strAction = 'Right'
        	ut = xt
        
        xt= c.pReady*(c.pMove*(stepCost+gamma*u[2][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health]))+1.0*(1-c.pReady)*(c.pMove*(stepCost+gamma*u[2][mat][arrow][0][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][0][health]))
        if ut<xt:
        	strAction = 'Left'
        	ut = xt
        
        xt= c.pReady*(c.pMove*(stepCost+gamma*u[3][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health]))+1.0*(1-c.pReady)*(c.pMove*(stepCost+gamma*u[3][mat][arrow][0][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][0][health]))
        if ut<xt:
        	strAction = 'Up'
        	ut = xt
        
        xt= c.pReady*(c.pMove*(stepCost+gamma*u[4][mat][arrow][1][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][1][health]))+1.0*(1-c.pReady)*(c.pMove*(stepCost+gamma*u[4][mat][arrow][0][health])+(1-c.pMove)*(stepCost+gamma*u[1][mat][arrow][0][health]))
        if ut<xt:
        	strAction = 'Down'
        	ut = xt
        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:
            
            xt= c.pReady*(c.pShoot*(reward+ (stepCost+gamma*u[0][mat][arrow-1][1][max(health+shootDamage,0)]))+(1-c.pShoot)*(stepCost+gamma*u[0][mat][arrow-1][1][health]))+1.0*(1-c.pReady)*(c.pShoot*(reward + (stepCost+gamma*u[0][mat][arrow-1][0][max(health+shootDamage,0)]))+(1-c.pShoot)*(stepCost+gamma*u[0][mat][arrow-1][0][health]))
            if ut<xt:
            	strAction = 'Shoot'
            	ut = xt
        if health==2:
            reward = c.profit
        
        xt= c.pReady*(c.pBlade*(reward + (stepCost+gamma*u[0][mat][arrow][1][max(health+c.bladeDamage,0)]))+(1-c.pBlade)*(stepCost+gamma*u[0][mat][arrow][1][health]))+1.0*(1-c.pReady)*(c.pBlade*(reward + (stepCost+gamma*u[0][mat][arrow][0][max(health+c.bladeDamage,0)]))+(1-c.pBlade)*(stepCost+gamma*u[0][mat][arrow][0][health]))
        if ut<xt:
        	strAction = 'Hit'
        	ut = xt
        if mat==0 and arrow==0 and state==0 and health==2:
            print(ut,strAction)

        v[0][mat][arrow][state][health] = ut

        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[0][mat][arrow][state][health] = actionIndex[strAction]
    return v , bestAction

 
