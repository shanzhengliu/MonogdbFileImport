

import json
import pymongo
import os


def pichuli(dirPath,MongoClient,dbName):

    client = pymongo.MongoClient(MongoClient)
    db = client[dbName]
    filenameList = os.listdir(dirPath)

    for i in filenameList:
        print(i)
        connectionName = i.replace(".json","")
        if(connectionName[-1]=='.'):
            connectionName=connectionName[0:-1]
        collection = db[connectionName]

        with open(dirPath+"/"+i, encoding="utf-8") as jf:
            str = jf.read()
            data = []
            data.extend(json.loads(str))
            collection.insert_many(data)
        client.close()  # 写完关闭连接


def filepprocess(fileName,MongoClient,dbName):
        client = pymongo.MongoClient(MongoClient)
        db = client[dbName]

        connectionName = fileName.split("/")[-1].replace(".json","")
        if(connectionName[-1]=='.'):
            connectionName=connectionName[0:-1]
        collection = db[connectionName]

        with open(fileName, encoding="utf-8") as jf:
            str = jf.read()
            data = []
            data.extend(json.loads(str))
            collection.insert_many(data)
        client.close()  # 写完关闭连接

