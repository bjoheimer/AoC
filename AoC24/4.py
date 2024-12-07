import os
import re

def get_file_path() -> str:
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input4_1.txt")
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

def get_xmas_count(lines: list[str]) -> int:
    """
    Counts all occurrences of XMAS in a list of lines of equal length.

    :param lines: The list of lines.
    :return count: The number of occurrences.
    """
    count: int = 0
    count += (
        get_count_horizontal_fwd(lines) 
        + get_count_horizontal_bwd(lines) 
        + get_count_vertical_fwd(lines) 
        + get_count_vertical_bwd(lines) 
        + get_count_diagonal_bl_to_tr(lines) 
        + get_count_diagonal_tl_to_br(lines) 
        + get_count_diagonal_br_to_tl(lines) 
        + get_count_diagonal_tr_to_bl(lines)
    )
    return count

def get_count_horizontal_fwd(lines: list[str]) -> int:
    count: int = 0
    for line in lines:
        count += len(re.findall("XMAS", line))
    return count

def get_count_horizontal_bwd(lines: list[str]) -> int:
    count: int = 0
    for line in lines:
        count += len(re.findall("SAMX", line))
    return count

def get_count_vertical_fwd(lines: list[str]) -> int:
    count: int = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[0])):
            if (lines[i][j] == "X" 
                 and lines[i+1][j] == "M" 
                 and lines[i+2][j] == "A" 
                 and lines[i+3][j] == "S"):
                count += 1
    return count

def get_count_vertical_bwd(lines: list[str]) -> int:
    count: int = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[0])):
            if (lines[i][j] == "S" 
                 and lines[i+1][j] == "A" 
                 and lines[i+2][j] == "M" 
                 and lines[i+3][j] == "X"):
                count += 1
    return count

def get_count_diagonal_tl_to_br(lines: list[str]) -> int:
    count: int = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[0])-3):
            if (lines[i][j] == "X" 
                 and lines[i+1][j+1] == "M" 
                 and lines[i+2][j+2] == "A" 
                 and lines[i+3][j+3] == "S"):
                count += 1
    return count

def get_count_diagonal_tr_to_bl(lines: list[str]) -> int:
    count: int = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[0])-3):
            if (lines[i][j+3] == "X" 
                 and lines[i+1][j+2] == "M" 
                 and lines[i+2][j+1] == "A" 
                 and lines[i+3][j] == "S"):
                count += 1
    return count

def get_count_diagonal_bl_to_tr(lines: list[str]) -> int:
    count: int = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[0])-3):
            if (lines[i+3][j] == "X" 
                 and lines[i+2][j+1] == "M" 
                 and lines[i+1][j+2] == "A" 
                 and lines[i][j+3] == "S"):
                count += 1
    return count

def get_count_diagonal_br_to_tl(lines: list[str]) -> int:
    count: int = 0
    for i in range(len(lines)-3):
        for j in range(len(lines[0])-3):
            if (lines[i+3][j+3] == "X" 
                 and lines[i+2][j+2] == "M" 
                 and lines[i+1][j+1] == "A" 
                 and lines[i][j] == "S"):
                count += 1
    return count

def get_x_mas_count(lines: list[str]) -> int:
    count = 0
    for i in range(len(lines)-2):
        for j in range(len(lines[0])-2):
            if((lines[i+1][j+1]=="A")
                and((lines[i][j]=="M" and lines[i+2][j+2]=="S") 
                    or (lines[i][j]=="S" and lines[i+2][j+2]=="M")) 
                and ((lines[i+2][j]=="M" and lines[i][j+2]=="S") 
                    or (lines[i+2][j]=="S" and lines[i][j+2]=="M"))):
                count+=1
    return count


def main() -> None:
    """
    Main function.
    """
    file_path = get_file_path()
    print("File path received as: ", file_path, "\n")
    lines = get_lines(file_path)

    xmas_count = get_xmas_count(lines)
    print("XMAS Count: ", xmas_count, "\n")

    x_mas_count = get_x_mas_count(lines)
    print("X-MAS Count: ", x_mas_count, "\n")

if __name__ == "__main__":
    main()