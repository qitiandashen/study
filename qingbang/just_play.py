'''for i in range(1,10):
   string = ""
   for j in range(1,i+1):
       string +=str(j) + " * "+str(i) + " = " +str(i*j)+"\t"
       print(string)'''
python_l=['lcg','szw','zjw']
linux_l=['lcg','szw']

python_and_linux_l=[]
for p_name in python_l:
    if p_name in linux_l:
        python_and_linux_l.append(p_name)

print(python_and_linux_l)
