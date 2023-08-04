import pandas as pd

def save_as_csv(table, filename):
    df = pd.DataFrame(table)
    df.to_csv(filename, index=False)
    print(f"Table has been successfully saved as {filename}")

def save_as_excel(table, filename, sheet_name="Sheet1"):
    df = pd.DataFrame(table)
    df.to_excel(filename, index=False, sheet_name=sheet_name)
    print(f"Table has been successfully saved as {filename}")

def main():
    table = [
        ["Name", "Age", "City"],
        ["John", 25, "New York"],
        ["Alice", 28, "Los Angeles"],
        ["Bob", 22, "Chicago"],
    ]

    csv_filename = "table_data.csv"
    excel_filename = "table_data.xlsx"

    save_as_csv(table, csv_filename)
    save_as_excel(table, excel_filename)

if __name__ == "__main__":
    main()
