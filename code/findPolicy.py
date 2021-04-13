import numpy as np 
import random
from probability import *
def findPolicy(bestAction , pos, mat , arrow , state , health):
    if health == 0:
        f1 = open("Policy.txt","a")
        f1.write("End State Reached! \n")
        f1.close()
        return
    action = actionAll[bestAction[pos][mat][arrow][state][health]]
    f1 = open("Policy.txt","a")
    yo = ""
    yo += "("+position[pos]+" , "+str(mat)+" , "+str(arrow)+" , "+stateName[state]+" , "+str(25*health)+" : "+action+"\n"
    f1.write(yo)
    f1.close()
    if pos == 0:
        if action=="Stay":
            if state==1:
                num = random.uniform(0,1)
                if num<=Common.pAttack:
                    health = min(health+1,4)
                    arrow = 0
                    state = 0
                else:
                    num = randon.uniform(0,1)
                    if num>Centre.pMove:
                        pos = 1
            else:
                num = random.uniform(0,1)
                if num<=Common.pReady:
                    state = 1
                num = random.uniform(0,1)
                if num>Centre.pMove:
                    pos = 1
        elif action=="Right":
            if state==1:
                num = random.uniform(0,1)
                if num<=Common.pAttack:
                    health = min(health+1,4)
                    arrow = 0
                    state = 0
                else:
                    pos = 1
                    num = random.uniform(0,1)
                    if num<=Common.pReady:
                        state = 1
            else:
                num = random.uniform(0,1)
                if num<=Common.pReady:
                    state = 1
                num = random.uniform(0,1)
                pos = 1
        elif action=="Left":
            if state==1:
                num = random.uniform(0,1)
                if num<=Common.pAttack:
                    state = 0
                    health = min(health+1,4)
                    arrow = 0
                else:
                    num = random.uniform(0,1)
                    if num<=Centre.pMove:
                        pos = 2
                    else:
                        pos = 1

            else:
                num = random.uniform(0,1)
                if num<=Centre.pMove:
                    pos = 2
                else:
                    pos = 1
                num = random.uniform(0,1)
                if num<=Common.pReady:
                    state = 1
        elif action=="Up":
            num = random.uniform(0,1)
            if state==1 and num<=Common.pAttack:
                state = 0
                health = min(health+1,4)
                arrow = 0
            else:
                num = random.uniform(0,1)
                if num<=Centre.pMove:
                    pos = 3
                else:
                    pos = 1
                if state==0:
                    num = random.uniform(0,1)
                    if num<=Common.pReady:
                        state = 1
        elif action=="Down":
            num = random.uniform(0,1)
            if state==1 and num<=Common.pAttack:
                state = 0
                health = min(health+1,4)
                arrow = 0
            else:
                num = random.uniform(0,1)
                if num<=Centre.pMove:
                    pos = 4
                else:
                    pos = 1
                if state ==0:
                    num = random.uniform(0,1)
                    if num<=Common.pReady:
                        state = 1
        elif action=="Shoot":
            num = random.uniform(0,1)
            if state == 1 and num <= Common.pAttack:
                state = 0
                health = min(health+1,4)
                arrow = 0
            else:
                num = random.uniform(0,1)
                if num<=Centre.pShoot:
                    health = max(health+shootDamage,0)
                    arrow = max(arrow-1,0)
                else:
                    arrow = max(arrow-1,0)
                if state==0:
                    num = random.uniform(0,1)
                    if num<=Common.pReady:
                        state = 1
        else:
            num = random.uniform(0,1)
            if state == 1 and num <= Common.pAttack:
                state = 0
                health = min(health+1,4)
                arrow = 0
            else:
                num = random.uniform(0,1)
                if num<=Centre.pBlade:
                    health = max(health+Common.bladeDamage,0)
                if state==0:
                    num = random.uniform(0,1)
                    if num<=Common.pReady:
                        state =1
    elif pos == 1:
        num = random.uniform(0,1)
        if state ==1 and num<=Common.pAttack:
            state = 0
            health = min(health+1,4)
            state = 0
        else:
            if action == "Left":
                num = random.uniform(0,1)
                if num<=East.pMove:
                    pos = 0
            elif action == "Shoot":
                num = random.uniform(0,1)
                arrow = max(arrow-1,0)
                if num<=East.pShoot:
                    health = max(health+shootDamage,0)
            elif action == "Hit":
                num = random.uniform(0,1)
                if num<=East.pBlade:
                    health = max(health+Common.bladeDamage,0)
            if state==0:
                num = random.uniform(0,1)
                if num<=Common.pReady:
                    state=1
    elif pos == 2:
        num  = random.uniform(0,1)
        if state==1:
            if num<=Common.pAttack:
                state = 0
               
            else:
                num =random.uniform(0,1)
                if action == "Stay":
                    if num>West.pMove:
                        pos = 1
                elif action == "Right":
                    if num<=West.pMove:
                        pos = 0
                    else:
                        pos = 1
                elif action == "Shoot":
                    arrow = max(arrow-1,0)
                    if num<=West.pShoot:
                        health = max(health+shootDamage ,0)
                num = random.uniform(0,1)

        else:
            if num<=Common.pReady:
                state = 1
            num =random.uniform(0,1)
            if action == "Stay":
                if num>West.pMove:
                    pos = 1
            elif action == "Right":
                if num<=West.pMove:
                    pos = 0
                else:
                    pos = 1
            elif action == "Shoot":
                arrow = max(arrow-1,0)
                if num<=West.pShoot:
                    health = max(health+shootDamage ,0)
            num = random.uniform(0,1)

    elif pos == 3:
        num = random.uniform(0,1)
        if state == 1:
            if num<=Common.pAttack:
                state = 0
               
            else:
                num = random.uniform(0,1)
                if action == "Stay":
                    if num>North.pMove:
                        pos = 1
                elif action == "Down":
                    if num<=North.pMove:
                        pos = 0
                    else:
                        pos = 1
                elif action == "Craft":
                    mat = max(mat-1,0)
                    if num<=pOneArrow:
                        arrow = min(arrow+1,3)
                    elif num<=pTwoArrow:
                        arrow = min(arrow+2,3)
                    else:
                        arrow = min(arrow+3,3)
                num = random.uniform(0,1)
        else:
            if num<=Common.pReady:
                state = 1
            num = random.uniform(0,1)
            if action == "Stay":
                if num>North.pMove:
                    pos = 1
            elif action == "Down":
                if num<=North.pMove:
                    pos = 0
                else:
                    pos = 1
            elif action == "Craft":
                mat = max(mat-1,0)
                if num<=pOneArrow:
                    arrow = min(arrow+1,3)
                elif num<=pTwoArrow:
                    arrow = min(arrow+2,3)
                else:
                    arrow = min(arrow+3,3)
            num = random.uniform(0,1)
    else:
        num = random.uniform(0,1)
        if state == 1:
            if num<=Common.pAttack:
                state = 0
          
            else:
                num = random.uniform(0,1)
                if action == "Stay":
                    if num>South.pMove:
                        pos = 1
                elif action == "Up":
                    if num<=South.pMove:
                        pos = 0
                    else:
                        pos = 1
                elif action == "Gather":
                    if num<=South.pGainMat:
                        mat = min(mat+1,2)
                num = random.uniform(0,1)

        else:
            if num<=Common.pReady:
                state = 1
            num = random.uniform(0,1)
            if action == "Stay":
                if num>South.pMove:
                    pos = 1
            elif action == "Up":
                if num<=South.pMove:
                    pos = 0
                else:
                    pos = 1
            elif action == "Gather":
                if num<=South.pGainMat:
                    mat = min(mat+1,2)
            num = random.uniform(0,1)
    try:
        findPolicy(bestAction , pos , mat, arrow, state , health)
    except RuntimeError as re:
        if re.args[0] != 'maximum recursion depth exceeded':
            raise
        print('Sorry but we cannot evaluate continue the policy because of the recursion delth limit, One possible reason could be repetition of a pattern of states again and again without reaching end state.')
