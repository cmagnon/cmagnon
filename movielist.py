movies = ["movie1","movie2","movie3",["actor1","actor2","actor3"]]
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
for eachMovie in movies:
    if isinstance(eachMovie,list):
        for item in eachMovie:
            print(item)
    else:
        print(eachMovie)
