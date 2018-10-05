import sqlite3

# connect to the database
conn = sqlite3.connect("songs.db")

# create a cursor to run commands
cur = conn.cursor()

# Ask for values. Students can optionally add exception handling and prompts to continue
name = input("Enter the song name: ")
artist = input("Enter the recording artist: ")
genre = input("Enter the genre of the song: ")
year = int(input("Enter the year the song was released: "))

# insert values into the database
cur.execute("insert into songs(name, artist, genre, year) values (?, ?, ?, ?)",(name, artist, genre, year))

# save the changes
conn.commit()
conn.close()