import random
initial_population = ['01010','10010','10101','11100']
values = []
fitness = []
probability=[]
expected_count=[]
sum = 0
for i in initial_population:
    values.append(int(i,2))

for i in values:
    fitness.append(int(i)*int(i))
    sum += (int(i)*int(i))

avg = sum/len(initial_population)

for i in fitness:
    probability.append(i/sum)

for i in fitness:
    expected_count.append(i/avg)

#print(values,fitness,expected_count)
minimum = min(expected_count)
maximum = max(expected_count)

indexOfMin = expected_count.index(minimum)
indexOfMax = expected_count.index(maximum)

initial_population[indexOfMin] = initial_population[indexOfMax]
values[indexOfMin] = values[indexOfMax]

print(initial_population)

for i in range(0,len(initial_population),2):
    r = random.randint(0,2)
    temp = initial_population[i][r:]
    temp2 = initial_population[i+1][r:]
    str1 = initial_population[i][0:r]
    str2 = initial_population[i+1][0:r]
    initial_population[i] = str1+temp2
    initial_population[i+1] = str2+temp

#mutation
#for i in initial_population:


print(initial_population)
