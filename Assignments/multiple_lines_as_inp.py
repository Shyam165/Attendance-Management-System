#  Give Multiple Lines In Input Function Using '\n'. 

def get_multiple_lines_input():
    print("Enter multiple lines of text. Press Enter on an empty line to finish.")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return lines

def main():
    lines = get_multiple_lines_input()

    print("\nYou entered the following lines:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
