import syllabus_pre_processor
from nlp_model import run

syllabus_pdf_path = r'/Users/suraj/PycharmProjects/pythonProject/BA_syllabus.pdf'
ner_model_path = "/Users/suraj/PycharmProjects/pythonProject/nlp_model/Models/model-best"

syllabus_object , course_code_list = syllabus_pre_processor.create_syllabus_object(syllabus_pdf_path)

print("syllabus_object::",syllabus_object['MBA 236']['syllabus'])
print("course_code_list::",course_code_list)
skills_required_for_job = run.run_model(ner_model_path)
print("skills_required_for_job::",skills_required_for_job)


