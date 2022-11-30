from collections import defaultdict
jug1=4
jug2=3
aim=2
visitedpair=defaultdict(lambda:False)

def WaterJugSolver(a1,a2):
    if((a1==0 and a2==aim) or (a2==0 and a1==aim)):
        print(a1,a2)
        return True
    
    if (visitedpair[(a1,a2)]):
        return False
    
    visitedpair[(a1,a2)]=True
    print(a1,a2)
    
    return (
        WaterJugSolver(0,a2) or
        WaterJugSolver(a1,0) or
        WaterJugSolver(jug1,a2) or
        WaterJugSolver(a1,jug2) or
        WaterJugSolver(a1+min(a2,jug1-a1),
                       a2-min(a2,jug1-a1)) or
        WaterJugSolver(a1-min(a1,jug2-a2),
                       a2+min(a1,jug2-a2))
    )




print("Steps:")
WaterJugSolver(0,0)