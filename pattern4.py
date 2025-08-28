line = ''
num = 1
for i in range(1, 6):
    if i % 2 == 0:
        line = line +'*'
    else:
        line =  line  + str(num)
        num = num + 2
    print(line)
  
  
# 1  
#1 *  
#1 * 3  
#1 * 3 *  

#1 * 3 * 5
