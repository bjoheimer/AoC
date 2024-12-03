import os

def get_file_path() -> str:
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input2_1.txt")
    return file_path

def get_reports(file_path: str) -> list[list[int]]:
    """
    Reads a text file with where each line is a list (report) and each column is a level.

    :param file_path: Path to the text file.
    :return reports: A list of lists, the so-called reports.
    """
    reports: list[list[int]] = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into two parts
                parts = line.strip().split()  # Adjust delimiter if necessary, e.g., split(',') for CSV
                report = [int(part) for part in parts]
                reports.append(report)
    except FileNotFoundError:
        print(f"Error: File not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")
    return reports

def analyze(reports: list[list[int]]) -> tuple[list[str], int]:
    """
    Analyzes a list of reports.
    
    :param reports: The reports to analyze.
    :return analysis, num_safe: A list of \"Safe\" and \"Unsafe\" for each report and the number of safe reports.
    """
    analysis: list[str] = []
    num_safe = 0
    for report in reports:
        if is_safe(report):
            analysis.append("Safe")
            num_safe += 1
        else:
            analysis.append("Unsafe")
    return analysis, num_safe

def is_safe(report: list[int]) -> bool:
    """
    Checks for a single report whether it is safe, i.e. its levels are all increasing or all decreasing by at least one and at most three.

    :param report: the report to analyze
    :return: whether the report is safe according to the definition
    """

    if len(report) < 2:
        return True
    
    increasing = True
    differential = report[1] - report[0]

    if differential < 0:
        increasing = False

    prev_level = report[0]

    for i in range(1, len(report)):
        curr_level = report[i]
        diff = curr_level - prev_level

        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        if increasing and diff < 0:
            return False
        
        if not increasing and diff > 0:
            return False
    
        prev_level = curr_level
        
    return True

def analyze_with_dampener(reports: list[list[int]]) -> tuple[list[str], int]:
    """
    Analyzes a list of reports, but with the problem dampener.
    
    :param reports: The reports to analyze.
    :return dampened_analysis, num_safe_dampened: A list of \"Safe\" and \"Unsafe\" for each report and the number of safe reports.
    """
    dampened_analysis: list[str] = []
    num_safe_dampened = 0
    for report in reports:
        if is_safe_dampened(report):
            dampened_analysis.append("Safe")
            num_safe_dampened += 1
        else:
            dampened_analysis.append("Unsafe")
    return dampened_analysis, num_safe_dampened

def is_safe_dampened(report: list[int]) -> bool:
    """
    Checks for a single report whether it is safe with the dampener, i.e. its levels are all increasing or all decreasing by at least one and at most three.
    At most one level can be removed from the report.
    The report is also considered safe if the remaining levels form a safe report.

    :param report: the report to analyze
    :return: whether the report is safe according to the dampened definition
    """
    full_safe = is_safe(report)
    if full_safe:
        return True
    
    for i in range(len(report)):
        dampened_report: list[int] = []
        for j in range(len(report)):
            if not i==j:
                dampened_report.append(report[j])
        if is_safe(dampened_report):
            print("Remove ", i)
            return True
        
    return False

def main() -> None:
    """
    Main function.
    """
    file_path = get_file_path()
    print("File path received as: ", file_path, "\n")
    reports = get_reports(file_path)

    analysis, num_safe = analyze(reports)

    dampened_analysis, num_safe_dampened = analyze_with_dampener(reports)

    print("Analysis:\n", analysis, "\n")
    
    print("Dampened Analysis:\n", dampened_analysis, "\n")

    print("Number of Safe Reports: ", num_safe, "\n")

    print("Number of Safe Reports with Problem Dampener: ", num_safe_dampened, "\n")

if __name__ == "__main__":
    main()