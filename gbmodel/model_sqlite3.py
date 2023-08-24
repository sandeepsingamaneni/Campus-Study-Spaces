"""
A simple campus study spaces flask app.
Data is stored in a SQLite database that looks something like the following:

+------------------------+-------------------+--------------+-------------+----building_id  | building_name          | building_code   | building_floor | room_number | rating |
+============+==================+============+----------------+---------------
       1     |Engineering Building   |     EB              | lower level    | 93          | 4/5
+------------+------------------+------------+----------------+----------------

This can be created with the following SQL (see bottom of this file):

    create table study_spaces (building_id integer, building_name string, building_code string, building_floor string, room_number integer, rating string);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from study_spaces")
        except sqlite3.OperationalError:
            cursor.execute("create table study_spaces (building_id integer, building_name string, building_code string, building_floor string, room_number integer, rating string)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains:building_id,building_name,building_code,building_floor,closest_room_number, rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM study_spaces")
        return cursor.fetchall()

    def insert(self,building_id, building_name,building_code,building_floor,room_number,rating):
        """
        Inserts entry into database
        :param building_id:Integer
        :param building_name: String
        :param building_code: String
        :param building_floor: String
        :param room_number: Integer
        :param rating: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'building_id':building_id, 'building_name':building_name, 'building_code':building_code,'building_floor':building_floor, 'room_number':room_number, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into study_spaces (building_id, building_name, building_code,building_floor, room_number, rating) VALUES (:building_id, :building_name, :building_code, :building_floor, :room_number, :rating)", params)

        connection.commit()
        cursor.close()
        return True

    def delete(self,building_id,building_name,building_code,building_floor,room_number,rating):
        """
        Deletes entry from database
        :param building_id:Integer
        :param building_name: String
        :param building_code: String
        :param building_floor: String
        :param room_number: Integer
        :param rating: String
        :return: True
        :raises: Database errors on connection and deletion
        """
        params = {'building_id':building_id, 'building_name':building_name, 'building_code':building_code,'building_floor':building_floor, 'room_number':room_number, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("delete from study_spaces where (building_id=:building_id)", params)

        connection.commit()
        cursor.close()
        return True

    def update(self,building_id,building_name,building_code,building_floor,room_number,rating):
        """
        updates entry in database
        :param building_id:Integer
        :param building_name: String
        :param building_code: String
        :param building_floor: String
        :param room_number: Integer
        :param rating: String
        :return: True
        :raises: Database errors on connection and deletion
        """
        params = {'building_id':building_id, 'building_name':building_name, 'building_code':building_code,'building_floor':building_floor, 'room_number':room_number, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("update study_spaces set building_id=:building:id,building_name=:building_name,building_code=:building_code, building_floor=:building_floor, room_number=:room_number, rating=:rating where building_id=:building_id", params)

        connection.commit()
        cursor.close()
        return True


    
   

        
 
 
