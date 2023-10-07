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
for i in range(len(marks_data)):
    module = marks_data[i]
    component_percentile = 0
    # for marks in module["component_marks"]:
    for ii in range(len(module["component_marks"])):
        marks = module["component_marks"][ii]
        component_percentile += (marks["weightage"] * (marks["obtained_marks"]/marks["total_marks"]))
        marks["component_percentail"] = component_percentile
        module["component_marks"][ii] = marks

    module["module_percentail"] = component_percentile
    marks_data[i] = module

    total_marks += component_percentile
    total_counts += 1

# print(f"TC : {total_counts}\nTm: {total_marks}")

total_percentail = total_marks/total_counts
grade_point = total_percentail/grade_dividand

final_grades = {
    "total_marks_obtained": total_marks,
    "grade_points": grade_point,
    "module_wise_details": marks_data
}

percentail_details_json_path=os.path.join(os.path.abspath("."),"percentail_details.json")

with open(percentail_details_json_path, 'w') as write_file:
    json.dump(final_grades, write_file, indent=4)

print("\n==========================================\n")
print(f"TP: {total_percentail}, GP: {grade_point}")
print("\n==========================================\n")