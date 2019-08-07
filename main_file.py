import sqlite3

#Create database if not exist and get a connection to it
connection = sqlite3.connect('AFMDB/AFM.db')

# Get a cursor ro execute sql statements
cursor = connection.cursor()


