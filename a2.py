try:
    num1,num2=eval(input("Enter two number,seperated by a coma:"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is error!!")
except SyntaxError:
    print("coma is missig.Enter numbers seperated by coma like this 1,2")   
except :
    print("Wrong Input")
else :
    print("No Exception")   
finally:
    print("This will execute no matter what")
    