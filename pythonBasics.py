import re

txt = 'The rain in Spain'
x = re.findall('\AThe', txt)
print(x)