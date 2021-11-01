from typing import Dict

item = {
    "sku": 12345,
    "name": "Michael",
    "min_stock": 10,
    "stock": 9
}

def main():
    is_order_required(item)
    print("done")

    show_tabbed(item)
    print("Donee")

    set_name(item)
    print("Doneee")

    if item['min_stock'] > item['stock']:
        new_stock = int(input("What is the new stock number? "))
        set_stock(item, new_stock)
        print("Done")
    else: 
        print("Stock up to date")

    change_op = int(input("What would you like to change new min stock to ? "))
    set_min_stock(item, change_op)
    print("Done")

def is_order_required(item: Dict) -> str:
    if item['min_stock'] > item['stock']: 
        print("False")
    else:
        print("True")

def show_tabbed(item: Dict) -> str:
    print("sku       name     min stock  stock")
    print("-----     -----     -----     -----")
    print(f"{item['sku']}     {item['name']}     {item['min_stock']}     {item['stock']}")

def set_name(item: Dict) -> str:
    str.isalnum(item['name'])

def set_stock(item: Dict, new_stock: int) -> int:
    item['stock'] == new_stock
    
def set_min_stock(item: Dict, change_op: int) -> int:
    item['min_stock'] == change_op


if __name__ == "__main__":
    main()
