"""
Module: product_manager.py
Chức năng:
- Quản lý danh sách sản phẩm
- Thêm, sửa, xóa, tìm kiếm
- Lưu và tải dữ liệu từ file JSON
"""

import json

FILE_NAME = "products.json"

# ------------------ FILE ------------------
def load_data():# Ham doc du lieu tu file JSON
    """Đọc dữ liệu từ file JSON"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(products):#hàm  lưu dữ liệu vào file
    """Lưu danh sách sản phẩm vào file JSON"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

# ------------------ CORE ------------------
def generate_id(products): # hàm tạo mã sản phẩm tự động
    """Tự động tạo mã sản phẩm"""
    if not products:
        return "LT01"
    max_id = 0
    for p in products:
        if p["id"].startswith("LT"):
            try:
                pid = int(p["id"][2:])
                if pid > max_id: max_id = pid
            except ValueError: continue
    return f"LT{max_id + 1:02d}"

def add_product(products): # hàm thêm sản phẩm 
    print("\n➕ THÊM SẢN PHẨM")
    name = input("Tên sản phẩm: ")
    brand = input("Thương hiệu: ")
    price = int(input("Giá: "))
    quantity = int(input("Số lượng: "))
    
    while True:
        try:
            price = int(input("Giá: "))
            quantity = int(input("Số lượng: "))
            break
        except ValueError:
            print("❌ Vui lòng nhập số cho Giá và Số lượng!")

    product = {
        "id": generate_id(products),
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("✅ Thêm thành công!")
    return products

def update_product(products):# hàm sửa sản phẩm
    print("\n✏️ CẬP NHẬT SẢN PHẨM")
    pid = input("Nhập mã sản phẩm: ")

    for p in products:
        if p["id"].lower() == pid.lower():
            print("Nhấn Enter để giữ nguyên")
            p["name"] = input(f"Tên ({p['name']}): ") or p["name"]
            p["brand"] = input(f"Thương hiệu ({p['brand']}): ") or p["brand"]

            price = input(f"Giá ({p['price']}): ")
            quantity = input(f"Số lượng ({p['quantity']}): ")

            if price:
                p["price"] = int(price)
                try:
                    p["price"] = int(price)
                except ValueError: print("❌ Giá không hợp lệ, giữ nguyên.")
            if quantity:
                p["quantity"] = int(quantity)
                try:
                    p["quantity"] = int(quantity)
                except ValueError: print("❌ Số lượng không hợp lệ, giữ nguyên.")

            print("✅ Cập nhật thành công!")
            return products

    print("❌ Không tìm thấy sản phẩm!")
    return products

def delete_product(products): # hàm xóa sản phẩm
    print("\n🗑️ XÓA SẢN PHẨM")
    pid = input("Nhập mã sản phẩm: ")

    for p in products:
        if p["id"].lower() == pid.lower():
            products.remove(p)
            print("✅ Đã xóa!")
            return products

    print("❌ Không tìm thấy sản phẩm!")
    return products

def search_product_by_name(products): # # Toi uu ham tim kiem
    print("\n🔍 TÌM KIẾM")
    keyword = input("Nhập từ khóa: ").lower()#(Dùng .lower() để tìm ko phân biệt hoa thường)

    found = False
    for p in products:
        if keyword in p["name"].lower():
            print(p)
            found = True

    if not found:
    results = [p for p in products if keyword in p["name"].lower()]
    
    if results:
        display_all_products(results)
    else:
        print("❌ Không tìm thấy sản phẩm!")

def display_all_products(products): # hàm hiển thị tất cả sản phẩm
    print("\n📦 DANH SÁCH SẢN PHẨM")
    if not products:
        print("Kho hàng trống.")
        return

    print("-" * 60)
    print("-" * 70)
    print(f"{'ID':<6} | {'Tên sản phẩm':<20} | {'Thương hiệu':<12} | {'Giá':>10} | {'SL':>4}")
    print("-" * 70)
    for p in products:
        print(f"{p['id']} | {p['name']} | {p['brand']} | {p['price']} | SL: {p['quantity']}")
    print("-" * 60)
        print(f"{p['id']:<6} | {p['name']:<20} | {p['brand']:<12} | {p['price']:>10,} | {p['quantity']:>4}")
    print("-" * 70)

def search_product_by_name(products): # # Toi uu ham tim kiem
    print("\n🔍 TÌM KIẾM")
    keyword = input("Nhập từ khóa: ").lower()#(Dùng .lower() để tìm ko phân biệt hoa thường)

    found = False
    for p in products:
        if keyword in p["name"].lower():
            print(p)
            found = True

    if not found:
    results = [p for p in products if keyword in p["name"].lower()]
    
    if results:
        display_all_products(results)
    else:
        print("❌ Không tìm thấy sản phẩm!")

def display_all_products(products): # hàm hiển thị tất cả sản phẩm
    print("\n📦 DANH SÁCH SẢN PHẨM")
    if not products:
        print("Kho hàng trống.")
        return

    print("-" * 60)
    print("-" * 70)
    print(f"{'ID':<6} | {'Tên sản phẩm':<20} | {'Thương hiệu':<12} | {'Giá':>10} | {'SL':>4}")
    print("-" * 70)
    for p in products:
        print(f"{p['id']} | {p['name']} | {p['brand']} | {p['price']} | SL: {p['quantity']}")
    print("-" * 60)
        print(f"{p['id']:<6} | {p['name']:<20} | {p['brand']:<12} | {p['price']:>10,} | {p['quantity']:>4}")
    print("-" * 70)
