# Gyan (জ্ঞান) The Learning Tracker
This is a command line based learning tracker application. We learn many things
on a daily basis, but we tend to forget those pretty fast. So, we can write down
in a file or a note book each of the learned things and maybe revisit those to
remind what it was. So, to write these down super fast, just by opening the terminal
and writing the words, you can use the Gyan app. It will organize these notes by
creating folders named as the current year, and file name as the current
month.

## Installation
0. Change the value of ```this_dir``` variable in ```gyan.py``` to the path of the directory
that the ```gyan.py``` is currently in.
1. First install pyinstaller
```
pip install pyinstaller
```
2. Move to the folder where the ```gyan.py``` file is, and run:
```
pyinstaller --onefile gyan.py
```
3. A folder named ```dist``` will be created where the executable will be in.
4. Add the path of the ```dist``` folder to your environment variable path.

## Usage
You can just open the terminal and type
```
gyan [learned_stuff]
```
It will add the ```[learned_stuff]``` to a csv file named after the current month which
will be in a folder named after the year.
You can also add a message about the ```[learned_stuff]``` like the following:
```
gyan [learned_stuff] -m "This is a message"
# Quotations are not necessary
```

The application won't add a keyword more than once.