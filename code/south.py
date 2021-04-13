import numpy as np
from probability import *
from probability import  South as c 

def findSouth(mat , arrow , state , health , u,v,bestAction):
    
    ut = -1e18
    strState = '(South , ' + str(mat)+' , '+str(arrow)+' , '+stateName[state]+' , '+str(health*healthMultiple)+')'
    strAction = 'None'
    if state==1:
        
        xt = (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[4][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+(c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[4][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+(c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Up'
            ut = xt
        
        xt = (1-c.pAttack)*(c.pGainMat*stepCost+c.pGainMat*gamma*u[4][min(mat+1,2)][arrow][1][health]+(1-c.pGainMat)*stepCost+(1-c.pGainMat)*gamma*u[1][min(mat+1,2)][arrow][1][health])+(c.pAttack)*(c.pGainMat*stepCost+c.pGainMat*gamma*u[4][min(mat+1,2)][arrow][0][health]+(1-c.pGainMat)*stepCost+(1-c.pGainMat)*gamma*u[1][min(mat+1,2)][arrow][0][health])
        if ut<xt:
            strAction = 'Gather'
            ut = xt
        v[4][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[4][mat][arrow][state][health] = actionIndex[strAction]
    else:
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[4][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[4][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Up'
            ut = xt

        xt= c.pReady*(c.pGainMat*stepCost+c.pGainMat*gamma*u[4][min(mat+1,2)][arrow][1][health]+(1-c.pGainMat)*stepCost+(1-c.pGainMat)*gamma*u[1][min(mat+1,2)][arrow][1][health])+1.0*(1-c.pReady)*(c.pGainMat*stepCost+c.pGainMat*gamma*u[4][min(mat+1,2)][arrow][0][health]+(1-c.pGainMat)*stepCost+(1-c.pGainMat)*gamma*u[1][min(mat+1,2)][arrow][0][health])
        if ut<xt:
            strAction = 'Gather'
            ut = xt
        
        v[4][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[4][mat][arrow][state][health] = actionIndex[strAction]
    return v , bestAction

 
