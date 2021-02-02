"""
Có 9 loại tiền 1, 2, 5, 10, 20, 50, 100, 200, 500. Cho nhập số tiền X.
 Chuyển số tiền X ra các loại tiền
sao cho số lượng là ít nhất. In ra số tờ tiền của mỗi loại
"""
def doi_tien(so_tien):
    list1 = [500,200,100,50,20,10,5,2,1]
    for i in list1 :
        a = so_tien//i
        print("loai %i gom %i to " %(i,a))
        so_tien = so_tien - a*i
    return
try:
    x = eval(input("Nhap vao so tien ban muon chuyen doi : "))
    doi_tien(x)
except NameError as nr:
    nr = "Tien nhap phai o dang so "
    print("Error :",nr)