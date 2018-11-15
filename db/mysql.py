import MySQLdb

conn = MySQLdb.connect('127.0.0.1', 'article_spider', 'spider', 'article_spider2', charset="utf8",
                       use_unicode=True)
cursor = conn.cursor()

insert_sql = """
        INSERT INTO articles(title, url, create_date, fav_num, content) VALUES (%s, %s, %s, %s, %s)
        """

item = {
    'title': 'Title',
    'url': 'Url',
    'create_date': 'Create Date',
    'fav_num': 'Fav Num',
    'content': 'Content'
}
cursor.execute(insert_sql, (item['title'], item['url'],
                            item['create_date'], item['fav_num'], item['content']))
conn.commit()
