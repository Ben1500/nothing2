def function(element,list1):
    new=list(list1)
    b=[]
    a=0
    for i in new:
        a+=1
        if i==element:
            b.append(a)
    return f"{element} {b} indexlarda joylashgan."
list2="alkhh mnakkj"
print(function("a",list2))
      



