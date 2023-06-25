import json, datetime
import urllib.request
from bs4 import BeautifulSoup
import re
import mysql.connector


# reading database connection credentials from json file
serverf = open("server.json", "r")
server = json.load(serverf)
serverf.close()


def crawlbookdata():
    try:
        booklist = []

        # target website url
        url = "https://book.douban.com/top250"
        # adding headers to simulate browser
        headers = {"User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

        while True:
            # request and fetch data from url
            print(f'request and read data......\nsource: {url}')
            request = urllib.request.Request(url=url, headers=headers)
            result = urllib.request.urlopen(request)
            data = result.read().decode("utf-8")

            # analysing html data
            print("analysing html file......")
            bs = BeautifulSoup(data, "html.parser")

            for table in bs.find_all("table"):
                bookname = table.find('div', class_="pl2").a.text.replace("\n","").replace(" ","")
                bookinfo = table.find('p', class_="pl").string.split(" / ")
                try:
                    price = float(re.findall(r'\d+.\d+', bookinfo[-1])[0])
                except IndexError:
                    price = float(re.findall(r'\d+', bookinfo[-1])[0])
                publishdate = bookinfo[-2]
                publisher = bookinfo[-3]
                writerlist = bookinfo[:-3]
                writer = " / ".join(writerlist)
                rating = float(table.find('span', class_="rating_nums").text)
                comments = int(re.findall(r'\d+', table.find('span', class_="pl").text)[0])

                booklist.append({
                    "bookname": bookname,
                    "writer": writer,
                    "publisher": publisher,
                    "publishdate": publishdate,
                    "price": price,
                    "rating": rating,
                    "comments": comments
                })
                print(f'book info fetched')
                print(f'bookname: {bookname}\nwriter: {writer}\npublisher: {publisher}')
                print(f'publish data: {publishdate}\nprice: {price}\nrating: {rating}\ncomments: {comments}\n')

            try:
                url = bs.find('div', class_="paginator").find('span', class_="next").a.attrs["href"]
            except AttributeError:
                print("All book info fetched......\n")
                break


        # connecting database
        print("connecting database......")
        db = mysql.connector.connect(
                host=server["host"],
                port=server["port"],
                user=server["user"],
                password=server["password"],
                database="grantit_codetest"
        )
        cursor = db.cursor()
        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") 


        # ddd fetched book info to database
        print("Adding fetched book info to database......\n")
        for book in booklist:
            try:
                query = "INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                val = (book["bookname"], book["writer"], book["publisher"], book["publishdate"],
                    book["price"], book["rating"], book["comments"], now)
                cursor.execute(query, val)
            except mysql.connector.errors.IntegrityError as e:
                if str(e).find("Duplicate entry") != -1 and str(e).find("book.PRIMARY") != -1:
                    query = f'UPDATE book \
                            SET bookname = "{book["bookname"]}", \
                                writer = "{book["writer"]}", \
                                publisher = "{book["publisher"]}", \
                                publish_date = "{book["publishdate"]}", \
                                price = {book["price"]}, \
                                rating = {book["rating"]}, \
                                comments = {book["comments"]}, \
                                lastupdate = "{now}" \
                            WHERE bookname = "{book["bookname"]}";'
                    cursor.execute(query)
                else:
                    print(f'unknown error: {str(e)}\n')
                    print(f'error book info:')
                    print(f'bookname: {book["bookname"]}\nwriter: {book["writer"]}\npublisher: {book["publisher"]}')
                    print(f'publish data: {book["publishdate"]}\nprice: {book["price"]}\nrating: {book["rating"]}\ncomments: {book["comments"]}\n')
                    raise mysql.connector.errors.IntegrityError(e)
        db.commit()


        # execute data cleaning process
        query = f'DELETE FROM book \
                WHERE lastupdate != "{now}";'
        print("executing data cleaning process......")
        cursor.execute(query)
        db.commit()
        print("data cleaning process complete!!!\n")

        db.close()

        print("TOP250 book info fetch/update complete!!!\n")
        return {"status": "TOP250 book info fetch/update complete!!!"}
    
    except Exception as e:
        print(str(e))
        return {"status": "unknown error, please check log infomation"}


def getbookdata():
    # connecting database
    print("connecting database......")
    db = mysql.connector.connect(
            host=server["host"],
            port=server["port"],
            user=server["user"],
            password=server["password"],
            database="grantit_codetest"
    )
    cursor = db.cursor()

    # fetched book info to database
    print("fetching all book info from database......\n")
    query = "SELECT * FROM book;"
    cursor.execute(query)
    result = cursor.fetchall()

    db.close()
    return {"data": result}


def getupdatetime():
    # connecting database
    print("connecting database......")
    db = mysql.connector.connect(
            host=server["host"],
            port=server["port"],
            user=server["user"],
            password=server["password"],
            database="grantit_codetest"
    )
    cursor = db.cursor()

    query = "SELECT MAX(lastupdate) FROM book;"
    cursor.execute(query)
    result = cursor.fetchall()

    db.close()
    return {"data": result[0][0]}


def deletebookdata():
    # connecting database
    print("connecting database......")
    db = mysql.connector.connect(
            host=server["host"],
            port=server["port"],
            user=server["user"],
            password=server["password"],
            database="grantit_codetest"
    )
    cursor = db.cursor()

    query = 'DELETE FROM book WHERE bookname != "";'
    cursor.execute(query)
    db.commit()

    db.close()
    return {"status": "all book data cleared in database!!!"}