create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl3;
    

    DROP TABLE IF EXISTS petl3.viable_countys;
    
    CREATE TABLE IF NOT EXISTS petl3.viable_countys (
        geo_id int,
        state text,
        county text,
        sales_vector float

        );
 
''')

insert_county = ('''
    INSERT INTO petl3.viable_countys
   VALUES(%s, %s, %s, %s);
''')
insert_t_movie = ('''
    INSERT INTO petl2.t_movie_list (Title)
   VALUES(%s);
''')

