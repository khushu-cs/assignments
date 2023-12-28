def can_travel_circuit(gas, cost):
    n = len(gas)
    
    total_gas = 0
    current_gas = 0
    start_index = 0
    
    for i in range(n):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        
        # If at any station, the current gas becomes negative,
        # reset the starting station to the next station
        if current_gas < 0:
            start_index = i + 1
            current_gas = 0
    
    # If the total gas is non-negative, a solution exists
    if total_gas >= 0:
        return start_index
    else:
        return -1
   #Example of implementation. 
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
result = can_travel_circuit(gas, cost)
print(result)
