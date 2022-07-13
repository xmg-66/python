import pymysql
#pymysql
#查询方法
def query(sql):
    db=pymysql.connect(host='127.0.0.1',user='root',password='123456',db='bookstore-uni')
    cur=db.cursor()     #创建游标
    cur.execute(sql)    #执行SQL
    res=cur.fetchall()  #获取所有的结果
    db.close()
    return res


#修改、增加、删除
def commit(sql):
    db=pymysql.connect(host='127.0.0.1',user='root',password='123456',db='bookstore-uni')
    cur=db.cursor()     #创建游标
    cur.execute(sql)    #执行SQL
    db.commit()           #修改生效
    db.close()


if __name__ == "__main__":  #只有在当前的py文件执行时才执行 __name__内置变量
    # s="select *from user"    #查询
    # res=query(s)
    # print(res)

    # s1="update user set password='222223' where name='wqh';"  #sql外单内双，内双外单
    # s2="select * from user where name='wqh'"    #修改
    # commit(s1)
    # res=query(s2)
    # print(res)

    # s3="insert into user values(8,'test2','test2@qq.com','123456',null)" #增
    # s4="select * from user"
    # commit(s3)
    # res=query(s4)
    # print(res)

    # s5="delete from user where name='test2'"    #删
    # s6="select * from user"
    # commit(s5)
    # res=query(s6)
    # print(res)

