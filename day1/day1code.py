import csv

data = []

with open('input.csv') as fp:
    reader = csv.reader(fp)
    for x in reader:
        data.append(int(x[0]))

answer = []

for x in range(len(data)):
    for y in range(len(data)):
        if data[x] == data[y]:
            break
        if data[x] + data[y] == 2020:
            temp = data[x], data[y]
            answer.append(temp)

print(answer[0][0] * answer[0][1])

# part2

answer2 = []
for x in range(len(data)):
    for y in range(len(data)):
        if data[x] == data[y]:
            break
        for j in range(len(data)):
            if data[x] == data[j] or data[y] == data[j]:
                break
            if data[x] + data[y] + data[j] == 2020:
                temp = data[x], data[y], data[j]
                answer2.append(temp)


print(answer2[0][0] * answer2[0][1] * answer2[0][2])
