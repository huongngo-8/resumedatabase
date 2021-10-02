import pandas as pd
import os
import csv

def cleanData(path):
    uncleanedFile = path

    uncleanedDf = pd.read_csv(uncleanedFile)
    uncleanedDf.set_index('key')

    # List
    # Email
    emails = []
    emailDf = uncleanedDf.loc[uncleanedDf["key"] == "email"]
    emails = emailDf['values'].tolist()


    # Phone Number
    phones = []
    phoneDf = uncleanedDf.loc[uncleanedDf['key'] == 'phone']
    phones = phoneDf['values'].tolist()

    # Name
    names = []
    nameDf = uncleanedDf.loc[uncleanedDf['key'] == 'name']
    names = nameDf['values'].tolist()

    # Designation
    designations = []
    designationDf = uncleanedDf.loc[uncleanedDf['key'] == 'designition']
    designations = designationDf['values'].tolist()

    # Degree
    degrees = []
    degreeDf = uncleanedDf.loc[uncleanedDf['key'] == 'degree']
    degrees = degreeDf['values'].tolist()

    # Skills
    skills = []
    skillDf = uncleanedDf.loc[uncleanedDf['key'] == 'skills']
    skills = skillDf['values'].tolist()


    # File
    files = []
    fileDf = uncleanedDf.loc[uncleanedDf['key'] == 'file']
    files = fileDf['values'].tolist()


    # Cleaning up skills
    for entry in skills:
        # deleting the first and last [] brackets
        slice_object = slice(1, -1)
        skills[skills.index(entry)] = entry[slice_object]   