class BackpackItem:
    def __init__(self, item_id, value):
        self.item_id = item_id
        self.value = value
        self.next = None
        self.prev = None


def input_item(item_id, value):
    new_item = BackpackItem(item_id, value)
    global head, tail, curr
    if head is None:
        head = tail = new_item
        head.prev = None
        tail.next = None
    else:
        curr = head
    while curr and curr.item_id != item_id:
        curr = curr.next
    if curr and curr.item_id == item_id:
        curr.value += value
    else:
        tail.next = new_item
        new_item.prev = tail
        tail = new_item
        tail.next = None


def del_all():
    global head, curr
    while head:
        curr = head
        head = head.next
        del curr


def del_head():
    global head, tail
    if head is None:
        print("Backpack empty!")
    else:
        if head == tail:
            del head
            del tail
        else:
            curr = head
            head = head.next
            del curr
            head.prev = None


def del_tail():
    global tail, head
    if tail is None:
        print("Backpack empty!")
    else:
        if head == tail:
            del head
            del tail
        else:
            curr = tail
            tail = tail.prev
            del curr
            tail.next = None


def del_select(item_id, item_amount):
    global head, tail, curr, count
    deleted = 0
    curr = head
    while curr and curr.item_id != item_id:
        curr = curr.next
    if curr and curr.item_id == item_id:
        if item_amount <= curr.value:
            deleted = item_amount
            curr.value -= item_amount
            count -= item_amount
            if curr.value == 0:
                if head == tail:
                    del head
                    del tail
                    head = None
                    tail = None
                elif curr == head:
                    del_head()
                elif curr == tail:
                    del_tail()
                else:
                    curr.prev.next = curr.next
                    del curr
                    deleted = item_amount
                    return deleted


def open_backpack(opened):
    global head, curr
    if opened:
        count = 1
        curr = head
        if head is None:
            print("Backpack is empty!")
            return
        print("No.\tItem Amount\t\tItem ID\n")
        while curr:
            print(f"{count}.\t{curr.value}\t\t\t{curr.item_id}\n")
            curr = curr.next
            count += 1


def open_backpack_reverse(opened):
    global tail, curr
    if opened:
        count = 1
        curr = tail
        if tail is None or head is None:
            print("Backpack is empty!")
            return
        print("No.\tItem Amount\t\tItem ID\n")
        while curr:
            print(f"{count}.\t{curr.value}\t\t\t{curr.item_id}\n")
            curr = curr.prev
            count += 1


def menu():
    print("1. Add Items")
    print("2. Open/Close Backpack")
    print("3. Delete Selected Item")
    print("4. Reverse Backpack List")
    print("5. Exit")


head = None
tail = None
curr = None
flag = False
count = 0
opened = False

while True:
    if count == 20:
        print("Backpack is full!")
    print("Backpack menu:")
    if not flag:
        open_backpack(opened)
    else:
        open_backpack_reverse(opened)
    print(f"Item in backpack: {count}\n")
    menu()
    input_choice = int(input("Input menu: "))

    if input_choice == 1:
        if count == 20:
            print("Backpack is full!")
            input("Press Enter to continue...")
            continue
        item_id = input("Input item ID: ").lower()
        item_amount = int(input("Input amount: "))
        count += item_amount
        if count > 20:
            print("Input failed! Backpack is full!")
            count -= item_amount
            input("Press Enter to continue...")
            continue
        input_item(item_id, item_amount)
        print("Item added!")
        input("Press Enter to continue...")

    elif input_choice == 2:
        opened = not opened

    elif input_choice == 3:
        if count == 0:
            print("Backpack is empty!")
        else:
            item_id = input("Input item ID: ").lower()
            item_amount = int(input("Input amount to del: "))
            del_status = del_select(item_id, item_amount)
            if del_status:
                count -= item_amount
                print("Item deleted!")
            else:
                print("Item not found!")
            input("Press Enter to continue...")

    elif input_choice == 4:
        flag = not flag

    elif input_choice == 5:
        break

    else:
        print("Invalid choice!")
        input("Press Enter to continue...")
