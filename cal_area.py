import math

def area_rectangle(width, height):
    """คำนวณพื้นที่สี่เหลี่ยมผืนผ้า"""
    return width * height

def area_circle(radius):
    """คำนวนพื้นที่วงกลม"""
    return math.pi * radius ** 2

def area_triangle(base, height):
    """คำนวนพื้นที่สามเหลี่ยม"""
    return 0.5 * base * height

def main():
    print("โปรแกรมหาพื้นที่ของรูปทรงต่าง ๆ")
    print("1. พื้นที่สี่เหลี่ยมผืนผ้า")
    print("2. พื้นที่วงกลม")
    print("3. พื้นที่สามเหลี่ยม")
    
    choice = int(input("เลือกตัวเลือก (1/2/3): "))
    
    if choice == 1:
        width = float(input("ป้อนความกว้าง: "))
        height = float(input("ป้อนความยาว: "))
        print(f"พื้นที่สี่เหลี่ยมผืนผ้า = {area_rectangle(width, height):.2f}")
    elif choice == 2:
        radius = float(input("ป้อนรัศมี: "))
        print(f"พื้นที่วงกลม = {area_circle(radius):.2f}")
    elif choice == 3:
        base = float(input("ป้อนความยาวฐาน: "))
        height = float(input("ป้อนความสูง: "))
        print(f"พื้นที่สามเหลี่ยม = {area_triangle(base, height):.2f}")
    else:
        print("ตัวเลือกไม่ถูกต้อง!")

if __name__ == "__main__":
    main()  