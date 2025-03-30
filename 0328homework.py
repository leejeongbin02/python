select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계:"))
if select == 1 :
    x = (input("***수식을 입력하세요 :"))
    m = eval(x)
    print("%s 결과는 %f 입니다." %(x, m))
elif select == 2 :
    num1 = int(input("***첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("***두 번째 숫자를 입력하세요 :"))
    total = 0
    for i in range (num1, num2+1) :
        total += i
    print("%d+...+%d는 %d입니다" %(num1, num2, total))
else :
    print("1과 2 중 입력해야 합니다.")
