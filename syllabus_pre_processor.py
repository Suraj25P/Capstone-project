import re
import pdfplumber as pdfplumber

# change this accordingly



def get_course_title_code(_course_header):
    # helper function to handle edge case : if course title spans 2 lines
    _header1 = _course_header[0].split('Course Code:')
    _title = _header1[0] + _course_header[1] if len(_course_header) > 2 else _header1[0]
    _code = _header1[1]
    return _title.strip(), _code.strip()


def run_regex(exp, _str):
    # helper function to run regEX
    try:
        return re.search(exp, _str).group(1)
    except AttributeError:
        return re.search(exp, _str)


# GLOBAL VARIABLES
def create_syllabus_object(file_path):
    complete_text = ''
    course_code_list = []  # To refer in return_object
    return_object = {}  # will contain Data of each course

    with pdfplumber.open(file_path) as pdf:
        # loop through every page and get the complete pdf into complete_text
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            complete_text = complete_text + single_page_text
    courses = complete_text.split('Course Name:')
    courses.pop(0)

    for each_course in courses:
        # get title and code from course header section for each course
        course_header = each_course.split('Total number of hours')[0].split('\n')
        course_title, course_code = get_course_title_code(course_header)
        course_code_list.append(course_code)
        # remove unnecessary new lines and carriage returns so that regex wont fail
        each_course = each_course.replace('\n', ' ').replace('\r', '').lower()
        # extract Data for each course
        _obj = {
            "title": course_title,
            "hrs": run_regex(r'total number of hours:(.*?)credits', each_course),
            "credits": run_regex(r'credits:(.*?)course description:', each_course),
            "description": run_regex(r'course description:(.*?)course objectives:', each_course),
            "objectives": run_regex(r'course objectives:(.*?)course learning outcomes:', each_course),
            "outcomes": run_regex(r'course learning outcomes:(.*?)pedagogy:', each_course),
            "syllabus": run_regex(r'syllabus(.*?)(essential reference|assessment outline:)', each_course)
        }
        # push to global object
        return_object[course_code] = _obj

    return  return_object,course_code_list
# you can now access Data from return object as : return_object[<add course_code>][<any property>]
