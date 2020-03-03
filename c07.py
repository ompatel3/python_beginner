import os
os.chdir("E:\documents")
import pickle
class athleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([]) # it is a list
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)

    @property
    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return(athleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print("file erro" + str(ioerr))
        return (None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = [ath.dob, ath.top3]
    try:
        with open('athletes.pickle', 'wb') as athf:
             pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store): ' + str(ioerr))
    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
             all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('Fileerror(get_from_store): ' + str(ioerr))
    return (all_athletes)

the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
print(data)
for each_athlete in data:
   print(each_athlete, data[each_athlete][0])
# or load from athf
data_copy = get_from_store()
for each_athlete in data_copy:
    print(each_athlete, data_copy[each_athlete][0])

