# strip: default to remove space from start and end of string
name = "      han tu         "
print(name.strip())

# strip: remomve combination of character from start and end of string
comment = "/------ here lies wisdom ------/"
print(comment.strip('/- '))
print(comment) # does not modify original

# replace: old substring with new
buf = 'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo'
print(buf.lower().replace('buffalo', 'giraffe'))

# optional: replace first # of substrings
print(buf.lower().replace('buffalo', 'giraffe',3))



