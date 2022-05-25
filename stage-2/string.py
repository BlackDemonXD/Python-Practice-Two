message = "GNU/Linux's world"                      #Avoiding collision by using double quotes
new_message = message.replace('World', 'Universe') #Replacing World with Universe
print('message')                                   #Printing message in the message variable
print(len(message))                                #Length of the variable message
print(message[0])                                  #Print the 0 numbered character of the message variable
print(message[0:5])                                #Print from the 0 to the 4th (does NOT include the 5th variable) from the message varaible
print(message[:5])                                 #With the same message, leaving the first parenthesis as blank before colon assumes it starts from the beginning, ie- 0
print(message[5:])                                 #Again if we take the first parenthesis as 5 and the area after colon as blank, it will assume to display variables till the end
print(message.lower())                             #Prints the content of message in lowercase
print(message.upper())                             #Prints the content of message in uppercase
print(message.count('l'))                          #Prints the counter of characters in the message

Greeting = 'Hello'
Name = 'Michael'
message = Greeting+', '+Name+'. Welcome!'          #Prints A whole message string
print(message)

message= '{}, {}. Welcome!' .format(Greeting, Name)#Print message using string formatting
print(message)

message= f'{Greeting}, {Name}. Welcome!'           #Print message using fstring formatting
print(message)

print(dir(Name))                                   #Shows all attributes we have access to with that specific variable
print(help(str))                                   #Prints string help
print(help(str.lower))                             #Prints help of the String 'lower'
