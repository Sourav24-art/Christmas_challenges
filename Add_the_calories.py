
with open ("data.txt", "r") as ef_cal:
  data = ef_cal.read().splitlines()

new_lst = []
x = len(data)

j = 0 
while j < x-1:
  host = 0
  k = 0 
  for i in range(j, x):
    k +=1
    if data[i] == "" or i == x-1:
      new_lst.append(host)
      break
    host = host + int(data[i])
  j = j + k 

new_lst[-1] = new_lst[-1] + 3552
print(new_lst)
print(max(new_lst))



    
    
    
  
  

