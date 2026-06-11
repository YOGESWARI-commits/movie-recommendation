import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    cursor.executescript(file.read())

conn.commit()


# Add Genre
def add_genre():
    genre_name = input("Enter Genre Name: ")

    cursor.execute(
        "INSERT INTO genres (genre_name) VALUES (?)",
        (genre_name,)
    )

    conn.commit()
    print("Genre Added Successfully!")


# Add Movie
def add_movie():

    movie_name = input("Enter Movie Name: ")

    print("\nAvailable Genres:")

    cursor.execute("SELECT * FROM genres")
    genres = cursor.fetchall()

    for genre in genres:
        print(genre)

    genre_id = int(input("Enter Genre ID: "))

    cursor.execute(
        "INSERT INTO movies (movie_name, genre_id) VALUES (?, ?)",
        (movie_name, genre_id)
    )

    conn.commit()
    print("Movie Added Successfully!")

def add_user():

    user_name = input("Enter User Name: ")

    cursor.execute(
        "INSERT INTO users (user_name) VALUES (?)",
        (user_name,)
    )

    conn.commit()

    print("User Added Successfully!")
def rate_movie():

    print("\nAvailable Users:")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    for user in users:
        print(user)

    user_id = int(input("Enter User ID: "))

    print("\nAvailable Movies:")
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    for movie in movies:
        print(movie)

    movie_id = int(input("Enter Movie ID: "))

    rating = int(input("Enter Rating (1-5): "))
    review = input("Enter Review: ")

    cursor.execute("""
        INSERT INTO ratings
        (user_id, movie_id, rating, review)
        VALUES (?, ?, ?, ?)
    """, (user_id, movie_id, rating, review))

    conn.commit()

    print("Rating Added Successfully!")

def top_rated_movies():

    cursor.execute("""
        SELECT movies.movie_name,
               AVG(ratings.rating) as avg_rating
        FROM movies
        JOIN ratings
        ON movies.movie_id = ratings.movie_id
        GROUP BY movies.movie_name
        ORDER BY avg_rating DESC
        LIMIT 10
    """)

    results = cursor.fetchall()

    print("\nTop Rated Movies")

    for movie in results:
        print(movie)
def filter_by_genre():

    print("\nAvailable Genres:")

    cursor.execute("SELECT * FROM genres")
    genres = cursor.fetchall()

    for genre in genres:
        print(genre)

    genre_id = int(input("Enter Genre ID: "))

    cursor.execute("""
        SELECT movie_name
        FROM movies
        WHERE genre_id = ?
    """, (genre_id,))

    movies = cursor.fetchall()

    print("\nMovies in Selected Genre:")

    for movie in movies:
        print(movie[0])
def recommend_movies():

    cursor.execute("""
        SELECT movies.movie_name,
               AVG(ratings.rating) as avg_rating
        FROM movies
        JOIN ratings
        ON movies.movie_id = ratings.movie_id
        GROUP BY movies.movie_name
        HAVING avg_rating >= 4
        ORDER BY avg_rating DESC
    """)

    recommendations = cursor.fetchall()

    print("\nRecommended Movies:")

    for movie in recommendations:
        print(movie)        
# Menu
# Menu
while True:

    print("\n===== Movie Recommendation System =====")
    print("1. Add Genre")
    print("2. Add Movie")
    print("3. Add User")
    print("4. Rate Movie")
    print("5. Top Rated Movies")
    print("6. Filter By Genre")
    print("7. Recommend Movies")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_genre()

    elif choice == 2:
        add_movie()

    elif choice == 3:
        add_user()

    elif choice == 4:
        rate_movie()

    elif choice == 5:
        top_rated_movies()

    elif choice == 6:
        filter_by_genre()

    elif choice == 7:
        recommend_movies()

    elif choice == 8:
        print("Thank You!")
    break