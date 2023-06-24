# grantit_codetest
this code test is developed under:
System: Linux
python: 3.9.6
database: MySQL 8.0.26 (Linux)


this program required:
    Python 3.9.6
    MySQL 8.0 
        (you need to prepare an account has full privileges in advanced, and make it can login)

required additional python module:
    urllib
    bs4
    mysql.connector


How to run this program:
1. edit MySQL login credentials:
    - copy "server_example.json" to "server.json"
    - change login credentials in "server.json"

2. initializa MySQL database
    execute "source init.sql" in MySQL server

3. run "main.py" python script
