
import mysql.connector

class QuotetutorialPipeline:
    def __init__(self):
        self.connect_mysql()

    def connect_mysql(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="quannguyen2004",
            database="datacrawl"
        )
        self.mycur = self.mydb.cursor()
        self.create_table()

    def create_table(self):
        self.mycur.execute("drop table if exists book")
        self.mycur.execute("CREATE TABLE IF NOT EXISTS book (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(200), author VARCHAR(100), tags Varchar(200))")

    def process_item(self, item, spider):
        self.insert_mysql(item)
        return item

    def insert_mysql(self,item):
        self.value = (
            item["title"],
            item["author"],
            ", ".join(item["tags"]) if item["tags"] else None
        )
        self.mycur.execute("INSERT INTO book (title, author,tags) VALUES (%s, %s,%s)", self.value)
        self.mydb.commit()