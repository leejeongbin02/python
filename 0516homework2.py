inFp = None
inList = []

inFp = open("C:\\Users\\MYCOM\\Desktop\\대학교 파일\\파이썬프로그래밍\\실습 파일\\FileTest\\data1.txt", "r", encoding="utf-8")
inList = inFp.readlines()
inFp.close()

for i in range(len(inList)):
    print("%d: %s" % (i + 1, inList[i]), end="")
