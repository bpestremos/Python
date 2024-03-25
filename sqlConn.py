import pyodbc


conn = pyodbc.connect(
     "Driver={SQL Server Native Client 11.0};"
     "Server=(LocalDB)\\LocalDB;"
     "Database=Python;"
     "Trusted_Connection=no;"
     ""
)

print("connection established")
