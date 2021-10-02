import pandas as pd
import parsedResumeCleaning as rdc
import resumeParser as rp
import os
import csv

checkInData = "/Users/huongngo/resumedatabase/dummydata.csv"
resumeData = "/Users/huongngo/resumedatabase/repeatingverification.csv"

checkInDf = pd.read_csv(checkInData)
resumeDf = pd.read_csv(resumeData)

checkInDict = checkInDf.to_dict('list')
resumeDict = resumeDf.to_dict('list')

# Dictionaries
    # First Name
firstNames = checkInDict['First Name']
    # Last Name
lastNames = checkInDict['Last Name']
    # Email
emails = checkInDict['Email']
    # Email from Resume Database
emailVerifying = resumeDict['Email']
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
for firstName in firstNames:
    firstNames[firstNames.index(firstName)] = firstName.title()

# Capitalizing last name column
for lastName in lastNames:
    lastNames[lastNames.index(lastName)] = lastName.title()

for email in emails:
    emails[emails.index(email)] = email.lower()
    if email in emailVerifying:
        row = checkInDf.loc[checkInDf['Email'] == email]
        olderRow = resumeDf.loc[resumeDf['Email'] == email]
        row.to_csv('repeats.csv', mode='a', header=False)
        olderRow.to_csv('repeats.csv', mode='a', header=False)
    

# Capitalizing "What is your current level of study?" column
for level in levelOfStudy:
    if type(level) != float:
        levelOfStudy[levelOfStudy.index(level)] = level.title()


# Capitalizing the "Other" universities
for university in universities:
    if university == 'Other':
        universities[universities.index(university)] = otherUniversities[universities.index(university)].title()
    
# Capitalizing the "Other" majors
for major in majors:
    if major == 'Other':
        majors[majors.index(major)] = otherMajors[majors.index(major)].title()

    
# Capitalizing additional majors
for additionalMajor in additionalMajors:
    if type(additionalMajor) != float:
        additionalMajors[additionalMajors.index(additionalMajor)] = additionalMajor.title()

# bug here, will check back again!
for major in majors:
    if type(additionalMajors[majors.index(major)]) == str and type(major) == str:
        newMajor = ""
        newMajor = major + ", " + additionalMajors[majors.index(major)]
        majors[majors.index(major)] = newMajor

# Capitalizing the minors
for minor in minors:
    if type(minor) != float:
        minors[minors.index(minor)] = minor.title()

# Capitalizing high schools
for highSchool in highSchools:
    if type(highSchool) != float:
        highSchools[highSchools.index(highSchool)] = highSchool.title()


# Capitalizing bootcamps
for bootcamp in bootcamps:
    if type(bootcamp) != float:
        bootcamps[bootcamps.index(bootcamp)] = bootcamp.title()

# Capitalizing cities
for city in cities:
    if type(city) != float:
        cities[cities.index(city)] = city.title()


cleanedDicts = {'First Name': firstNames, 'Last Name': lastNames, 'Phone Number': phoneNumbers, 'Email': emails, 'Pronouns': pronouns, 
'Current Level of Study': levelOfStudy, 'Employment Status': employmentStatus, 'College': universities, 'Major': majors, 'Other': additionalMajors, 'Minor': minors, 
'High School': highSchools, 'Bootcamp Program': bootcamps, 'Country of Residence': countries, 'State': states, 
'City': cities, 'Resume': resumes, 'LinkedIn': linkedIn}

cleanedDf = pd.DataFrame.from_dict(cleanedDicts)

cleanedDf.to_csv("cleanedData.csv", index = "False")



