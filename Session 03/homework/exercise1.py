# break là một câu lệnh có thể nằm trong 1 khối (block) lệnh của 1 vòng lăp
# Đây là lệnh kết thúc vòng lặp vô điều kiện
# Xem xét ví dụ sau đây
# Tạo biến x và gán cho nó giá trị bằng 2
x = 2

while(x<15):
    print('------------------\n')
    print('x= ',x)

    # Kiểm tra nếu x = 10 thì thoát khỏi vòng lăp
    if (x==10):
        break

    # Tăng giá trị của x thêm 1 đơn vị
    x = x+1
    print('x after +1 = ',x)
print('End of example')
