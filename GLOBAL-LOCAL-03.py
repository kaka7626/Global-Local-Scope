def spam():
    global eggs #gán giá trị mới cho biến global ở trong hàm
    eggs = 'Chào' #biến local và global độc lập
    print(eggs) #biến global eggs có thể dùng được trong hàm nếu không có biến local

eggs = 7
spam()
print(eggs)