# extract man's words and others' words repectively
import os
os.getcwd()
os.chdir("E:\documents")
man = []
other = []
data = open('sketch.txt')
try:
  data = open('sketch.txt')
  for each_line in data:
    try:
       (role, line_spoken) = each_line.split(':', 1)
       line_spoken = line_spoken.strip() #The “strip()” method removes unwanted whitespace from a string
       if role == 'Man':
         man.append(line_spoken) # add white-space-removed string to man
       elif role == 'Other Man':
         other.append(line_spoken)
    except ValueError:
       pass
  data.close()
except IOError:
  print('The datafile is missing!')
print(man)
print(other)
# Open your file in write mode

try:
    man_file = open("man_data.txt", "w") #  open your files in write mode and w means write mode (in your current dir)
    other_file = open("other_data.txt", "w")
# Use the “print()” BIF to save the named lists to named disk files.
    print(man,file=man_file)
    print(other, file=other_file)
except IOError:
    print("File error.")
finally:
    man_file.close()
    other_file.close() # it is importan to close file
# in case that there is something woring with the codes under try we put it under the finally
# The finally suite is always executed no matter what exceptions occur within a try/except statement.

# open a non-exist file
try:
  data = open('missing.txt')
  print(data.readline(), end='')
except IOError as err: # show your error message
  print('File error: ' + str(err)) # make sure err is a string
finally:
  if 'data' in locals(): # The “in” operator tests for membership.
    data.close()

# with open
try:
  with open('its.txt', "w") as data: # when you use with open, you no longer have to worry about closing any opened files
    print("It's...", file=data)
except IOError as err:
  print('File error: ' + str(err))

# change the previous code
try:
  with open("man_data.txt", "w") as man_file:
    print(man, file=man_file)
  with open("other_data.txt", "w") as other_file:
    print(other, file=other_file)
except IOError as err:
  print("File error: " + str(err))
# sometimes we can combine 2 with open
with open("man_data.txt", "w") as man_file, open("other_data.txt", "w") as other_file:
  print(man, file=man_file)
  print(other, file=other_file)

# Use a with statement to open your data file and display a single line from it:
with open('man_data.txt') as mdf:
  print(mdf.readline())

# change the txt in a format to look better
import sys
def print_lol(the_list, indent=False, level=0, fh = sys.stdout): # add fh to identify a place to write your data to
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file= fh)
            print(each_item, file=fh)
print_lol(man)

# pickle your data
import pickle
...
with open('mydata.pickle', 'wb') as mysavedata: # create a mysavedate named as mydata.pickle
    # b in wb meansThe “b” tells Python to open your data files in BINARY mode.
  pickle.dump([1, 2, 'three'], mysavedata) # To save your data, use “dump()”.
...
with open('mydata.pickle', 'rb') as myrestoredata:
  a_list = pickle.load(myrestoredata) # Restore your data from your file using “load()”.
print(a_list)


try:
  with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
      pickle.dump(man, man_file)
      pickle.dump(other, other_file)
except pickle.PickleError as perr:
  print('Pickling error: ' + str(perr))
# in this way, Python’s pickle module uses a custom binary format (known as its protocol)
# viewing this format in your editor looks decidedly weird.

# if u want to unpickle your file
new_man = []
try:
  with open('man_data.txt', 'rb') as man_file:
    new_man = pickle.load(man_file)
except IOError as err:
  print('File error: ' + str(err))
except pickle.PickleError as pernr:
  print('Pickling error: ' + str(pernr))

print(new_man)
