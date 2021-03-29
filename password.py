a = 3
while a > 0 :
    password = input("請輸入密碼:")
    if password == "123456" :
        print("登入成功")
        break
    else :
        a = a - 1
        print("密碼錯誤 剩餘", a , "次")