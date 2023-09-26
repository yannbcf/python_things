import os
import re

input_folder_path = ""
output_file_path = ""

issues = {
    "duplicate": 0,
    "missing": 0
}

def check_patterns(folder_path):
    try:
        with open(output_file_path, "w"):
            pass

        with open(output_file_path, "a") as output_file:
            pattern_dict = extract_patterns_from_folder(folder_path)

            for name, pattern in pattern_dict.items():
                for i in range(2):
                    addr = idc.find_binary(0, ida_search.SEARCH_DOWN, pattern)
                    if (i == 1 and addr != ida_idaapi.BADADDR):
                        output_file.write(f"Duplicate pattern: {name} ({pattern})\n")
                        issues["duplicate"] += 1
                        break

                    if (i == 0 and addr == ida_idaapi.BADADDR):
                        output_file.write(f"Missing pattern: {name} ({pattern})\n")
                        issues["missing"] += 1

            return True

    except FileNotFoundError:
        print(f"File not found: {output_file_path}")
        return False

def extract_patterns_from_folder(folder_path):
    patterns_dict = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            extract_patterns_from_file(patterns_dict, file_path)

    return patterns_dict

def extract_patterns_from_file(patterns_dict, file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                if not "CMemory::Pattern" in line:
                    continue

                match = re.search(r'CMemory::Pattern\s+(\w+)\("([^"]+)"\);', line.strip())
                if match:
                    name = match.group(1)
                    pattern_str = match.group(2)
                    patterns_dict[name] = pattern_str

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    return patterns_dict

print(f"\nStarting to analyze the patterns from the folder {input_folder_path} ..\n")

if check_patterns(input_folder_path):
    print(f"Analysis finished ! found {issues['duplicate']} duplicated patterns and {issues['missing']} missing patterns")

    if issues["duplicate"] != 0 or issues["missing"] != 0:
        print(f"Check the output file at {output_file_path}")
