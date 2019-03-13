# re regular expression
# findall(rule, target, flag)
# functional letters

# .*?+|$\
# rules range: (){}[]

# [''] -- a collection of letters
# to match anyone inside the bracket
# [abc123] - match with a,b,c,1,2,3

# 无捕获组 ‘(?: )’

# ‘^’和’$’ 匹配字符串开头和结尾


# 匹配字符串的开头。它和’^’的区别是，’\A’只匹配整个字符串的开头，
# 即使在’M’模式下，它也不会匹配其它行的行首。
import re
s = '123\nh56\n789 66'
res = re.findall(r'\d+\Z', s, re.M)
print(res)