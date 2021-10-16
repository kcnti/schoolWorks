import textwrap

def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width): #เริ่มจาก 0 จบที่ len ของ string โดยที่เพิ่มที่ละ max_width
        s += string[c:c+max_width] + "\n" #เพิ่ม string โดยระบุ index ที่ได้จาก for loop ไปที่่ตัวแปล s
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)