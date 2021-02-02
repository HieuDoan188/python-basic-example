"""
Quản lý thông tin nhân viên(2.5đ)
 Yêu cầu: Viết chương trình thực hiện việc quản lý thông tin nhân viên như sau:
 Tạo một danh sách nhân viên kiểu dictionary để lưu trữ thông tin các thông tin với key là mã
nhân viên, value bao gồm các thông tin : tên nhân viên, số điện thoại, lương.
Chương trình thực hiện các công việc sau:
 Nhậpthêm nhânviênmới.Chophépngườidùnglầnlượtnhậpcácphầntửchodanh sách cho
đến khi không muốn nhập nữa
 In danh sách nhân viên
 Cho phép người dùng tim kiếm theo mã nhân viên.
 Sắp xếp danh sách nhân viên theo tên nhân viên ( theo thứ tự alphabet)
"""

print("Nhập thông tin danh sách nhân viên :")
dict1 = {}
while 1>0:
    ma_nv = input("Nhập mã nhân viên : ")
    ten_nv = input("Nhập tên nhân viên : ")
    sdt_nv = input("Nhập số điện thoại nhân viên : ")
    luong_nv = eval(input("Nhập lương nhân viên : "))
    select = eval(input("Nhập giá trị tiếp không ? 1: Có , 0: Không "))
    dict1[ma_nv]=[ten_nv,sdt_nv,luong_nv]
    if select == 0 :
        break
print("DSNV",dict1)
print("*************************Danh sách nhân viên*************************")
print('Mã Nhân viên \t Họ và tên \t Số điện thoại \t Lương(VND)')
for key, value in dict1.items():
    print('{} \t\t {} \t\t {} \t {}'.format(key, value[0],value[1],value[2]))

while 1>0:
    find_nv = input("Nhập mã nhân viên cần tìm : ")
    if find_nv in dict1.keys():
        print("Thông tin nhân viên :\n",dict1[find_nv])
    else:
        print("Không tìm thấy nhân viên cần tìm !")
    select1 = eval(input("Bạn muốn tìm kiếm tiếp không ? 1: Có, 0: Không "))
    if select1 == 0:
        break

print("*************************Danh sách nhân viên sau khi sắp xếp*************************")
""" list_name = dict1.values[:][1]
sorted(list_name)
for key, value in dict1.items():
    print('{} \t\t {} \t\t {} \t {}'.format(key, value[0],value[1],value[2]))
"""