# สร้างลิสต์สำหรับเลขคี่และเลขคู่
odd_numbers = []    # เลขคี่
even_numbers = []   # เลขคู่

# วนลูปตั้งแต่เลข 21 ถึง 40
for number in range(21, 41):
    if number % 2 == 0: # สูตร [number%2 == 0] = เลขคู่, [number%2 != 0] = เลขคี่
        # ถ้าเป็นเลขคู่ให้เพิ่มเข้าไปในลิสต์ even_numbers
        even_numbers.append(number)
    else:
        # ถ้าเป็นเลขคี่ให้เพิ่มเข้าไปในลิสต์ odd_numbers
        odd_numbers.append(number)

# แสดงผลลัพธ์
print("เลขคี่:", odd_numbers)
print("เลขคู่:", even_numbers)
