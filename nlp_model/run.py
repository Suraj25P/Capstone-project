# This file will take a JD and run it against a NER model to extract skills

import spacy
import os
import pdfplumber as pdfplumber


# insert job description
# job_description = """
# Master or Ph.D. in Mathematics, Physics, Computer Science or a similar field
# Three to six years of professional experience outside academia, preferably experience in Supply Chain
# Strong skills in Machine Learning, Statistics and Predictive Modelling
# Project management experience
# Programming skills, e.g. Python, Java,
# Comfortable reporting results to both technical and non-technical audiences
# Ability to work with people from various backgrounds/cultures
# Strong interpersonal skills with the desire to share knowledge and skills
# Preferably experience in Visualization Tools, e.g. Tableau, Qlik as well as Data processing and/or database programming skills, e.g. SQL.
# """

def convert_to_text(_jd_name):
    script_dir = os.path.dirname(__file__)
    rel_path = _jd_name
    abs_file_path = os.path.join(script_dir,'sample_jd', rel_path)
    complete_text = ''

    with pdfplumber.open(abs_file_path) as pdf:
        # loop through every page and get the complete pdf into complete_text
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            complete_text = complete_text + single_page_text

    return complete_text


def run_model(ner_model_path, jd_name):
    ner_model = spacy.load(ner_model_path)
    # test the algorithm
    _complete_text = convert_to_text(jd_name)
    doc = ner_model(_complete_text)
    skills_required = {}
    # initilize the keys
    for ent in doc.ents:
        skills_required[ent.label_] = []
    for ent in doc.ents:
        print(ent.text, '--->', ent.label_)
        skills_required[ent.label_] += [ent.text.lower()]
    return skills_required
