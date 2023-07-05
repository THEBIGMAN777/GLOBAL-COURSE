marks = [13342,3445,323,332]
max = 0 
min = marks[0]
for i in range(0,len(marks)):
    if(marks[i] > max):
        max = marks[i]
    if (marks[i] < min):
        min = marks[i]
print(max, min)
