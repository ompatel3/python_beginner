# creat a list
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)
print(len(cast))
# index from 0-2
print(cast[0])
print(cast[1])
print(cast[2])
# add a single data item to the end of your list by "append"
cast.append("Gilliam")
print(cast)
# remove a single data item to the end of your list by "pop"
cast.pop()
print(cast)
# add a collection of data items to the end of your list
cast.extend(["Gilliam", "Chapman"])
print(cast)
# remove a specific item
cast.remove("Gilliam")
print(cast)
# insert in a specific item in a speccific place
cast.insert(0, "Chapman")
print (cast)
cast.insert(1,"IG")
print (cast)
# example: insert number behind the movies
cast.insert(1,1)
cast.insert(3,2)
cast.insert(5,3)
cast.insert(7,4)
print(cast)

# for loop
fav_movies = ["The Holy Grail", "The Life of Brian","LGD","EG"]
for each_movie in fav_movies:
    print(each_movie)
#while loop
count=0
while count < len(fav_movies):
    print(fav_movies[count])
    count=count+1

# Store lists within lists
movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman",
["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
print(movies[4][1][3])
for each_item in movies:
  print(each_item)

# isinstance
print(isinstance(movies,list))
names = ['Michael', 'Terry']
isinstance(names, list)
num_names = len(names)
isinstance(num_names, list)

# define denest() to decompose nested list with 2 nested list
def denest(the_list):
    for each_item in the_list:
      if isinstance(each_item, list):
        for nested_item in each_item:
          if isinstance(nested_item, list):
            for deeper_item in nested_item:
              print(deeper_item)
          else:
            print(nested_item)
      else:
        print(each_item)
DOTA2=[1,2,3,[4,4,[5,5,5,[666,888]]]]
denest(DOTA2)

# define print_lol (decompose nested list)
def print_lol(the_list):
    for each_item in the_list:
      if isinstance(each_item, list):
        print_lol(each_item)
      else:
        print(each_item)

print_lol(movies)






