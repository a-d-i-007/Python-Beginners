s=input("Enter temperature in farenheit : ")
def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
print(convert(s))
