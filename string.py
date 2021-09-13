#whattodo = 'Charlist'
whattodo = 'printString'

def string_methods(whatToDo,str1):
    ###############################################################
    #  count the character (lenght of the string)
    ###############################################################
    
    if(whatToDo =='Charlist'):
        count=0
        for char in str1:
            count +=1
        return count
    #################################################################
    # print String
    #################################################################
    elif(whatToDo =='printString'):
        return str1
    else:
        print('try again')

#greeting ='Hello World'
#print(string_methods('Charlist',greeting))
#print(string_methods('printString',greeting))


    
def letterCase(str1,letterCase):
    #################################################################
    # string uppercase
    #################################################################
    if(letterCase =='U'):
        return str1.upper()
    #################################################################
    # string lowerCase
    #################################################################

    elif(letterCase=='L'):
        return str1.lower()
    #################################################################
    # first letter Capitalize
    #################################################################
    elif(letterCase=='C'):
        return str1.capitalize()
    #################################################################
    # txt = "Hello, And Welcome To My World!"
    # x = txt.casefold()
    #################################################################
    elif(letterCase=='CF'):
        return str1.casefold()
    else:
        return letterCase

print(letterCase(greeting,'L'))


stringtest = 'hello world'
print(stringtest[0])
print(stringtest[:])

##################################################string####
message ='Hello World'
message1 ='Bobby\'s world'
print(message)

multipleText ="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. """

singleText = 'hello world'
print(len(singleText))
print(singleText[0])  //H
print(singleText[10])
print(singleText.lower())
print(singleText.count('Hello')
print(singleText.count('l')
print(singleText.find('World')
new_message = singleText.replace('World','Universe')
print(new_message)
print(singleText)
###########################
greeting = 'Hello'
name ='Michael'
message = greeting+ ' '+name
print(message)
message ='{},{}'.format(greeting,name)
print(message)

message= f'{greeting},{name}.'
message= f'{greeting},{name.upper()}.'
print(message)

print(dir(name))  

print(help(str)) 

# for more info about string  https://www.w3schools.com/python/python_strings.asp


##############################################


"""
def findWord(txt,param1):
    return txt.find(param1)

def replaceString(txt,param1):
     new_message = txt.replace(txt,param1)tru
     return mew_message
    
def wordfindAndReplace(w='unknow',txt,param1):
    if w is 'f':
      return  findWord(txt,param1)
    elif w is 'r'
      new_message = replaceString(txt,param1)
      return mew_message
    else:
         return 'hello'

txt ='Hello world'
param1 = 'world'

       
print(wordfindAndReplace('f',txt,param1))
"""
