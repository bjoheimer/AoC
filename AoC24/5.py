import os
import re

def get_file_path() -> str:
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input5_2.txt")
    return file_path

def get_lines(file_path: str) -> list[str]:
    """
    Reads a text file where all lines have equal length.

    :param file_path: Path to the text file.
    :return lines: A list of lists, the so-called reports.
    """
    lines: list[str] = []
    line_len: int = -1

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line_len == -1:
                    line_len = len(line)
                elif line_len != len(line):
                    raise ValueError(f"Not all lines are equally long")
                # Split each line into two parts
                lines.append(line)
    except FileNotFoundError:
        print(f"Error: File not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")
    return lines


def main() -> None:
    """
    Main function.
    """
    file_path = get_file_path()
    print("File path received as: ", file_path, "\n")
    lines = get_lines(file_path)

if __name__ == "__main__":
    main()