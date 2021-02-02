from module_chuyen_doi_dv import cm_foot,cm_inch,foot_cm,foot_inch,inch_cm,inch_foot

print("CHƯƠNG TRÌNH CHUYỂN ĐỔI GIỮA 3 ĐƠN VỊ cm,inch va foot")
list1 = ["1- Từ cm sang inch","2- Từ cm sang foot","3- Từ inch sang cm","4- Từ inch sang foot",
"5- Từ foot sang cm","6- Từ foot sang inch","0- Kết thúc chương trình"]
for i in list1 :
    print(i)
try:
    while 1>0:
        select = eval(input("Bạn chọn chức năng (0-6) : "))
        if select == 1 :
            x = eval(input("Nhap vao so cm can chuyen doi sang inch : "))
            cm_inch(x)
            break
        elif select == 2 :
            x = eval(input("Nhap vao so cm can chuyen doi sang foot : "))
            cm_foot(x)
            break
        elif select == 3 :
            x = eval(input("Nhap vao so inch can chuyen doi sang cm : "))
            inch_cm(x)
            break
        elif select == 4 :
            x = eval(input("Nhap vao so inch can chuyen doi sang foot : "))
            inch_foot(x)
            break
        elif select == 5 :
            x = eval(input("Nhap vao so foot can chuyen doi sang cm : "))
            foot_cm(x)
            break
        elif select == 6 :
            x = eval(input("Nhap vao so foot can chuyen doi sang inch : "))
            foot_inch(x)
            break
        elif select == 0 :
            print("Ket thuc chuong trinh")
            break
        else :
            print("Chuc nang ban chon khong co ! Vui long chon lai ")
except NameError as nr:
    nr = "Bạn nhập không phải là số "
    print("Error : ",nr)