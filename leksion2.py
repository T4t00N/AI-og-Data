#Imports
import sqlite3
from sqlite3 import Error
import os

#Function to delete a file with the same name, to start from scratch.
def delete_existing_db(db_file):
    """ Delete the existing database file to ensure a fresh start. """
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted existing database: {db_file}")
    
#Create connection to a newly created database called "School.db."
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("school.db")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#Use the curser method to read the tables.
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#A function for creating and inserting things into the database.
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_tables():
#Define what the students_table should consist of.
    create_students_table = """
    CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    major TEXT NOT NULL
    );
    """

    #Define what the courses_table should consist of.
    create_courses_table = """
    CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    instructor TEXT NOT NULL
    );
    """

    #Create the Enrollments table, that takes data from both.
    create_enrollments_table = """
    CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    #Create the 3 tables.
    tables = [create_students_table,create_courses_table,create_enrollments_table]
    for table in tables:
        execute_query(connection, table)


def insert_data():

    insert_students = """
    INSERT INTO Students (name, major) VALUES
    ('John Doe', 'Computer Science'),
    ('Jane Smith', 'Biology'),
    ('Alice Johnson', 'Mathematics'),
    ('Bob Brown', 'English'),
    ('Mike Davis', 'Physics');
    """

    insert_courses = """
    INSERT INTO Courses (course_name, instructor) VALUES
    ('Introduction to Programming', 'Dr. Smith'),
    ('General Biology', 'Dr. Johnson'),
    ('Linear Algebra', 'Dr. White'),
    ('British Literature', 'Dr. Black'),
    ('Quantum Mechanics', 'Dr. Brown');
    """

    Enrollments = """
    INSERT INTO Enrollments (student_id, course_id)
    SELECT Students.student_id, Courses.course_id FROM Students
    CROSS JOIN Courses;
    """
    
    school_data = [insert_students,insert_courses,Enrollments]
    for data in school_data:
        execute_query(connection, data)

def get_courses_by_student_id(connection, student_id):
    """ Fetch and print all courses attended by the given student ID. """
    query = f"""
    SELECT 
        Students.name,
        Courses.course_name,
        Courses.instructor
    FROM 
        Students 
    JOIN 
        Enrollments ON Students.student_id = Enrollments.student_id
    JOIN 
        Courses ON Enrollments.course_id = Courses.course_id
    WHERE 
        Students.student_id = {student_id};
    """
    courses = execute_read_query(connection, query)
    if courses:
        print(f"Courses attended by Student ID {student_id}:")
        for course in courses:
            print(f"Course Name: {course[1]}, Instructor: {course[2]}")
    else:
        print("No courses found for this student.")

def get_students_by_course_id(connection, course_id):
    """ Fetch and print all students enrolled in the given course ID. """
    query = f"""
    SELECT 
        Courses.course_name,
        Students.name,
        Students.major
    FROM 
        Courses 
    JOIN 
        Enrollments ON Courses.course_id = Enrollments.course_id
    JOIN 
        Students ON Enrollments.student_id = Students.student_id
    WHERE 
        Courses.course_id = {course_id};
    """
    students = execute_read_query(connection, query)
    if students:
        print(f"Students enrolled in Course ID {course_id}:")
        for student in students:
            print(f"Student Name: {student[1]}, Major: {student[2]}")
    else:
        print("No students found for this course.")

#Path to the database file.
db_file = "school.db"

#Delete the existing database file if it exists.
delete_existing_db(db_file)

#Create new connection.
connection = create_connection()
#Create the tables.
create_tables()
#Insert the school data.
insert_data()

#Select student to retrieve information about(Student_id)
#get_courses_by_student_id(connection, 3)
#Select course to get information about students in it(Course_id)
get_students_by_course_id(connection, 3)
