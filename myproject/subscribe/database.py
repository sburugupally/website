import sqlite3
obj = sqlite3.connect('db.sqlite3')
cur = obj.cursor()
print(obj)
save = cur.execute('select * FROM subscribe_Post')

# save = cur.execute()
lst = list(save.fetchall())
print(lst)
obj.close()