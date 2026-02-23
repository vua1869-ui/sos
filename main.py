"""
File: main.py
Chức năng:
- Hiển thị menu
- Nhận lựa chọn người dùng
- Gọi các hàm xử lý từ product_manager 
"""

from manager import *

def menu():
    print("\n====== POLY-LAP MANAGER ======")#dòng đầu tiên của menu
    print("1. Hiển thị sản phẩm")# # Update giao dien lan 1
    print("2. Thêm sản phẩm") #ahahahah
    print("3. Sửa sản phẩm") # sửa sản phẩm thì ấn số 3
    print("4. Xóa sản phẩm") # xóa sản phẩm thì ấn số 4
    print("5. Tìm theo tên") # tìm sản phẩm theo tên thì ấn số 5
    print("0. Thoát")
    print("=============================")

def main():
    products = load_data()

    while True:
        menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            display_all_products(products)
        elif choice == "2":
            products = add_product(products)
            save_data(products)
        elif choice == "3":
            products = update_product(products)
            save_data(products)
        elif choice == "4":
            products = delete_product(products)
            save_data(products)
        elif choice == "5":
            search_product_by_name(products)
        elif choice == "0":
            save_data(products)
            print("👋 Đã lưu và thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()# chốt
