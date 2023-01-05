if __name__ == '__main__':
    number_of_commands = int(input())
    output_list = []
    for i in range(number_of_commands):
        command = list(map(str, input().strip().split(" ")))
        if command[0] == "insert":
            output_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            output_list.append(int(command[1]))
        elif command[0] == "sort":
            output_list.sort()
        elif command[0] == "print":
            print(output_list)
        elif command[0] == "pop":
            output_list.pop()
        elif command[0] == "reverse":
            output_list.reverse()
        elif command[0] == "remove":
            output_list.remove(int(command[1]))
