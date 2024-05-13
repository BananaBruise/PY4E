import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about metting @2PM'
lst = re.findall('\w+@\w+.\w+', s)
print(lst)