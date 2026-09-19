# ໂປຣເຈັກ: ລະບົບຈັດການຂໍ້ມູນສະຕັອກລົດ (Car Inventory System)

# 1. ສ້າງຖານຂໍ້ມູນຈຳລອງໂດຍໃຊ້ List ທີ່ເກັບ Dictionary ຂອງລົດແຕ່ລະຄັນ
car_inventory = [
    {"id": "1", "brand": "Toyota", "model": "Hilux Revo", "price": 100000000},
    {"id": "2", "brand": "BYD", "model": "Atto ", "price": 150000000}
]

def show_menu():
    """Function ສະແດງເມນູຫຼັກ"""
    print("\n" + "="*30)
    print("🚗 ລະບົບຈັດການສະຕັອກລົດ 🚗")
    print("="*30)
    print("1. ເບິ່ງລາຍຊື່ລົດທັງໝົດ (Read)")
    print("2. ເພີ່ມລົດເຂົ້າສະຕັອກ (Create)")
    print("3. ອັບເດດລາຄາລົດ (Update)")
    print("4. ລຶບລົດອອກຈາກສະຕັອກ (Delete)")
    print("5. ອອກຈາກໂປຣແກຣມ")
    print("="*30)

def view_cars():
    """1. Function ເບິ່ງລາຍຊື່ລົດທັງໝົດ"""
    if not car_inventory:
        print("\n❌ ບໍ່ມີຂໍ້ມູນລົດໃນສະຕັອກໃນເວລານີ້.")
        return
    
    print("\n📋 ລາຍຊື່ລົດໃນສະຕັອກ:")
    for car in car_inventory:
        # ການນຳໃຊ້ f-string ເພື່ອຈັດຮູບແບບການສະແດງຜົນໃຫ້ສວຍງາມ
        print(f"🆔 ID: {car['id']} | 🚗 ຍີ່ຫໍ້: {car['brand']} | 📦 ລຸ້ນ: {car['model']} | 💰 ລາຄາ: {car['price']:,} ກີບ")

def add_car():
    """2. Function ເພີ່ມລົດໃໝ່"""
    print("\n➕ ເພີ່ມລົດໃໝ່:")
    car_id = input("ປ້ອນ ID ລົດ: ")
    
    # ກວດສອບບໍ່ໃຫ້ ID ຊ້ຳກັນ
    for car in car_inventory:
        if car['id'] == car_id:
            print("❌ ຂໍ້ອະໄພ: ID ນີ້ມີໃນລະບົບແລ້ວ!")
            return
            
    brand = input("ປ້ອນຍີ່ຫໍະລົດ: ")
    model = input("ປ້ອນລຸ້ນລົດ: ")
    try:
        price = int(input("ປ້ອນລາຄາ (ຕົວເລກ): "))
    except ValueError:
        print("❌ ຂໍ້ຜິດພາດ: ລາຄາຕ້ອງເປັນຕົວເລກເທົ່ານັ້ນ!")
        return

    # ສ້າງ Dictionary ໃໝ່ແລ້ວເອົາໄປຢັດໃສ່ List
    new_car = {"id": car_id, "brand": brand, "model": model, "price": price}
    car_inventory.append(new_car)
    print(f"🎉 ເພີ່ມລົດ {brand} {model} ເຂົ້າສະຕັອກສຳເລັດ!")

def update_car():
    """3. Function ອັບເດດລາຄາລົດ"""
    print("\n🔄 ອັບເດດລາຄາລົດ:")
    car_id = input("ປ້ອນ ID ລົດທີ່ຕ້ອງການແກ້ໄຂ: ")
    
    for car in car_inventory:
        if car['id'] == car_id:
            print(f"🚘 ລົດທີ່ເລືອກຄື: {car['brand']} {car['model']} (ລາຄາປະຈຸບັນ: {car['price']:,} ກີບ)")
            try:
                new_price = int(input("ປ້ອນລາຄາໃໝ່: "))
                car['price'] = new_price # ປ່ຽນຄ່າລາຄາໃນ Dictionary
                print(f"✅ ອັບເດດລາຄາລົດ ID {car_id} ສຳເລັດ!")
                return
            except ValueError:
                print("❌ ຂໍ້ຜິດພາດ: ລາຄາຕ້ອງເປັນຕົວເລກເທົ່ານັ້ນ!")
                return
                
    print("❌ ບໍ່ພົບ ID ລົດທີ່ທ່ານລະບຸ.")

def delete_car():
    """4. Function ລຶບລົດອອກ"""
    print("\n❌ ລຶບລົດອອກຈາກສະຕັອກ:")
    car_id = input("ປ້ອນ ID ລົດທີ່ຕ້ອງການລຶບ: ")
    
    for car in car_inventory:
        if car['id'] == car_id:
            car_inventory.remove(car) # ລຶບ Dictionary ອອກຈາກ List
            print(f"🗑️ ລຶບລົດ ID {car_id} ອອກຈາກລະບົບແລ້ວ.")
            return
            
    print("❌ ບໍ່ພົບ ID ລົດທີ່ທ່ານລະບຸ.")

# --- ລະບົບຫຼັກ (Main Loop) ---
while True:
    show_menu()
    choice = input("ເລືອກເມນູ (1-5): ")
    
    if choice == "1":
        view_cars()
    elif choice == "2":
        add_car()
    elif choice == "3":
        update_car()
    elif choice == "4":
        delete_car()
    elif choice == "5":
        print("\n👋 ຂອບໃຈທີ່ໃຊ້ບໍລິການ. ລາກ່ອນ!")
        break
    else:
        print("❌ ຕົວເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາເລືອກ 1 ຫາ 5 ເທົ່ານັ້ນ.")
