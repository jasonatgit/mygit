#核心思想：F(N) = F(N - 1) + F(N - 2) (N >= 2)

def fibonacci_list(n):
    if n == 1 or n == 2 :
        return 1
    else:
        m = fibonacci_list(n - 1) + fibonacci_list(n - 2)
    return m

try :
    n = int(input("please input a integer number:"))
except ValueError:
    print('please input a integer n(n > 0)!') 

list_num = [0]
temp = 1
while (temp <=n):
    list_num.append(fibonacci_list(temp))
    temp +=1
print(list_num)
