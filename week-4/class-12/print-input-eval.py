## Printing
import datetime
from xmlrpc.client import DateTime

h = datetime.datetime.now()
print('Let\'s calculate Celsius degrees in Fahrenheit. Now the time is', h.hour, 'hours', sep='/', end='.\n')

## Inputting

name = input('What\'s your name?')

## Eval

print(type(eval('3')))

## Activity

question = 'Hello ' + name + ', please type the degree in Celsius'
c = input(question)
c_temp = eval(c)
f = 1.8 * c_temp + 32
print('Degrees in Fahrenheit:', f)