from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import NoneType
import pandas as pd
import resumeParser as rp
import urllib as url
import re
import os
import csv

# locating where check in data file is
checkInData = "COPY PATH OF CHECK IN CSV FILE HERE"

# reading in the check in data as a dataframe
checkInDf = pd.read_csv(checkInData)

# dropping duplicates within the check-in dataset
checkInDf = checkInDf.drop_duplicates(subset=['First Name', 'Last Name'])

# converting every column of dataframe into a list
checkInDict = checkInDf.to_dict('list')

# Dictionaries
    # First Name
firstNames = checkInDict['First Name']
    # Last Name
lastNames = checkInDict['Last Name']
    # Email
emails = checkInDict['Email']
    # Phone Number
phoneNumbers = checkInDict['Phone Number']
    # Pronouns
pronouns = checkInDict['Pronouns']
    # Job/Internship?
employmentStatus = checkInDict['Are you currently looking for a job or internship?']
    # Current level of study
levelOfStudy = checkInDict['What is your current level of study?.']
    # Name of University
universities = checkInDict['Name of University']
    # Other University
otherUniversities = checkInDict['Please enter name of your university']
    # Majors
majors = checkInDict['What is your major?']
    # Other Majors
additionalMajors = checkInDict['If applicable, what are your other major(s)?']
    # Minors
minors = checkInDict['If applicable, what are your minor(s)?']
    # Majors (Others, not in MLH)
otherMajors = checkInDict['Please enter your major']
    # Name of High School
highSchools = checkInDict['Name of High School']
    # Name of Bootcamp Program
bootcamps = checkInDict['Name of Bootcamp program.']
    # Country of Residence
countries = checkInDict['What is your country of residence?']
    # State of Residence
states = checkInDict['What state do you currently reside in?']
    # City
cities = checkInDict['What city do you currently reside in?']
    # Resume Link
resumes = checkInDict['Resume (Optional)']
    # LinkedIn Profile Link
linkedIn = checkInDict['LinkedIn Profile (Optional)']

# Capitalizing first name column
for i in range(len(firstNames)):
    firstNames[i] = firstNames[i].title()

# Capitalizing last name column
for i in range(len(lastNames)):
    lastNames[i] = lastNames[i].title()

for i in range(len(emails)):
    emails[i] = emails[i].lower()

# Capitalizing "What is your current level of study?" column
for i in range(len(levelOfStudy)):
    if type(levelOfStudy[i]) != float:
        levelOfStudy[i] = levelOfStudy[i].title()


# Capitalizing the "Other" universities
for i in range(len(universities)):
    if type(otherUniversities[i]) != float and universities[i] == 'Other':
        universities[i] = otherUniversities[i].title()
    
# Capitalizing the "Other" majors
for i in range(len(majors)):
    if type(majors[i]) != float and majors[i] == 'Other':
        majors[i] = otherMajors[i].title()

    
# Capitalizing additional majors
for i in range(len(additionalMajors)):
    if type(additionalMajors[i]) != float:
        additionalMajors[i] = additionalMajors[i].title()

# Concatenating on the major with additional major(s) individual stated
for i in range(len(majors)):
    if type(additionalMajors[i]) == str and type(majors[i]) == str:
        newMajor = ""
        newMajor = majors[i] + ", " + additionalMajors[i]
        majors[i] = newMajor

# Capitalizing the minors
for i in range(len(minors)):
    if type(minors[i]) != float:
        minors[i] = minors[i].title()

# Capitalizing high schools
for i in range(len(highSchools)):
    if type(highSchools[i]) != float:
        highSchools[i] = highSchools[i].title()


# Capitalizing bootcamps
for i in range(len(bootcamps)):
    if type(bootcamps[i]) != float:
        bootcamps[i] = bootcamps[i].title()

# Capitalizing cities
for i in range(len(cities)):
    if type(cities[i]) != float:
        cities[i] = cities[i].title()

cleanedDict = {'First Name': firstNames, 'Last Name': lastNames, 'Phone Number': phoneNumbers, 'Email': emails, 'Pronouns': pronouns, 
'Current Level of Study': levelOfStudy, 'Employment Status': employmentStatus, 'College': universities, 'Major': majors, 
'Minor': minors, 'High School': highSchools, 'Bootcamp': bootcamps, 'Country': countries, 'State': states, 
'City': cities, 'Resume': resumes, 'LinkedIn': linkedIn}

finalCheckInDf = pd.DataFrame.from_dict(cleanedDict)

# Saves all valid resume files to a spreadsheet and downloads it (don't know where, need to test)
files = []
for i in range(len(resumes)):
    if type(resumes[i]) == float:
        files.append(None) # not sure if type is float
    else:
        fileName = resumes[i].split('/')[-1]
        url.request.urlretrieve(resumes[i], fileName)
        files.append(fileName)

cleanedResumeDf, cleanedResumeCSV = rp.resumeParser(files)

finalDf = pd.merge(finalCheckInDf, cleanedResumeDf, left_index=True, right_index=True)
finalCSV = finalDf.to_csv('NAME OF THE FINAL CHAPTER-SPECIFIC RESUME BOOK')

print('Complete Creation of TechTogether Resume Book')





