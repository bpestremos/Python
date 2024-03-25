import pyodbc
from datetime import datetime

def READ(conn):
    cursor = conn.cursor()
    cursor.execute("select * from Employees")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))  # Convert each row to a dictionary
    return result


def CREATE(conn):
    print("POST")
    cursor = conn.cursor()
    employee_data = [
        (1001, 'John', 'Doe', 'Smith', datetime.now()),
        (1002, 54345, 'Doe', 'Mary', datetime.now())
    ]

    print(f"Posting data: {employee_data}")
    # SQL query to insert records into the Employees table
    insert_query = '''
        INSERT INTO Employees (EmployeeId, FirstName, LastName, MiddleName, DateUploaded)
        VALUES (?, ?, ?, ?, ?)
    '''

    # Executing the insert query for each record
    for employee in employee_data:
        cursor.execute(insert_query, employee)

    conn.commit()
    cursor.execute('SELECT top 1 * FROM Employees order by ID desc')
    for row in cursor:
        print(f"Data posted. {row}")
    print("END POST")


conn = pyodbc.connect(
     "Driver={SQL Server Native Client 11.0};"
     "Server=(LocalDB)\\LocalDB;"
     "Database=Python;"
     "Trusted_Connection=no;"
     ""
)


# READ(conn)
# CREATE(conn)






