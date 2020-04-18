
import argparse
from MongoFileImport import MongoFileImport

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--mongourl', type=str, default=None)
    parser.add_argument("--file",type=str, default=None)
    parser.add_argument("--dir",type=str,default=None)
    parser.add_argument("--db",type=str,default=None)
    parser.add_argument("--help", type=str, default=None)

    args = parser.parse_args()
    if(args.help==None and args.mongourl == None):
        print("you can user the command: MonogoFileImport --mongourl mongo+srv://xxxxx --dir yourDir --db  databaseName to import your data")
        print("you can user the command: MonogoFileImport --mongourl mongo+srv://xxxxx --file yourfile --db  databaseName to import your data")



    if(args.mongourl!=None):
        if(args.dir!=None and args.db!=None):
            MongoFileImport.pichuli(args.dir,args.mongourl,args.db)
        elif(args.file!=None and args.db!=None):
            MongoFileImport.filepprocess(args.file,args.mongourl,args.db)
        else:
            print("args error")


