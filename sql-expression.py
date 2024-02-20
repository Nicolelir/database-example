from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# --1-- executing the instructions from our localhost "chinook" db (linkl python file to chinook)
db = create_engine("postgresql:///chinook") #db=database, locally

meta = MetaData(db)#metaData class will contain a collection of our table objects, and the associated data within those objects.

# --2-- create variable for "Artist" table
artist_table = Table(
    "artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("name", String)
)

# --2--create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# --2--create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# --3-- making the connection, Before we start to query the database, we need to construct our tables
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    #select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)