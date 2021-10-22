from resume_parser import resumeparse
import os
import pandas as pd
import csv
import re

def resumeParser(fileList):
    path = "PATH OF WHERE THE ENTIRE WORKSPACE WILL BE" 
    count = 0
    parsedDf = pd.DataFrame([], columns=['Degree', 'Skills', 'Designations', 'File Name'])
    row = []
    rows = []
    for file in fileList:
        if type(file) == str and (file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.doc')):
            f = os.path.join(path, file)
            print('File: %s' %file)
            if os.path.isfile(f):
                data = resumeparse.read_file(f)
                data['file'] = file
                row = [data['degree'], data['skills'], data['designition'], data['file']]
                rows.append(row)
                count += 1
                print(count)
        else:
            row = [None, None, None, None]
            rows.append(row)
            count += 1
            print(count)
    print('Completed Resume Parsing')
    parsedDf = pd.DataFrame(rows, columns=['Degree', 'Skills', 'Designation', 'File Name'])
    parsedCSV = parsedDf.to_csv('NAME OF CSV FILE WITH PARSED RESUME DATA', header=['Degree', 'Skills', 'Designation', 'File Name'])
    finalResDf = cleanData('NAME OF CSV FILE WITH PARSED RESUME DATA (SAME WITH PREVIOUS LINE)')
    finalResCSV = finalResDf.to_csv('NAME OF CSV FILE WITH PARSED RESUME DATA (SAME WITH PREVIOUS LINE)', header=['Degree', 'Designations', 'Skills', 'File Name'])

    return finalResDf, finalResCSV


def cleanData(parsedCSV):
    parsedDf = pd.read_csv(parsedCSV)
    uncleanedDict = parsedDf.to_dict('list')

    # Designation
    designations = uncleanedDict['Designation']

    # Degree
    degrees = uncleanedDict['Degree']

    # Skills
    skills = uncleanedDict['Skills']

    # File
    files = uncleanedDict['File Name']

    # Cleaning up skills
    for i in range(len(skills)):
        if type(skills[i]) == str:
            slice_object = slice(1, -1)
            skills[i] = skills[i][slice_object]
            table = str.maketrans('', '', '\'"')
            skills[i] = skills[i].translate(table)
            skillsList = re.split(', | \| |\|', skills[i])
            cleanedSkills = filter(skillsList)
            for j in range(len(cleanedSkills)):
                cleanedSkills[j] = cleanedSkills[j].capitalize()
            skill = ', '.join(cleanedSkills)
            skills[i] = skill

    # Cleaning up designations
    for i in range(len(designations)):
        if type(skills[i]) == str:
            slice_object = slice(1, -1)
            designations[i] = designations[i][slice_object]
            table = str.maketrans('', '', '\'●"')
            designations[i] = designations[i].translate(table)
            designations[i] = designations[i].title()

    for i in range(len(degrees)):
        if type(skills[i]) == str:
            slice_object = slice(1, -1)
            degrees[i] = degrees[i][slice_object]
            table = str.maketrans('', '', '\'()"')
            degrees[i] = degrees[i].translate(table)
            degrees[i] = degrees[i].title()
    finalDict = {'Degree': degrees, 'Designations': designations, 'Skills': skills, 'Files': files}
    finalResDf = pd.DataFrame.from_dict(finalDict)
    print('Completed Cleaning Parsed Resume Data')

    return finalResDf

def filter(list):
    newList = []
    singles = []
    skills = pd.read_csv('skills.csv').keys().tolist()
    for i in range(len(skills)):
        if len(skills[i]) == 1:
            singles.append(skills[i])
    for i in range(len(list)):
        list[i] = list[i].lower()
        if len(list[i]) == 1:
            for singleSkill in singles:
                if list[i] == singleSkill:
                    list[i] = singleSkill
        else:
            for skill in skills:
                if skill in list[i]:
                    newList.append(skill)
    return newList 

