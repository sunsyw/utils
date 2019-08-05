a = 'abcdabcdababcdcdabcd'
b = 'abcd'

import re

# ret = re.findall(r'abcd','abcdabcd')
ret = re.findall(b,a)
print(len(ret))