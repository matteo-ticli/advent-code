def read_input(file_name):
    """Reads the input grid from a file."""
    with open(f"./{file_name}", "r") as f:
        puzzle_input = f.read().strip().splitlines()
    return [list(row) for row in puzzle_input]


def check_horz(data, row, pos, match):
    """Check horizontally for the word and its reverse."""
    size = len(match)
    if pos + size <= len(data[row]):
        word = "".join(data[row][pos:pos + size])
        if word == match or word[::-1] == match:
            print(f"Horizontal Match at ({row}, {pos})")
            return 1
    return 0


def check_vert(data, row, pos, match):
    """Check vertically for the word and its reverse."""
    size = len(match)
    if row + size <= len(data):
        word = "".join(data[row + i][pos] for i in range(size))
        if word == match or word[::-1] == match:
            print(f"Vertical Match at ({row}, {pos})")
            return 1
    return 0


def check_diag_dn(data, row, pos, match):
    """Check diagonally (down-right) for the word and its reverse."""
    size = len(match)
    if row + size <= len(data) and pos + size <= len(data[row]):
        word = "".join(data[row + i][pos + i] for i in range(size))
        if word == match or word[::-1] == match:
            print(f"Diagonal Down Match at ({row}, {pos})")
            return 1
    return 0


def check_diag_up(data, row, pos, match):
    """Check diagonally (up-right) for the word and its reverse."""
    size = len(match)
    if row - size + 1 >= 0 and pos + size <= len(data[row]):
        word = "".join(data[row - i][pos + i] for i in range(size))
        if word == match or word[::-1] == match:
            print(f"Diagonal Up Match at ({row}, {pos})")
            return 1
    return 0


def find_cross_mas(data, row, pos, match):
    """Check that MAS is an X.

    We want to find a pattern like the following:

    (M)(.)(M)
    (.)(A)(.)
    (S)(.)(S)

    (M)(.)(S)
    (.)(A)(.)
    (M)(.)(S)

    ...

    Therefore, we will look for A's and then construct the surrounding cross.

    """
    if not data[row][pos] == "A":
        return 0
    else:

        row_up = row - 1
        row_dn = row + 1
        pos_sx = pos - 1
        pos_dx = pos + 1

        word_1 = "".join([data[row_up][pos_sx], data[row][pos], data[row_dn][pos_dx]])
        word_2 = "".join([data[row_up][pos_dx], data[row][pos], data[row_dn][pos_sx]])

        if ((word_1 == match or word_1[::-1] == match) and
                (word_2 == match or word_2[::-1] == match)):
            print(f"X-MAS Match at ({row}, {pos})")
            return 1

        return 0


def day_4_1(file_name, word_to_match="XMAS"):
    """Main function to search for the word in all directions in the grid."""
    count = 0
    data = read_input(file_name)

    # Print the grid for verification
    print("Input Grid Loaded. Grid Dimensions:", len(data), "x", len(data[0]))

    for j in range(len(data)):
        for i in range(len(data[0])):
            count += check_horz(data, j, i, word_to_match)
            count += check_vert(data, j, i, word_to_match)
            count += check_diag_dn(data, j, i, word_to_match)
            count += check_diag_up(data, j, i, word_to_match)

    print(f"Total Matches Found: {count}")
    return count


def day_4_2(file_name, word_to_match="MAS"):
    """Main function to search for two MAS words that are shaped like an X."""
    count = 0
    data = read_input(file_name)

    # Print the grid for verification
    print("Input Grid Loaded. Grid Dimensions:", len(data), "x", len(data[0]))

    for j in range(1, len(data)-1):
        for i in range(1, len(data[0])-1):
            count += find_cross_mas(data, j, i, word_to_match)

    print(f"Total Matches Found: {count}")
    return count


# Run the function with the file name
print(day_4_1("day_4.txt"))
print(day_4_2("day_4.txt"))