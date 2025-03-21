jinsoo = int(input("입력 진수 결정(16/10/8/2):"))
num = input("값 입력 :")

num1 = int(num, jinsoo)

print("16진수 ==>", hex(num1))
print("10진수 ==>", num1)
print("8진수 ==>", oct(num1))
print("2진수 ==>", bin(num1)) 