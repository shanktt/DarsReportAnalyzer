import pandas as pd
import re
import sys

df = pd.read_csv('uiuc-course-catalog.csv')

def main(course, lnum, hnum, not_allowed):
    courses = df.loc[df['Subject'] == course]
    text = ''
    for index, row in courses.iterrows():
        if ((lnum*100) <= row['Number'] <= (hnum*100)+100):
            if (str(row['Number']) not in not_allowed):
                text += row['Subject'] + ' ' + str(row['Number']) + ', '
    print (text)
    text = text[:2]

if __name__ == "__main__":
    not_allowed = sys.argv[4:]
    not_allowed = not_allowed[1::2]
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), not_allowed)
