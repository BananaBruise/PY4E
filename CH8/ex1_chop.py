def chop(li) -> None:
    if len(li) == 0:
        return
    elif len(li) == 1:
        li.pop()
        return
    else:
        li.pop(0) #remove first
        li.pop()  #remove last
    
    return

def middle(li) -> list:
    if len(li) <= 2:
        return []
    
    return li[1:-1]

def bad_delete_head(t):
    t = t[1:]


l1 = ['a','b','c']
l2 = l1.copy()

print(l1)
print(l2)

chop(l1)
print(l1)

l2 = middle(l2)
print(l2)