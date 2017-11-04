import csv
import os
filename = input("what is the name of the exported CSV file: ")
print(filename)
with open(filename,'r') as f:
    reader = csv.reader(f)
    next(f)
    next(f)
    for row in reader:
        date = row[0]
        hour = row[2]
        minute = row[3]
        level = row[4]
        levelText = row[5]
        comment = row[6]
        dateWithTime = '{0} {1}:{2}'.format(date,hour,minute)
        text = '''
## DayScore: *{0} {1}*
{2}


Imported from iMoodJournal
'''.format(level,levelText,comment)
        s = 'dayone2 --date="{0}" new "{1}"'.format(dateWithTime,text)
        os.system(s)
