import os
os.getcwd()
os.chdir("E:\documents")
# seantinize : seperate the time_string by "."
def santinize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return(time_string)
    (mins , secs) = time_string.split(splitter,1)
    return(mins + "." + secs)
# open the txt file and turn it into a list instead of using "," to seperate the elements
def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(","))
    except IOError as ioerr:
        print("file erro:" + str(ioerr))
        return(none)
# find the fastest times
sarah = get_data("sarah2.txt")
print(sarah)
(sarah_name,sarah_job) = sarah.pop(0), sarah.pop(0)
print(sarah_name)
print(sarah_job)
print(sarah_name + "'s fastest times are: " + str(sorted(set([santinize(t) for t in sarah]))[0:3]))

# dictionary
cleese = {}
palin = dict()
type(cleese)
type(palin)
# Provide the data associated with the new key
cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}
print(palin['Name'])
print(palin['Occupations'])
# a Python dictionary does not maintain insertion order
cleese['Occupations'][-2]
palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"
print(cleese)

# uses a dictionary to hold and process Sarah’s data.
sarah = get_data("sarah2.txt")
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data)
print(sarah_data['Name'] + '’s fastest times are: ' + str(sorted(set([santinize(t) for t in sarah_data['Times']]))[0:3]))

# uses a dictionar in get_data function
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return({"names":templ.pop(0),"DOB":templ.pop(0),'Times':str(sorted(set([santinize(t) for t in templ]))[0:3])})
    except IOError as ioerr:
        print("file erro" + str(ioerr))
        return (None)

print(get_coach_data("sarah2.txt"))


# define a class
class Athlete:
    def __init__(self, a_name, a_dob= None, a_times = []):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
print(sarah.name)
print(sarah.dob)
print(sarah.times)
james = Athlete('James Jones')
print(james.name)
print(james.dob)
print(james.times)

# using class in get_data function
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        sarah = Athlete(templ.pop(0),templ.pop(0),str(sorted(set([santinize(t) for t in templ]))[0:3]))
        return(sarah.name, sarah.dob, sarah.times)
    except IOError as ioerr:
        print("file erro" + str(ioerr))
        return (None)
print(get_coach_data("sarah2.txt"))

# or
def get_coach_data_2(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return(Athlete(templ.pop(0),templ.pop(0),str(sorted(set([santinize(t) for t in templ]))[0:3])))
    except IOError as ioerr:
        print("file erro" + str(ioerr))
        return (None)
sarah2 = get_coach_data_2("sarah2.txt")
print(sarah2.name, sarah2.dob, sarah2.times)

# add more function in class
class Athlete:
    def __init__(self, a_name, a_dob= None, a_times = []):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([santinize(t) for t in self.times]))[0:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, time_list):
        self.times.extend(time_list)

vera = Athlete("Vera Vi")
vera.add_time('1.31')
print(vera.top3())
vera.add_times(["1.37","1.33","1.34"])
print(vera.top3())

# built-in list class
class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
johnny = NamedList("JohnPaul_Jones")
johnny.append("Bass Player")
johnny.extend(['Composer', "Arranger", "Musician"])
print(johnny)
print(johnny.name)

# Because johnny is a list, it’s quite OK to do list-type things to it:
for attr in johnny:
    print(johnny.name + " is a " + attr + ".")

# using built-in list class in get_data function
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(str(sorted(set([santinize(t) for t in self]))[0:3]))
vera = AthleteList('Vera Vi',"2020-2-14")
vera.append('1.31')
print(vera)
print(vera.name)
print(vera.dob)
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())




