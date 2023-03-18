while(True):
    str = input("> ")
    if '+' in str:
        a, b = str.split('+')
        print(float(a)+float(b))
    elif '-' in str:
        a, b = str.split('-')
        print(float(a)-float(b))
    elif '*' in str:
        a, b = str.split('*')
        print(float(a)*float(b))
    elif '/' in str:
        a, b = str.split('/')
        print(float(a)/float(b))
    elif str == "" :
        break
    else:
        print("error , just 4 main oprators(+-*/)")
       
