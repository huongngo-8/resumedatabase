# import
import pandas as pd
import os 

checkInData = "dummydata.csv"
resumeData = "Repeat Verification.csv"


checkInDf = pd.read_csv(checkInData)
resumeDf = pd.read.csv(resumeData)

checkInDict = checkInDf.to_dict('list')
resumeDict = resumeDf.to_dict('list')

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
    # University (Other)
universityOther = checkInDict['Name of University (Other)']
    # Majors
majors = checkInDict['What is your major?']
    # Other Majors
otherMajors = checkInDict['If applicable, what are your other major(s)?']
    # Minors
minors = checkInDict['If applicable, what are your minor(s)?']
    # Majors (Others, not in MLH)
majorsOther = checkInDict['Major (Other)']
    # Name of High School
highSchools = checkInDict['Name of High School']
    # Name of Bootcamp Program
bootcamps = checkInDict['Name of Bootcamp Program']
    # Title/Company
titleCompany = checkInDict['Title and Company']
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


def wordReformatting(string):
    if string[0].islower():
        string[0].upper
    
    if not string[1:].islower():
        string[1:].lower

    return string

def emailReformatting(email):
    if not email.islower():
        email.lower
        
    return email

def stringReplacement(string, column):
    if string.find(" ") != -1:
        otherWords = string.split(" ")
        for word in otherWords:
            newWord = wordReformatting(word)
            newString = newString + " " + newWord
            newString = newString[1:]
    else:
        newString = wordReformatting(string)
    column[column.index(string)] = newString

    return column

for firstName in firstNames:
    newFirstName = wordReformatting(firstName)
    firstNames[firstNames.index(firstName)] = newFirstName
for lastName in lastNames:
    newLastName = wordReformatting(lastName)
    lastNames[lastNames.index(lastName)] = newLastName

for email in emails:
    newEmail = emailReformatting(email)
    emails[emails.index(email)] = newEmail

for university in universities:
    if university == "Other":
        otherUniversity = universityOther[universities.index(university)]
        if not otherUniversity.isnan():
            stringReplacement(otherUniversity, universities)

for major in majors:
    index = majors.index(major)
    if major == "Other":
        majorOther = majorsOther[index]
        otherMajor = otherMajors[index]
        if not majorOther.isnan():
            stringReplacement(majorOther, majors)
    
    # Check for entry in "If applicable, what are your other major(s)" column (adjacent)
        # If entry not blank - NEED TO DOUBLE CHECK THIS, NOT SURE IF DICTIONARY OF COLUMN WILL SHOW BLANKS OR NOT ACCOUNT FOR BLANK ENTRIES AT ALL
            # wordReformatting(word) - word is Major (Other) entry
                # Check if first character of each word (separated by " " or ",") is upper case, and remaining characters is lower case
                    # Reformat each "word" so that first character is capital and remaining is lower case
    # Concatenate the string from  "If applicable, what are your other major(s)" column with the string from the Major column and permanently add to the Major column
    if not otherMajor.isnan():
        if otherMajor.find(" ") != -1:
            otherMajorWords = otherMajor.split(" ")
            for word in otherMajorWords:
                new_word = wordReformatting(word)
                new_major = new_major + " " + new_word
                new_major = new_major[1:]
        else:
            new_major = wordReformatting(otherMajor)
        majors[index] = majors[index] + ", " + new_major

for minor in minors:
    stringReplacement(minor, minors)

for highSchool in highSchools:
    stringReplacement(highSchool, highSchools)

for bootcamp in bootcamps:
    stringReplacement(bootcamp, bootcamps)

for city in cities:
    stringReplacement(city, cities)

# OUTPUT PROCESSING

cleanedDicts = {'First Name': firstNames, 'Last Name': lastNames, 'Phone Number': phoneNumbers, 'Email': emails, 'Pronouns': pronouns, 
'Current Level of Study': levelOfStudy, 'Employment Status': employmentStatus, 'College': universities, 'Major': majors, 'Minor': minors, 
'High School': highSchools, 'Bootcamp Program': bootcamps, 'Title and Company': titleCompany, 'Country of Residence': countries, 'State': states, 
'City': cities, 'Resume': resumes, 'LinkedIn': linkedIn}

cleanedDf = pd.DataFrame.from_dict(cleanedDicts)

cleanedDf.to_csv("cleanedData.csv", index = "False")

