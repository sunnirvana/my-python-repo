import pymongo

"""
安装: pip install pymongo
"""


def print_title(title):
    print('\n ' + title)


"""
链接: pymongo.MongoClient("mongodb://localhost:27017/")
"""
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["test"]

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
# database_names 在最新版本的 Python 中已废弃，Python3.7+ 之后的版本改为了 list_database_names()。
if "test" in dblist:
    print("数据库 test 已存在！")

mydb = myclient['test']
mycol = mydb['sites']
mycol2 = mydb['sites2']

"""
添加数据
insert_one()，返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值
insert_many()，返回 InsertManyResult 对象，该对象包含 inserted_ids 属性，该属性保存着所有插入文档的 id 值。
"""
print_title('插入一条')
mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
# print(mycol.insert_one(mydict))

print_title('插入多条')
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
# print(mycol2.insert_many(mylist))

print_title('指定 _id 插入多条')
mylist2 = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]
# print(mycol2.insert_many(mylist2))

"""
查询数据
find_one(), 查询集合中的一条数据
find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作
find().limit(num) 返回指定条数数据
find().sort() 指定升序或降序, 第一个参数指定要排序的字段, 第二个字段指定排序规则 1升, -1降, 默认为升序

find({},{}) 第二个{}用来查询指定字段的数据，
1. 将要返回的字段对应值设置为 1; find({}, {'name': 1})
2. 如果你设置了一个字段为 0，则其他都为 1，反之亦然。(_id 字段除外), 同时指定了 0 和 1 则会报错; find({}, {'name':0})

find({}, {}) 第一个{}用来指定条件查询,
1. 一般查找; find({'name': 'Facebook'})
2. 高级查找; find({'name': {'$gt': 'H'}})
3. 正则; find()
"""
print_title('find_one()')
print(mycol.find_one())

print_title('find() 查询所有')
for x in mycol2.find():
    print(x)

print_title('find() 指定字段')
for x in mycol2.find({}, {'_id': 0, 'name': 1, 'alexa': 1}):
    print(x)

print_title('find() 隐藏一个字段')
for x in mycol2.find({}, {'name': 0}):
    print(x)

# for x in mycol2.find({}, {'name': 0, 'alexa': 1}):
#     报错 pymongo.errors.OperationFailure: Projection cannot have a mix of inclusion and exclusion.
#     print(x)
print_title('find() 根据指定条件')
for x in mycol2.find({'name': 'Facebook'}):
    print(x)

print_title('find() 高级查找')
for x in mycol2.find({'name': {'$gt': 'H'}}):
    print(x)

print_title('find() 正则查找')
for x in mycol2.find({'name': {'$regex': '^R'}}):
    print(x)

print_title('返回指定条数记录')
for x in mycol2.find().limit(3):
    print(x)

print_title('按alexa升序排列')
for x in mycol2.find().sort('alexa'):
    # TODO: 会将'alexa'不存在的数据参与排序, 需要调查, 如果不存在此字段则应该过滤掉
    print(x)

"""
修改数据
update_one(), 修改文档中的一条记录, 第一个参数为查询条件, 第二个参数为要修改的字段
update_many(), 修改文档中的多条记录, 第一个参数为查询条件, 第二个参数为要修改的字段
"""
print_title('修改一条记录')
xx = mycol2.update_one({'alexa': '10000'}, {'$set': {'alexa': '12345'}})
print(xx.modified_count)

print_title('修改多条记录')
xx = mycol2.update_many({'alexa': {'$regex': '^F'}},
                        {'$set': {'alexa': '123'}})
print(xx.modified_count, xx.raw_result)

"""
删除数据
delete_one(), 删除一条记录, 第一个参数为查询条件
delete_many(), 删除多条记录, 第一个参数为查询条件, 如果第一个参数为{} 则删除所有记录
drop(), 删除集合
"""
print_title('删除一条记录')
xx = mycol2.delete_one({'name': 'Taobao'})
print(xx.deleted_count)

print_title('删除多条记录')
xx = mycol2.delete_many({'name': {'$regex': '^F'}})
print(xx.deleted_count)

print_title('删除所有记录')
xx = mycol2.delete_many({})
print(xx.deleted_count)

print_title('删除集合')
xx = mycol.drop()
print(xx.deleted_count)
