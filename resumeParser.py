from resume_parser import resumeparse
import os
import pandas as pd
path = "/Users/huongngo/resumedatabase/Resumes"
file_list = sorted(os.listdir(path))
size = 0
for file in file_list:
    f = os.path.join(path, file)
    print(f)
    if os.path.isfile(f):
        print(file)
        data = resumeparse.read_file(f)
        data['file'] = file
        print(data)
        size += 1
        print(size)
        df = pd.DataFrame(list(data.items()))
        df.to_csv('resumes.csv', mode='a', header=['key', 'values'], index=False)
# steps:
# loop through list of the resume files
# get name of file
# pass name of file through resumeparser
# convert dictionary to dataframe
# append data frame to csv file


