# This file will take a JD and run it against a NER model to extract skills

import spacy

# insert job description
job_description = """
Master or Ph.D. in Mathematics, Physics, Computer Science or a similar field
Three to six years of professional experience outside academia, preferably experience in Supply Chain
Strong skills in Machine Learning, Statistics and Predictive Modelling
Project management experience
Programming skills, e.g. Python, R, Java, C++
Comfortable reporting results to both technical and non-technical audiences
Ability to work with people from various backgrounds/cultures
Strong interpersonal skills with the desire to share knowledge and skills
Preferably experience in Visualization Tools, e.g. Tableau, Qlik as well as Data processing and/or database programming skills, e.g. SQL.
"""


ner_model_path = "/Users/suraj/PycharmProjects/pythonProject/nlp_model/Models/model-best"

ner_model = spacy.load(ner_model_path)
print(ner_model)
# test the algorithm
doc = ner_model(job_description)
print(doc.ents)
skills_required = {}
# initilize the keys
for ent in doc.ents:
    skills_required[ent.label_] = []
for ent in doc.ents:
    print(ent.text, '--->', ent.label_)
    skills_required[ent.label_] += [ent.text]
print(skills_required)