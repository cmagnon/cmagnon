movies = ["movie1","movie2","movie3",["actor1","actor2","actor3",[1,2,3,4]]]
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
for eachMovie in movies:
    if isinstance(eachMovie, list):
        for nestedItem in eachMovie:
            if isinstance(nestedItem, list):
                for deepNestedItem in nestedItem:
                    print(deepNestedItem)
            else:
                print(nestedItem)
    else:
        print(eachMovie)

def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)

print('PART 2 ------------------------------')
print_lol(movies)
