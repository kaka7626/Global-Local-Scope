def spam(): #các biến local sẽ xuất hiện khi hàm được gọi, sẽ bị hủy khi hàm dược trả về
    eggs = 37 #đây là biến local trong hàm, không thể sử dụng bên ngoài hàm (global)

spam()
print(eggs) #lỗi vì local không dùng được ở global, nhưng global dùng được ở trong local