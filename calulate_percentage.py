import os
import json

grade_dividand=9.5
marks_details_json_path=os.path.join(os.path.abspath("."),"marsk_details.json")

marks_data = None

with open(marks_details_json_path, 'r') as read_file:

    marks_data = json.load(read_file)

assert marks_data is not None, f"failed to read data from file {marks_details_json_path}"

total_marks = 0
total_counts = 0
for module in marks_data:
    module_percentile = 0
    for marks in module["component_marks"]:

        module_percentile += (marks["weightage"] * (marks["obtained_marks"]/marks["total_marks"]))

    # module_percentile/=100

    # print(f"{module['module_code']} --> {module_percentile}")

    total_marks += module_percentile
    total_counts += 1

# print(f"TC : {total_counts}\nTm: {total_marks}")

total_percentail = total_marks/total_counts
grade_point = total_percentail/grade_dividand



print("\n==========================================\n")
print(f"TP: {total_percentail}, GP: {grade_point}")
print("\n==========================================\n")