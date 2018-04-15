import pymongo
import json

class Json_Database(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 27017

    # 打开文件
    def __open_file(self):
        self.file = open('qiushi.json','r')
        # 链接数据库
        self.client = pymongo.MongoClient(host=self.host,port=self.port)
        # 创建数据库
        self.db = self.client['Qiushi']
        # 创建集合
        self.collection = self.db['dunzi']
    # 关闭文件
    def __close_file(self):
        self.file.close()
    # 调度方法
    def start_work(self):
        # 链接# 打开文件
        self.__open_file()
        # 读取数据列表 由列表转换成字典 list--->dict
        data_list = json.load(self.file)
        #写入
        try:
            self.collection.insert(data_list)
        except Exception as e:
            print(e)
        finally:
            # 关闭文件
            self.__close_file()

if __name__ == '__main__':
    foo = Json_Database()
    foo.start_work()