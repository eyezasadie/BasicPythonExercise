#สร้างฟังก์ชั่นหาผลรวมของเบอร์โทร
def sum_phone_digit(phone_number):

    total = 0
    for c in phone:
        total += int(c)
    return total

#สรา้งฟังก์ชั่นทำนายผลของเบอร์
def interpret(number):

#รับค่าเบอร์
#phone = input("enter your phone number") #string
#print("Sum of Phone Number is", total)

#เขียนเงื่อนไขตรวจสอบกับข้มอูลหมายเลขใน list
    if number in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
        print('ดีมาก')
    elif number in (69, 79):
        print('โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข')
    elif number in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
        print('ดีปานกลาง')
    elif number in (62, 66, 68, 74, 75):
        print('เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม')
    elif number in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
        print('เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น')
    else:
        print("ไม่พบข้อมูล")


phone = input("enter your phone number") #string
print(interpret(sum_phone_digit(phone)))

