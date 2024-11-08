class SymbolTableNode:
    def __init__(self, label, addr):
        self.label = label
        self.addr = addr
        self.next = None

class SymbolTable:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert(self):
        label = input("Enter the label: ")
        if self.search(label):
            print("The label already exists. Duplicate cannot be inserted")
        else:
            addr = int(input("Enter the address: "))
            new_node = SymbolTableNode(label, addr)
            if self.size == 0:
                self.first = new_node
                self.last = new_node
            else:
                self.last.next = new_node
                self.last = new_node
            self.size += 1

    def display(self):
        print("LABEL\tADDRESS")
        current = self.first
        while current is not None:
            print(f"{current.label}\t{current.addr}")
            current = current.next

    def search(self, label):
        current = self.first
        while current is not None:
            if current.label == label:
                return True
            current = current.next
        return False

    def modify(self):
        choice = int(input("What do you want to modify?\n1. Only the label\n2. Only the address of a particular label\n3. Both the label and address\nEnter your choice: "))
        label = input("Enter the old label: ")

        if not self.search(label):
            print("No such label")
            return

        if choice == 1:
            new_label = input("Enter the new label: ")
            current = self.first
            while current is not None:
                if current.label == label:
                    current.label = new_label
                    break
                current = current.next
        elif choice == 2:
            new_addr = int(input("Enter the new address: "))
            current = self.first
            while current is not None:
                if current.label == label:
                    current.addr = new_addr
                    break
                current = current.next
        elif choice == 3:
            new_label = input("Enter the new label: ")
            new_addr = int(input("Enter the new address: "))
            current = self.first
            while current is not None:
                if current.label == label:
                    current.label = new_label
                    current.addr = new_addr
                    break
                current = current.next

    def delete(self):
        label = input("Enter the label to be deleted: ")

        if not self.search(label):
            print("Label not found")
            return

        if self.first.label == label:
            self.first = self.first.next
            if self.size == 1:
                self.last = None
        else:
            prev = None
            current = self.first
            while current is not None:
                if current.label == label:
                    if self.last == current:
                        self.last = prev
                    if prev is not None:
                        prev.next = current.next
                    break
                prev = current
                current = current.next

        self.size -= 1


table = SymbolTable()
while True:
    print("\nSYMBOL TABLE IMPLEMENTATION")
    print("1. INSERT")
    print("2. DISPLAY")
    print("3. DELETE")
    print("4. SEARCH")
    print("5. MODIFY")
    print("6. END")
    op = int(input("Enter your option: "))
    if op == 1:
        table.insert()
        table.display()
    elif op == 2:
        table.display()
    elif op == 3:
        table.delete()
        table.display()
    elif op == 4:
        label = input("Enter the label to be searched: ")
        if table.search(label):
            print("The label is already in the symbol table")
        else:
            print("The label is not found in the symbol table")
    elif op == 5:
        table.modify()
        table.display()
    elif op == 6:
        break
