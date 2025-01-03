'''Створіть функцію, яка прийматиме масив несортованих чисел 
і поверне boolean значення залежно від того, чи можна із заданих значень скласти піфагорів трикутник 
з відповідними довжинами сторін.

Тести:
[5, 3, 4] -> True
[6, 8, 10] -> True
[100, 3, 65] -> False'''

test=[[5,3,4],[6,8,10],[100,3,65],[5,3],[5,3,'text'],[3,4,5.0],[5.0,3.0,4.0],[5.1,4.0,3.0]]


def triangle_pifagor(a,b,c):
    x,y,z =a**2,b**2,c**2
    if x+y==z or x+z==y or y+z==x:
        print(True)
    else:
        print(False)

def check_test_data(lent):
    g=0
    for item in lent:
        if isinstance(item, int) or isinstance(item, float): #check Integer
            g+=1
            if g==3 and len(lent)==3:
               g=0
               return True

def test_date(list_test):
    for i in test:#check lenght
        flag=check_test_data(i)
        if flag==True:
            a,b,c= i[0],i[1],i[2]
            triangle_pifagor(a,b,c)
        else:
            print('It is not triangle')

if __name__== "__main__":
    test_date(test)
