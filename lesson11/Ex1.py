x = 10 #(Global Variable)

def test():
    x = 20   #(Local Variable)
    print(x) #20

test()
print(x) # يطبع 10 لأن المتغير العالمي لم يتغير