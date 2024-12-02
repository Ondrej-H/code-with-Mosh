
def increment(number, by=1):  # we give the second parameter (by) the default value (by=1) -->
    return number + by        # --> every required parameter (here number) must go before all optional parameters 


#print(increment(2, by=1))      # beacause we don't want to type everytime by=1
# now, the second argument is optional - if we don't give any second argument, it's default # now, the second argument is voluntary - if we don't give anysecond argument, it's default 1:
print(increment(2))

# but we still can give the second argument to the function:
print(increment(2, 5))