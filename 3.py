# 1.加入例外處理
# 2.重複輸入,直到a=>exit 離開,使用while true

while True:
    try:
        a = input("請輸入a:")
        if a == "exit":
            print("離開程式")
            break
        a = eval(a)
        b = eval(input("請輸入b:"))
        if a > b:
            print(f"a比b大{a-b}")
        elif a < b:
            print(f"b比a大{b-a}")
        else:
            print("a跟b一樣大")
    except Exception as e:
        print(f"輸入錯誤,請重新輸入! ({e})")
print("程式結束")
