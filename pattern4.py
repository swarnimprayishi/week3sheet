n = 5  
for i in range(1, n + 1):
    odd_num = 1
    line_elements = []
    for j in range(i):
        if j % 2 == 0:
            line_elements.append(str(odd_num))
            odd_num = odd_num + 2
        else:
            line_elements.append('*')
    print(' '.join(line_elements))
  
  
# 1  
#1 *  
#1 * 3  
#1 * 3 *  
#1 * 3 * 5