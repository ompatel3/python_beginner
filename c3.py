import os  # Import “os” from the Standard Library.
os.getcwd()  # What’s the current working directory?
os.chdir("E:\documents")  # Change to the folder that contains your data file.
os.getcwd()  # Confirm you are now in the right place
data = open('sketch.txt')  # Open a named file and assign the file to a file object called “data”.
print(data.readline(), end='') #Use the “readline()” method to grab a line from the file, then use the “print()” BIF to display it on screen.
print(data.readline(), end='')
data.seek(0)   # Use the “seek()” method to return to the start of the file.
for each_line in data:
  print(each_line, end='')  # it’s a standard iteration using the file’s data as input.
data.close()  # Since you are now done with the file, be sure to close it.
# split the data by ":"
data = open('sketch.txt')
help(each_line.split)
# find() You can ask find() to try and locate a substring in another string
# if it can’t be found, the find() method returns the value -1
each_line = "I tell you, there's no such thing as a flying circus."
print(each_line.find(':'))
each_line = "I tell you: there's no such thing as a flying circus."
print(each_line.find(':')) # return the index of ":"

for each_line in data:
    if not each_line.find(':') == -1:
      (role, line_spoken) = each_line.split(':',1)  # 1 make sure there are possibably 2 ":" in a sentence.
# A list of target identifiers on the left…,
# …“line_spoken”: is assigned the string “Is this the right room for an argument?”
      print(role, end='')
      print(' said: ', end='')
      print(line_spoken, end='')
data.close()

## using exception handler to ignore the runtime error
data = open('sketch.txt')
for each_line in data:
  try:
    (role, line_spoken) = each_line.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')
  except:
    pass
data.close()

# what if we do not know whether the data file exists
# method 1
import os
if os.path.exists('sketch.txt'):
     data = open('sketch.txt')
     for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
     data.close()
else:
  print('The data file is missing!')

# Or add another level of exception handling
import os
try:
    data = open('sketch.txt')
    for each_line in data:
      if not each_line.find(':') == -1:
       (role, line_spoken) = each_line.split(':', 1)
       print(role, end='')
       print(' said: ', end='')
       print(line_spoken, end='')
    data.close()
except:
   print('The data file is missing!')

# final version (spcificify error type)
import os
try:
    data = open('sketch.txt')
    for each_line in data:
      try:
         (role, line_spoken) = each_line.split(':', 1)
         print(role, end='')
         print(' said: ', end='')
         print(line_spoken, end='')
      except ValueError:
          pass
    data.close()
except IOError:
   print('The data file is missing!')
# A ValueError occurs when your data does not conform to an expected format.
# An IOError occurs when your data cannot be accessed properly (e.g., perhaps your data file has been moved or renamed).