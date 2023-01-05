def hanoi(n, root, destination, temporary):
    if n == 1:
        move(n, root, destination)
    else:
        hanoi(n-1, root, temporary, destination)
        move(n, root, destination)
        hanoi(n-1, temporary, destination, root)


def move(n, root, destination):
    print(f"Moving {n} {root} to {destination}")


hanoi(3, "Root", "Destination", "temporary")