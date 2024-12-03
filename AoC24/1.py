import os

def get_file_path() -> str:
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input1_1.txt")
    return file_path

def read_columns_into_lists(file_path: str) -> tuple[list[int], list[int]]:
    """
    Reads a text file with two columns and separates them into two lists.

    :param file_path: Path to the text file.
    :return: Two lists representing the two columns.
    """
    column1: list[int] = []
    column2: list[int] = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into two parts
                parts = line.strip().split()  # Adjust delimiter if necessary, e.g., split(',') for CSV
                if len(parts) == 2:
                    column1.append(int(parts[0]))
                    column2.append(int(parts[1]))
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")
    return column1, column2

def prepare_lists(l1: list[int], l2:list[int]) -> None:
    if(len(l1) != len(l2)):
        print(f"Lists don't have the same length. Aborting...\n")
        exit(1)
    l1.sort()
    l2.sort()

def getDiff(l1: list[int], l2: list[int]) -> int:
    diff: int = 0
    for i in range(len(l1)):
        diff += abs(l1[i]-l2[i])
    return diff

def get_similarity_score(l1: list[int], l2: list[int]) -> int:
    score = 0
    for i in range(len(l1)):
        num = l1[i]
        for j in range(len(l2)):
            if l2[j] == num:
                score += num
    return score

def main() -> None:
    """
    Main function.
    """
    file_path = get_file_path()
    print("File path received as: ", file_path, "\n")
    l1, l2 = read_columns_into_lists(file_path)
    #l1 = [3, 4, 2, 1, 3, 3]
    #l2 = [4, 3, 5, 3, 9, 3]

    prepare_lists(l1, l2)

    diff = getDiff(l1, l2)

    print("Total distance between the lists: ", diff, "\n")

    similarity_score = get_similarity_score(l1, l2)

    print("Similarity Score: ", similarity_score)

if __name__ == "__main__":
    main()