def get_weather(temp):
    if (temp>20):
        return "Warm"
    else:
        return "Cold"
    
def add(a,b):
    return a+b

def divide(a,b):
    if (b==0):
        raise ValueError("cannot divide by zero")
    
    return a/b