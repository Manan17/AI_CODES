import random
positions=[]
for i in range(8):
    positions.append(random.randint(0,7))

def cost(state):
    cost=0
    for i in range(len(state)):
        for j in range(i+1,len(state)):
            if state[i] == state[j]:
                cost +=1
            elif abs(i-j) == abs(state[i]-state[j]):
                cost+=1

    return cost

def get_new_state(state):
    queen = random.randint(0,7)
    position = random.randint(0,7)
    newState = state.copy()
    newState[queen] = position
    return newState
   

def hill_climbing(state,maxIterations=1000):
    curr = state
    for i in range(maxIterations):
        newState = get_new_state(curr)
        if cost(newState) < cost(curr):
            curr = newState

    return curr

ans = hill_climbing(positions)
print(ans)
print(cost(ans))
