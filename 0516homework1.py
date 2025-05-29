inFp = None
inStr = ""

inFp = open("C:\\Users\\MYCOM\\Desktop\\대학교 파일\\파이썬프로그래밍\\실습 파일\\FileTest\\data1.txt", "r", encoding="utf-8")

line_num = 1
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (line_num, inStr), end="")
    line_num += 1

inFp.close()
