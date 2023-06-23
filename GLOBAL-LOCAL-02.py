def spam():
    eggs = 37
    bacon() #biến local ở hàm bacon bị hủy trước khi được print ra, nên sẽ print ra là 37
    print(eggs)

def bacon(): #không sử dụng biến local của hàm này sang hàm khác được
    ham = 101
    eggs = 0 #tên biến có thể giống nhau ở các hàm khác nhau, nhưng độc lập

spam()
