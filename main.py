import syllabus_pre_processor
from nlp_model import run
import re
from prettytable import PrettyTable
import os

# all files
project_path = "/Users/suraj/PycharmProjects/pythonProject/"
jd_name = 'Product Specialist _ JD 2.pdf'
# Join various path components
syllabus_pdf_path = f"{project_path}BA_syllabus.pdf"
ner_model_path = f"{project_path}nlp_model/Models/model-best"

syllabus_object, course_code_list = syllabus_pre_processor.create_syllabus_object(syllabus_pdf_path)
skills_required_for_job = run.run_model(ner_model_path,jd_name)
print("syllabus_object ::", syllabus_object)
print("course_code_list::", course_code_list)
print("skills_required_for_job::", skills_required_for_job)

# This part is just for displaying the output..not related to Model/Code.
col_headers = ['']
for i in skills_required_for_job['SKILLS']:
    col_headers.append(i.lower())
col_headers = [*set(col_headers)]
myTable = PrettyTable(col_headers)


def add_to_table(row_name, data_list):
    row_to_add = [''] * len(col_headers)
    row_to_add[0] = syllabus_object[row_name]['title']
    for i in data_list:
        row_to_add[col_headers.index(i)] = 'Yes'
    myTable.add_row(row_to_add)


# end of display part

# ------calculating and displaying output------
# create re exp from the list of skills required for the job
search_list = skills_required_for_job['SKILLS']
regex = re.compile('|'.join(search_list))
# for syllabus section of each course compare and check if skills required is present.
for course_code in course_code_list:
    # course_units data contains syllabus details for each course_code.
    course_units_data = syllabus_object[course_code]['syllabus']
    res = []
    if course_units_data is not None:
        # from the re pattern created in line 19,20 find all against course_units_data.
        course_units_data = course_units_data.strip()
        cleanString = re.sub('[^A-Za-z0-9 ]+', '', course_units_data)
        res = regex.findall(cleanString, re.IGNORECASE)
        # remove duplicates from result
        res = [*set(res)]
        # res will now contain the matched skills in this particular course.
    try:
        add_to_table(course_code, res)
    except:
        print()
    print("_____________________________")

print(myTable)
