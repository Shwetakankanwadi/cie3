import sys

if len(sys.argv) >=3:
    name="xyz"
    marks=[float(m)for m in sys.argv[2]]
    
else:
    name="xyz"
    marks=[45,50,65]
    
    average=sum(marks)/len(marks)

    print("student name:",name)
    print("Internal test marks:",marks)
    print("average internal score:",round(average,2))
  
