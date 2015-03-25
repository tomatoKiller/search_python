import threading
import pymysql
import config

class dbManager:
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        self.__conn = pymysql.connect(
            host=config.Database['host'],
            user=config.Database['user'],
            passwd=config.Database['pass'],
            port=config.Database['port'],
            db=config.Database['dbname'],
            charset="utf8"
        )

        self.__cursor = self.__conn.cursor()

        with open('db.sql','r') as f:
            searchstr = f.read()

        self.execute(searchstr)


    def __del__(self):
        self.__cursor.close()
        self.__conn.close()

    def execute(self, sql, arg=None):
        self.__cursor.execute(sql, arg)
        # self.__conn.commit()
        return self.__cursor


    @staticmethod
    def getInstance():
        if not dbManager.__instance:
            dbManager.__lock.acquire()
            if not dbManager.__instance:
                dbManager.__instance = dbManager()
                dbManager.__lock.release()

        return dbManager.__instance

