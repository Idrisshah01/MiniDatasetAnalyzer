from file_handler import load_csv, save_csv
from analyzer import (
    average_column,
    max_column,
    min_column,
    search_rows,
    frequency_count,
    search_by_id,
    search_by_name
)

def main():
    data = load_csv("data/students_sample.csv")
    if not data:
        print("  No data loaded. Exiting...")
        return

    while True:
        print("\n=====  Student Data Analyzer =====")
        print("1. Show average of a column")
        print("2. Show max of a column")
        print("3. Show min of a column")
        print("4. Show frequency count of a column")
        print("5. Search rows by column & value")
        print("6. Search by ID")
        print("7. Search by Name")
        print("8. Save data to new CSV")
        print("9. Exit")
        print("===================================")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            col = input("Enter column name (e.g. age, score): ")
            print(f"Average of '{col}': {average_column(data, col)}")

        elif choice == "2":
            col = input("Enter column name: ")
            print(f"Max of '{col}': {max_column(data, col)}")

        elif choice == "3":
            col = input("Enter column name: ")
            print(f"Min of '{col}': {min_column(data, col)}")

        elif choice == "4":
            col = input("Enter column name (e.g. gender): ")
            print(f"Frequency of '{col}': {frequency_count(data, col)}")

        elif choice == "5":
            col = input("Enter column name: ")
            val = input("Enter value to search: ")
            result = search_rows(data, col, val)
            print(f"Results for {col} = {val}: {result}")

        elif choice == "6":
            val = input("Enter ID to search: ")
            print(f"Search by ID '{val}': {search_by_id(data, val)}")

        elif choice == "7":
            val = input("Enter Name to search: ")
            print(f"Search by Name '{val}': {search_by_name(data, val)}")

        elif choice == "8":
            save_csv("data/output_sample.csv", data, fieldnames=data[0].keys())
            print("Data saved to data/output_sample.csv")

        elif choice == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
