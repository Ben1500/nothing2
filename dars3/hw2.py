def function(son):
    son_str = str(son) 
    reversed_str = son_str[::-1] 
    reversed_number = int(reversed_str)  
    if reversed_number == son:
        return True
    else:
        return False

print(function(131))