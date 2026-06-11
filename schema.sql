CREATE TABLE IF NOT EXISTS genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL,
    genre_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ratings (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    review TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);
