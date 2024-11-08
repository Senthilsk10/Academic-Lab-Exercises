class SymbolTable:
    def __init__(self, size):
        """Initialize the symbol table with a specific size"""
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, symbol):
        """Custom hash function to generate a hash key based on the symbol"""
        hash_value = 0
        for char in symbol:
            hash_value += ord(char)
        return hash_value % self.size

    def create(self, symbol, value):
        """Insert a symbol with its value in the symbol table"""
        index = self.hash_function(symbol)
        # Check if symbol already exists and update
        for entry in self.table[index]:
            if entry[0] == symbol:
                entry[1] = value
                print(f"Symbol '{symbol}' updated with value '{value}'.")
                return
        # If symbol doesn't exist, add a new entry
        self.table[index].append([symbol, value])
        print(f"Symbol '{symbol}' added with value '{value}'.")

    def retrieve(self, symbol):
        """Retrieve the value of a symbol"""
        index = self.hash_function(symbol)
        for entry in self.table[index]:
            if entry[0] == symbol:
                return entry[1]
        return None

    def display(self):
        """Display all the symbols in the table"""
        print("\n--- Symbol Table Contents ---")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")
        print("-----------------------------")


size = int(input("Enter the size of the symbol table: "))
symbol_table = SymbolTable(size)

while True:
    print("\nOptions:")
    print("1. Create (Insert/Update a symbol)")
    print("2. Retrieve (Search for a symbol)")
    print("3. Display (Show all symbols)")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        symbol = input("Enter the symbol: ")
        value = input(f"Enter the value for '{symbol}': ")
        symbol_table.create(symbol, value)
    elif choice == "2":
        symbol = input("Enter the symbol to retrieve: ")
        value = symbol_table.retrieve(symbol)
        if value:
            print(f"Symbol '{symbol}' has value: {value}")
        else:
            print(f"Symbol '{symbol}' not found.")
    elif choice == "3":
        symbol_table.display()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

