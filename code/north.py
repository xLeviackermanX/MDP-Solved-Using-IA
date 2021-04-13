import numpy as np
from probability import *
from probability import  North as c 

def findNorth(mat , arrow , state , health , u,v,bestAction):
    
    ut = -1e18
    strState = '(North , ' + str(mat)+' , '+str(arrow)+' , '+stateName[state]+' , '+str(health*healthMultiple)+')'
    strAction = 'None'
    if state==1:
        
        xt = (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[3][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+(c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[3][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= (1-c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+(c.pAttack)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])
        if ut<xt:
            strAction = 'Down'
            ut = xt

        if mat>0:
            xt = (1-c.pAttack)*(stepCost+c.pOneArrow*gamma*u[3][mat-1][min(arrow+1,3)][1][health]+c.pTwoArrow*gamma*u[3][mat-1][min(arrow+2,3)][1][health]+c.pThreeArrow*gamma*u[3][mat-1][min(arrow+3,3)][1][health])+(c.pAttack)*(stepCost+c.pOneArrow*gamma*u[3][mat-1][min(arrow+1,3)][0][health]+c.pTwoArrow*gamma*u[3][mat-1][min(arrow+2,3)][0][health]+c.pThreeArrow*gamma*u[3][mat-1][min(arrow+3,3)][0][health])
            if ut<xt:
                strAction = 'Craft'
                ut = xt
        v[3][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[3][mat][arrow][state][health] =actionIndex[strAction]
    else:
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[3][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[3][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Stay'
            ut = xt
        
        
        xt= c.pReady*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][1][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][1][health])+1.0*(1-c.pReady)*(c.pMove*stepCost+c.pMove*gamma*u[0][mat][arrow][0][health]+(1-c.pMove)*stepCost+(1-c.pMove)*gamma*u[1][mat][arrow][0][health])
        if ut<xt:
            strAction = 'Down'
            ut = xt
        
        if mat>0:
            xt = (c.pReady)*(stepCost+c.pOneArrow*gamma*u[3][mat-1][min(arrow+1,3)][1][health]+c.pTwoArrow*gamma*u[3][mat-1][min(arrow+2,3)][1][health]+c.pThreeArrow*gamma*u[3][mat-1][min(arrow+3,3)][1][health])+(1-c.pReady)*(stepCost+c.pOneArrow*gamma*u[3][mat-1][min(arrow+1,3)][0][health]+c.pTwoArrow*gamma*u[3][mat-1][min(arrow+2,3)][0][health]+c.pThreeArrow*gamma*u[3][mat-1][min(arrow+3,3)][0][health])
            if ut<xt:
                strAction = 'Craft'
                ut = xt
        v[3][mat][arrow][state][health] = ut
        writeFile(strState+' : '+strAction +' = '+str(ut))
        bestAction[3][mat][arrow][state][health] = actionIndex[strAction]
    return v , bestAction
