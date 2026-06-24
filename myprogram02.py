# โค้ดเวอร์ชันใหม่ของฉัน
# พัฒนาจากต้นแบบ โดย: นายณภัทร จริงดี ม.6/10 เลขที่ 6

def calculate_rectangle():
    try:
        width = float(input("กรอกความกว้าง (ซม.): "))
        length = float(input("กรอกความยาว (ซม.): "))
        if width <= 0 or length <= 0:
            print("❌ ข้อผิดพลาด: ค่าความกว้างและความยาวต้องมากกว่า 0")
            return
        area = width * length
        print(f"📐 พื้นที่สี่เหลี่ยมมุมฉากคือ: {area:.2f} ตารางเซนติเมตร")
    except ValueError:
        print("❌ ข้อผิดพลาด: กรุณากรอกเป็นตัวเลขเท่านั้น")

def calculate_triangle():
    try:
        base = float(input("กรอกความยาวฐาน (ซม.): "))
        height = float(input("กรอกความสูง (ซม.): "))
        if base <= 0 or height <= 0:
            print("❌ ข้อผิดพลาด: ค่าฐานและความสูงต้องมากกว่า 0")
            return
        area = 0.5 * base * height
        print(f"📐 พื้นที่สามเหลี่ยมคือ: {area:.2f} ตารางเซนติเมตร")
    except ValueError:
        print("❌ ข้อผิดพลาด: กรุณากรอกเป็นตัวเลขเท่านั้น")

def main():
    while True:
        print("\n=== โปรแกรมคำนวณพื้นที่เรขาคณิต (เวอร์ชันอัปเกรด) ===")
        print("1. คำนวณพื้นที่สี่เหลี่ยมมุมฉาก")
        print("2. คำนวณพื้นที่สามเหลี่ยม")
        print("3. ออกจากโปรแกรม")
        
        choice = input("เลือกเมนู (1-3): ")
        
        if choice == '1':
            calculate_rectangle()
        elif choice == '2':
            calculate_triangle()
        elif choice == '3':
            print("ขอบคุณที่ใช้งานโปรแกรม! สวัสดีครับ")
            break
        else:
            print("❌ กรุณาเลือกเมนูให้ถูกต้อง (1-3)")

if __name__ == "__main__":
    main()