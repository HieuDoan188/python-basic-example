"""
Yêu cầu : Viết chương trình xử lý list như sau
 Tạo ra một list dùng để chứa các phần tử kiểu chuỗi
 Cho phép người dùng lần lượt nhập các phần tử kiểu chuỗi cho list cho đến khi không muốn
nhập nữa
 In list vừa nhập.
 In thông tin của từng phần tử trong chuỗi: mỗi phần tử in 2 thông tin là nội dung và chiều
dài của chuỗi theo mẫu (nội dung : chiều dài)
 Hãy cho biết phần tử nào chứa chuỗi có độ dài dài nhất, in vị trí và giá trị của phần tử này theo
mẫu (vị trí : nội dung : chiều dài)
 Cho người dùng nhập vào một chuỗi. Hãy cho biết có phần tử nào trong list có giá trịgiống
với chuỗi đã nhập hay không? Nếu có thì cho biết ở vị trí nào (tính từ 0 -> chiều dài -1). Nếu
không thì thông báo là “Không có phần tử nào giống ...”
 Sắp xếp các phần tử trong list theo thứ tự tăng dần theo Alphabet.
"""

list1 = []
list2 = []
try:
    while 1 > 0 :
        ptu = input("Nhap vao phan tu ban muon them vao list : ")
        select = eval(input("Tiếp tục nhập giá trị ? 1 : có , 0 : Không "))
        if select == 0 :
            break
        list1.append(ptu)

    print("List bạn vừa nhâp là : ", list1)
    for i in list1 :
        print("Nội dung là : " ,i , ": với độ dài chuỗi :", len(i))
        list2.append(len(i))
    max1 = max(list2)
    print("phan tu dai nhat voi so ki tu la : ",max1)

    string_find = input("Nhập vào giá trị bạn muốn tìm kiếm : ")
    if string_find in list1 :
        print("Vị trí có giá trị ",string_find,"cần tìm là : ",list1.index(string_find))
    else :
        print("Không có giá trị bạn muốn tìm trong list !")

    print("list sau khi sắp xếp ",sorted(list1))

except NameError as nr:
    nr = "Bạn nhập không phải là số 1 hoặc 0"
    print("Error : ",nr)