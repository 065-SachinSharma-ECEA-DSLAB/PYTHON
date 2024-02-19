def linear_search(arr, element):
    for i, item in enumerate(arr):
        if item == element:
            print(f"Element {element} found at index {i}.")
            return  # Exit the function after finding the element
    print(f"Element {element} not found.")

def insert_element(arr, index, element):
    arr.insert(index, element)

def delete_element(arr, index):
    arr.pop(index)

def reverse_array(arr):
    arr.reverse()

def update_array(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] += 5
        else:
            arr[i] *= 2

def print_array(arr):
    print("Array:", ' '.join(map(str, arr)))

def main():
    n = int(input("Enter the size of the array: "))
    arr = [int(input()) for _ in range(n)]
    
    while True:
        print("\nMenu:")
        print("1. Linear Search")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Reverse Array")
        print("5. Update Array")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter the element to search: "))
            linear_search(arr, element)
        elif choice == 2:
            index = int(input("Enter the index of array to insert element: "))
            element = int(input("Enter the element to be inserted: "))
            insert_element(arr, index, element)
            print("\nAfter insertion array:", arr)
        elif choice == 3:
            index = int(input("Enter the index of element to be deleted: "))
            delete_element(arr, index)
            print("\nAfter deletion:", arr)
        elif choice == 4:
            reverse_array(arr)
            print_array(arr)
        elif choice == 5:
            update_array(arr)
            print_array(arr)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

