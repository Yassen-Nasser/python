# design full calclator function 
'''
اعمل اله حاسبة عبارة عن فنكشن بتاخد 
رقمين والعملية وبترجع النتيجة ف متغير 
وبعد كدا اطبع النتيجة على الشاشة 

ملحوظة  اعمل  : +,* فقط

'''
def sum(number1,number2,yy):
    if yy=="+":
        return  number1+number2
    elif  yy =="*":
        return number1*number2
    else: 
        print('error')
    
#y0y= sum(9,8,"+")
#print( str(y0y))


'''
def calclator(number1, number2, operation):
    # [+, - , *, /]
    if(operation =='+'):
        return number1 + number2

    elif (operation== '-'):
        return number1 - number2
    
    elif(operation=='*'):
        return number1 * number2

    elif(operation=='/'):
        return number1 / number2
    else:
        print('wrong input please check again ')

result = calclator(2, 2 , '-')
print('result is: '+str(result))
'''

'''
wake_up_early = False

if wake_up_early:
    print("i will go to school")
else:
    print("i will watching tv ")
'''
def equality(value1,value2):
    if value1==value2:
        return 'equal'        
    elif value1!= value2:
        return 'not equal'
    

#result = equality('ali', 'ali')1
#print(result)
def  even_odd (number) :
    try:
        if number%2 >0:
            return "odd"
        elif number%2 ==0:
            return 'even'
    except:
        return 'wrong'
         
y0y=even_odd('fbg')
print(y0y)




















 














