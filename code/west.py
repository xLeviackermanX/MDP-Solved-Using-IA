import numpy as np
from probability import *
from probability import  West as c 

def findWest(mat , arrow , state , health , u,v,bestAction):
    
    ut = -1e18
    strState = '(West , ' + str(mat)+' , '+str(arrow)+' , '+stateName[state]+' , '+str(health*healthMultiple)+')'
    strAction = 'None'
    if state==1:
        
        xt = (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[2][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+(c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[2][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+(c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Right'
            ut = xt
        
        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:
            xt= (1-c.pAttack)*(c.pShoot*stepCost+c.pShoot*(reward+ gamma*u[2][mat][arrow-1][1][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[2][mat][arrow-1][1][health])+(c.pAttack)*(c.pShoot*stepCost+c.pShoot*(reward+ gamma*u[2][mat][arrow-1][1][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[2][mat][arrow-1][1][health])
            if ut<xt: 
                strAction = 'Shoot'
                ut = xt
        v[2][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[2][mat][arrow][state][health] = actionIndex[strAction]
    else:
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[2][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[2][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Right'
            ut = xt
        
        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:
            
            xt= c.pReady*(c.pShoot*stepCost+c.pShoot*(reward+ gamma*u[2][mat][arrow-1][1][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[2][mat][arrow-1][1][health])+1.0*(1-c.pReady)*(c.pShoot*stepCost+c.pShoot*(reward + gamma*u[2][mat][arrow-1][0][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[2][mat][arrow-1][0][health])
            if ut<xt:
                strAction = 'Shoot'
                ut = xt
        v[2][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[2][mat][arrow][state][health] = actionIndex[strAction]
    return v , bestAction

 
