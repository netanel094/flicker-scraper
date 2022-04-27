import mysql.connector

# This function build the database and the image table
def create_data_base (Urls, Date_scrape, Keyword):

    # connect to MySQL server
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234"
    )

    #craate the database
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE flicker")
    mycursor.execute("SHOW DATABASES")

    for x in mycursor: # Test
        print(x)

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="flicker"  # Adding the database name
    )

    print(mydb)
    mycursor = mydb.cursor()

    # Create 'images' table
    mycursor.execute("CREATE TABLE images (imageUrl VARCHAR(255), scrapeTime DATETIME, keyword VARCHAR(255) )")

    # insert the data in 'images' table
    for i in range(len(Urls)):
        sql = "INSERT INTO images (imageUrl, scrapeTime,keyword) VALUES (%s, %s, %s)"
        vals = (Urls[i], Date_scrape[i],Keyword)
        mycursor.execute(sql, vals)
        mydb.commit()



# method 2
def search(minScrapeTime, maxScrapeTime,keyword,size):

    # connect to MySQL server
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database = "flicker"
    )
    print(mydb)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM images WHERE (scrapeTime BETWEEN %s AND %s) AND keyword = %s LIMIT %s",(minScrapeTime,maxScrapeTime,keyword,size))
    myresult = mycursor.fetchall()
    for x in myresult: # Checking
        print(x)

    return myresult #Returns all rows that meet the conditions


