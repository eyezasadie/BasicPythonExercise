#การสร้าง lists ใน python
numbers = [20,32,89,95,130]
names =["Jane","Abby","Bob"]
mixed =[-2,5,84.2,"M","P"]
#การแสดงข้อมูลใน list ลำดับแรก นับที่ลำดับที่ 0
print(numbers[0])
print(numbers[4])
print(names[2])
print(mixed[3])

#การวนลูปข้อมูลสมาชิกใน list
for num in numbers:
    print(num)
for name in names:
    print(name)
for mix in mixed:
    print(mix)

