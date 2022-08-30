from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# 映射对象的基类
Base = declarative_base()
# 连接数据库.指定编码为utf-8
# 使用mysqlconnector(安装mysql-connector-python)而不是pymsql,以解决下面的错误
# 错误1366:"Incorrect string value",下面是输出的异常信息
# latin-1' codec can't encode characters in position 58-62: ordinal not in range(256)
engine = create_engine('mysql+mysqlconnector://root:3838438@localhost:3306/k8', encoding='utf-8')
# 创建绑定于该连接的数据库会话.域session可以将session进行共享
DBSession = scoped_session(sessionmaker(bind=engine))


# 要映射到的类,它要继承前面的基类
class Product(Base):
    # 映射到DB中的表名.私有属性(双'_'开头)
    __tablename__ = 'product'
    # 表的结构.使用Column对象,其中记录了该属性对应于数据库中的数据类型以及其它信息
    id = Column(String(20), primary_key=True)  # 标识为主键
    name = Column(String(20))
    type = Column(String(20))


# 添加用户
def add_user(user):
    session = DBSession()
    session.add(user)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        # 输出异常信息
        print("add_user(): ======={}=======".format(e))
    finally:
        session.close()


# 其它的一些测试
def other_test():
    session = DBSession()
    # 查询并更新用户
    session.query(Product).filter(Product.id == '12345678').update({Product.name: "北京两日游"})
    # 这样输出的是这些操作对应的SQL语句,并不是查询结果
    # print(session.query(Product).filter(Product.id == '12345678'))
    # 查询并查看查询结果
    goal = session.query(Product).filter(Product.id == '12345678').one()
    print('name:' + goal.name + ',type' + goal.type)
    # 查询并删除用户
    session.query(Product).filter(Product.id == '12345678').delete()
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print("other_test(): ======={}=======".format(e))
    finally:
        session.close()


if __name__ == '__main__':
    # 创建一个自定义的Product对象(因为继承了基类,这里不需要实现Product类的该构造器即可使用)
    new_user = Product(id='12345678', name='上海一日游', type='景+酒')
    # 添加用户的测试
    add_user(new_user)
    # 修改,查询和删除用户的演示
    other_test()
