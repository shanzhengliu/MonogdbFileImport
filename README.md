# MonogoFileImport Instruction


This is a module to help you import json file into monogodb.
## How to install 

```pip install MongoFileImport```


## Using in command
There are 9 argument when you use in the command.

| argument | type |default|desctipyion|
| --- | --- | --- |---|
|--mongourl|str|None|Your monogoDB url, you need to get the python version connection url, like mongodb+srv://username:password@clusterxxxx.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true
--file|str|None|your file name
|--dir|str|None|your dir name
|--db|str|None|your database name


Example 1:
import a folder with json files to your database 
```
MongoFileImport --mongourl mongodb+srv://username:password@cluster0-xxxxx.mongodb.net --db test --dir d:/Downloads/Dataset_22_March_2020/Dataset_22_March_2020/revisions
```

Example 2:
import a json files to your database 
```
MongoFileImport --mongourl mongodb+srv://username:password@cluster0-xxxxx.mongodb.net --db test --file d:/Downloads/Dataset_22_March_2020/Dataset_22_March_2020/revisions/Australian.json
```



if you want to know more, please visit : https://github.com/shanzhengliu/SimpleSpider




