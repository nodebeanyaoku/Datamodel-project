# DROP TABLES

songplay_table_drop = "DROP TABLE songplays;"
user_table_drop = "DROP TABLE users;"
song_table_drop = "DROP TABLE songs;"
artist_table_drop = "DROP TABLE artists;"
time_table_drop = "DROP TABLE time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, 
                                                                start_time timestamp REFERENCES time (start_time), 
                                                                user_id int REFERENCES users (user_id), 
                                                                level varchar,
                                                                song_id int REFERENCES songs (song_id),
                                                                artist_id int REFERENCES artists (artist_id), 
                                                                session_id int, 
                                                                location varchar, 
                                                                user_agent varchar
                                                                );
                                                                """)


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
                                                        first_name varchar,
                                                        last_name varchar,
                                                        gender varchar,
                                                        level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id int PRIMARY KEY,
                                                            title varchar, 
                                                            artist_id int, 
                                                            year int, 
                                                            duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id int PRIMARY KEY,
                                                              location varchar,
                                                              latitude int,
                                                              longitude int);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time int PRIMARY KEY,
                                                        hour int, 
                                                        day int, 
                                                        week int, 
                                                        month int, 
                                                        year int, 
                                                        weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, 
                                                    user_id, 
                                                    level, 
                                                    song_id, 
                                                    artist_id,
                                                    session_id, 
                                                    location, 
                                                    user_agent )
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                                    ON CONFLICT (songplay_id) 
                                                    DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users (user_id,
                                            first_name,
                                            last_name,
                                            gender,
                                            level)
                                            VALUES (%s, %s, %s, %s, %s)
                                            ON CONFLICT (user_id) 
                                            DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id,
                                            title, 
                                            artist_id, 
                                            year, 
                                            duration)
                                             VALUES (%s, %s, %s, %s, %s)
                                            ON CONFLICT (song_id) 
                                            DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id,
                                               location,
                                                latitude,
                                                longitude)
                                                VALUES (%s, %s, %s, %s)
                                                ON CONFLICT (artist_id) 
                                                DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time,
                                          hour, 
                                          day, 
                                          week, 
                                          month, 
                                          year, 
                                          weekday)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s)
                                          ON CONFLICT (start_time) 
                                          DO NOTHING;
""")

# FIND SONGS

song_select = (""" SELECT *
                    FROM songs
                    LIMIT 10;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]