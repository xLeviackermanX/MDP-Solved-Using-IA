import numpy as np
from probability import *
from probability import  East as c 
def findEast(mat , arrow , state , health , u,v,bestAction):
    
    ut = -1e18
    strState = '(East , ' + str(mat)+' , '+str(arrow)+' , '+stateName[state]+' , '+str(health*healthMultiple)+')'
    strAction = 'None'
    if state==1:
        
        xt = (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[1][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health]) + c.pAttack*(c.loss+stepCost + gamma*u[1][mat][0][0][min(health+1,4)])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health]) + c.pAttack*(c.loss+stepCost + gamma*u[1][mat][0][0][min(health+1,4)])
        if ut<xt:
            strAction = 'Left'
            ut = xt
        
        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:
            xt= (1-c.pAttack)*(c.pShoot*(reward+stepCost+ gamma*u[1][mat][arrow-1][1][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[1][mat][arrow-1][1][health])+c.pAttack*(c.loss+stepCost + gamma*u[1][mat][0][0][min(health+1,4)])
            if ut<xt: 
                strAction = 'Shoot'
                ut = xt
        if health==2:
            reward = c.profit
        
        xt= (1-c.pAttack)*(c.pBlade*stepCost+c.pBlade*(reward
            + gamma*u[1][mat][arrow][1][max(health+c.bladeDamage,0)])+(1-c.pBlade)*stepCost+(1-c.pBlade)*gamma*u[1][mat][arrow][1][health])+c.pAttack*(c.loss+stepCost + gamma*u[1][mat][0][0][min(health+1,4)])
        if ut<xt:
            strAction = 'Hit'
            ut = xt
        v[1][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[1][mat][arrow][state][health] = actionIndex[strAction]
    else:
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[1][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[1][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Left'
            ut = xt
        
        reward = 0.0
        if health<2:
            reward = c.profit
        if arrow>0:
            
            xt= c.pReady*(c.pShoot*(reward+stepCost+ gamma*u[1][mat][arrow-1][1][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[1][mat][arrow-1][1][health])+1.0*(1-c.pReady)*(c.pShoot*(reward+stepCost + gamma*u[1][mat][arrow-1][0][max(health+shootDamage,0)])+(1-c.pShoot)*stepCost+(1-c.pShoot)*gamma*u[1][mat][arrow-1][0][health])
            if ut<xt:
                strAction = 'Shoot'
                ut = xt
        if health==2:
            reward = c.profit
        
        xt= c.pReady*(c.pBlade*stepCost+c.pBlade*(reward + gamma*u[1][mat][arrow][1][max(health+c.bladeDamage,0)])+(1-c.pBlade)*stepCost+(1-c.pBlade)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pBlade*stepCost+c.pBlade*(reward + gamma*u[1][mat][arrow][0][max(health+c.bladeDamage,0)])+(1-c.pBlade)*stepCost+(1-c.pBlade)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Hit'
            ut = xt
        v[1][mat][arrow][state][health] = ut

        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[1][mat][arrow][state][health] = actionIndex[strAction]
    return v , bestAction

 
