"""
Cho nhập 1 số nguyên n, cho biết số lượng từng ký số có trong n. Lưu ý: chỉ in ra các ký số có xuất
hiện.
 Yêu cầu: sử dụng list để lưu biến đếm.
"""
n = eval(input("Nhap vao so can dem ki tu : "))
len1 = str(n)
count_0,count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9 = 0,0,0,0,0,0,0,0,0,0
list1 = [count_0,count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9]
for i in len1[::-1]:
    if i=="0":
        list1[0] +=1

print(list1[0])