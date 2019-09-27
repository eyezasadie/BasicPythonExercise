#การสร้าง function
def hello(name):
    print("Hello %s" %name)

#การสร้าง Function ที่มีการคืนค่า
def area(width=0,height=0):
    c = width * height
    return c


#การเรียกใช้ Function
hello("Aye")
#เรียกใช้ area
print(area(5,8))
print(area(15,2))
