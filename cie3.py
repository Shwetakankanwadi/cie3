import sys

if len(sys.argv) >= 3:
    name = sys.argv[1]
    marks = [float(m) for m in sys.argv[2:]]  
else:
    name = "shweta"
    marks = [45, 50, 65]

average=sum(marks)/len(marks)

print("student name:", name)
print("Internal test marks:",marks)
print("average internal score:",round(average, 2))
