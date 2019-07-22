# This is a simple example related to list processing

movies = ["The next three days", "The man who knew infinity", "Armaddegon"]

print("Print the lenght of the list")
print(len(movies))

print("Print all the movies present in the list")
print(movies)
print("\n")

print("Print the First movie in the list")
print(movies[0])
print("\n")

print("Print the last movie in the list")
print(movies[2])
print("\n")

print("Print the second movie in the list")
print(movies[1])
print("\n")

fav_movies = ["StarDust", "Fast and Furious", "The girl next door"]

print("Extend the movies list")
movies.extend(fav_movies)
print(movies)

print("Append a adhoc movie to the list")
movies.append("Bourne legacy")
print(movies)

print("Remove a particular movie")
movies.remove("StarDust")
print(movies)

print("Remove the last movie from the list")
movies.pop()
print(movies)

print("Insert movie before a specified data location")
movies.insert(0, "Interstellar")
print(movies)

