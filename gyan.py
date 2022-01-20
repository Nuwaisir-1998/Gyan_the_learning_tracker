import datetime
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('learned_stuff', type=str, nargs=1)
parser.add_argument('-m', type=str, nargs='*', default='')

args = parser.parse_args()

mydate = datetime.datetime.now()
cur_month = mydate.strftime("%B")
cur_year = mydate.strftime("%Y").lower()
cur_week = mydate.strftime("%A").lower()

this_dir = 'C:/Home/Projects/Command_line_tool/'

exists = False
try:
    os.mkdir(this_dir + 'Learnings/' + cur_month + '_' + cur_year)
except:
    pass
file_name = this_dir + 'Learnings/' + cur_month + '_' + cur_year + '/' + cur_week + '.csv'
# print(file_name)
f = open(file_name, 'a')
f.close()

with open(file_name, 'r') as f:
    for row in f.readlines():
        if row.split(',')[0] == args.learned_stuff[0]:
            exists = True
            
if not exists:
    with open(file_name, 'a') as f:
        for words in args.learned_stuff:
            f.write(words + ',' + ' '.join(args.m) + '\n')