if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")
    for i in range(len(file_name)):
        if file_name[i] == ".":
            print("The extension of the file is: ", end='')
            for j in range(i + 1, len(file_name)):
                print(file_name[j], end='')
            break