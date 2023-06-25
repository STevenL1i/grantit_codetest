# grantit_codetest
clone this repo with command:
git clone https://github.com/STevenL1i/grantit_codetest.git

this code test is developed under:
System: Linux (CentOS 8)
python: 3.9.6
database: MySQL 8.0.26 (Linux)


this program required:
    Python 3.9.6
    MySQL 8.0
        (need to prepare an account has full privileges in advanced, and make it can login)
    httpd service
        (need to config and start the service in advance, especially firewall config to open 8080 and 9001 port)

required additional python module:
    urllib
    bs4
    Flask
    mysql.connector


How to run this program:
1. edit MySQL login credentials:
    - copy "server_example.json" to "server.json"
    - change login credentials in "server.json"

2. initializa MySQL database
    login to your MySQL server
    execute command "source init.sql"

3. initialize web page
    Linux: 
        - run "cp grantit.* /var/www/html/" command
        - access the web page through http service
          (e.g. http://yourserverip:httpdserviceport/grantit.html)
    Windows:
        just directly open "grantit.html" file

4. launch backend server
    execute python script "server.py"

5. then you can open the webpage to crawl, view and clear data



Notes during the code test:
I have little experience on backend web development in my own small project, but until this code test I had no experience on python crawler, so it took me some time to search for tutorial to make it run.