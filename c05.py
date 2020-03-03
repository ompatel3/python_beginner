import os
os.getcwd()
os.chdir("E:\documents")
# string.strip, delete something in the string
data = "A loves B"
print(data.strip("A l"))
print(list(data))
# string.strip().split()
data = "A loves e"
print(data.strip().split("e")) # delete "e" firstly and then seperate the list by "e"
with open("james.txt") as jaf:
 data = jaf.readline()
james = data.strip().split(",") #Convert the data to a list. and
with open("julie.txt") as juf:
 data = juf.readline()
julie = data.strip().split(",")
with open("mikey.txt") as mif:
 data = mif.readline()
mikey = data.strip().split(",")
with open("sarah.txt") as saf:
 data = saf.readline()
sarah = data.strip().split(",")
print(james)
print(julie)
print(mikey)
print(sarah)

# sort data
data = [6, 3, 1, 2, 4, 5]
data[2] = "."
print(data)
 #Perform IN-PLACE sorting on the data.
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
# def sanitize(time_string): to change all : and - to .
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []
for each_t in sarah:
  clean_mikey.append(sanitize(each_t))
for each_t in mikey:
  clean_julie.append(sanitize(each_t))
for each_t in julie:
  clean_james.append(sanitize(each_t))
for each_t in james:
  clean_sarah.append(sanitize(each_t))
print(sorted(clean_james))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
print(sorted(clean_julie))
# or in other way： [sanitize(t) for t in james])
print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in sarah]))
print(sorted([sanitize(t) for t in mikey]))
# remove duplicates
print(james)
unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james)

# set function(Any duplicates in the “james” list are ignored. Cool)
distances = {10.6, 11, 8, 10.6, "two", 7}
print(distances)
distances = set(james)
print(distances)
#To access more than one data item from a list, use a slice. 'set' object is not subscriptable! For example:
distances = [10.6, 11, 8, 10.6, "two", 7]
print(distances[3:6])

# open the txt and sperate by "," (delete"," and then seperate)
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(","))
    except IOError as ioerr:
        print("File error:"+ str(ioerr))
        return (None)
sarah = get_coach_data("sarah.txt")
print(sarah)


