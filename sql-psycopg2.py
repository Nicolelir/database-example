import psycopg2


# --1-- connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# --2-- build a cursor object of the database
cursor = connection.cursor()

# --6-- Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "Name" column from the "Artist" table
#cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "album" WHERE "artistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])


# --3 -- fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# --4-- close the connection
connection.close()

# --5-- print results
for result in results:
    print(result)


