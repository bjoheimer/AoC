import os
import re

def get_file_path() -> str:
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input3_1.txt")
    return file_path

def get_lines(file_path: str) -> list[str]:
    """
    Reads a text file with where each line is a list (report) and each column is a level.

    :param file_path: Path to the text file.
    :return lines: A list of lists, the so-called reports.
    """
    lines: list[str] = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into two parts
                lines.append(line)
    except FileNotFoundError:
        print(f"Error: File not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")
    return lines

def filter_lines(lines: list[str]) -> list[str]:
    """
    Extracts all matches for a valid mul(x,y) instruction call from a list of lines.

    :param lines: The list of scrambled memory lines.
    :return muls: The list of valid multiplication instructions.
    """
    muls: list[str] = []
    for line in lines:
        muls_in_line: list[str] = extract_muls_from_line(line)
        muls.extend(muls_in_line)
    return muls

def extract_muls_from_line(line: str) -> list[str]:
    """
    Extracts all matches for a valid mul(x,y) instruction call from a single line.

    :param lines: The list of scrambled memory lines
    :return: The list of valid multiplication instructions
    """
    return re.findall(r'mul\([0-9]*,[0-9]*\)', line)

def scan_conditional(lines: list[str]) -> list[str]:
    """
    Extracts all matches for a valid mul(x,y) instruction call that have been enabled by a previous do().
    All muls behind a don't() are ignored.
    In order to implement this, we scan the text linearly.

    :param lines: The list of scrambled memory lines
    :return muls: The list of valid multiplication instructions
    """
    enabled = True
    muls: list[str] = []
    for line in lines:
        enabled = extract_enabled_muls_from_line(line, enabled, muls)
        #print(enabled)
    return muls

            
def extract_enabled_muls_from_line(line:str, enabled: bool, muls: list[str]) -> bool:
    """
    Recursively examines a line and extracts enabled multiplications.
    In enabled mode, the line is partitioned by "don't".
    Before don't(), all multiplications are extracted.
    After don't(), we need to descent recursively in disabled mode if there is string left.
    In disabled mode, we partition with do().
    Everything before do() is ignored, after do, we recursively descent in enabled mode.

    The base case of the recursion is when do() or don't() cannot be found (then the enabled flag stays the same) or when there is nothing left behind do() or don't() (then the flag is toggled).

    :param line: The string to be examined.
    :param enabled: Current mode, i.e. was do() last (enabled = true) or don't().
    :param muls: List of muls, passed by reference.
    :return loc_enabled: The mode after the line was read.
    """
    loc_enabled = enabled
    #print("Before: ", line, enabled)
    if enabled:
        before_dont, dont, after_dont = line.partition("don't()")
        if len(before_dont) != 0 :
            muls.extend(extract_muls_from_line(before_dont))
        if dont == "don't()":
            loc_enabled = extract_enabled_muls_from_line(after_dont, False, muls)
        
    else:
        before_do, do, after_do = line.partition("do()")
        if len(after_do) != 0 :
            loc_enabled = extract_enabled_muls_from_line(after_do, True, muls)
        elif do == "do()":
            loc_enabled = True

    #print("After : ", line, loc_enabled)   
    return loc_enabled


def get_sum_of_muls(muls: list[str]) -> int:
    """
    From a list of muls, calculates the products and returns the sum of those products.

    :param muls: The list of multiplication operations, given as strings.
    :return sum: The sum of products.
    """
    sum: int = 0
    for mul in muls:
        sum += multiply(mul)
    return sum

def multiply(mul: str) -> int:
    """
    Returns the product calculated by a multiplication operation.

    :param mul: The multiplication operation.
    :return: The product.
    """
    nums = re.findall(r'[0-9]+', mul)
    if len(nums) != 2:
        raise ValueError("Multiplication does not have two arguments.")
    return int(nums[0])*int(nums[1])


def main() -> None:
    """
    Main function.
    """
    file_path = get_file_path()
    print("File path received as: ", file_path, "\n")
    lines = get_lines(file_path)

    #muls = filter_lines(["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)", "+mul(32,64]then(mul(11,8)mul(8,5))"])

    muls = filter_lines(lines)
    print("Multiplication Operations: ", len(muls), "\n", muls, "\n")

    #lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", "don't()do()mul(1,42)don't()", "mul(1,69)do()"]

    enabled_muls = scan_conditional(lines)
    print("EnabledMultiplication Operations: ", len(enabled_muls), "\n", enabled_muls, "\n")

    sum = get_sum_of_muls(muls)
    print("Sum of Products: ", sum, "\n")

    enabled_sum = get_sum_of_muls(enabled_muls)
    print("Sum of Enabled Products: ", enabled_sum)

if __name__ == "__main__":
    main()