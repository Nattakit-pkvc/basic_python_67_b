"""
#
# Part : Python Comment (คอมแมนท์)
#
"""

# this is comment
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (s)

"""
v = s/t
v = ความเร็ว (m/s)
s = ระยะทาง (m)
t = เวลา (s)
"""

print("Hello world!!!")

x = 5  # Interger
y = "Hey Brus"  # String
print(x, y)

x = str(3)
y = int(5)
z = float(7)
print(type(x), type(y), type(z))


"""
#
# Part : Variables Names (การตั้งชื่อ)
#
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
my_var2 = "John"
# 2my_var = "John"; (ทำไม่ได้)
# my-vars = "John"; (ทำไม่ได้)
# my vars = "John"; (ทำไม่ได้)

# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
myvariableName = "John"

"""
#
# Part : Python String (ตัวอักษร)
#
"""
x = "Hey Brus"
print(x)

y = """
1 Hey Brus
2 Hey Brus
3 Hey Brus
"""
print(y)

x = "Hey Brus"
print(x[2])
print(len(x))
print("Hey" in x)
print("What'sup" not in x)
print(x.upper())  # ตัวพิมพ์ใหญ่
print(x.lower())  # ตัวพิมพ์เล็ก

print(x.replace("Brus", "Sis"))  # แทนที่
print(x.split(" "))  # แยกคำ


a = "Apple"
b = "Company"
print(a+" "+b)

price = 20
word = f"Price: {price:.2f}"
print(word)

