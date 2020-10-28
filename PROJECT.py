#递归案例题
def age(num,a):
    if num ==1:     #定义条件
        print (a)
    else:
        num-=1      #对值重新赋值
        a+=2        
        age(num,a)  #对函数进行递归
age(5,10)       #函数调用，也可理解为递归函数是从这里开始
