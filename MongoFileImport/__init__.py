
import argparse
from MongoFileImport import MongoFileImport

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--mongourl', type=str, default=None)
    parser.add_argument("--file",type=str, default=None)
    parser.add_argument("--dir",type=str,default=None)
    parser.add_argument("--db",type=str,default=None)
    parser.add_argument("--cn",type=str,default=None)


    args = parser.parse_args()



    if(args.mongourl!=None):
        if(args.cn!=None ):
           if( args.file != None and args.db!=None):
               MongoFileImport.SingleCollectionprocess(args.file,args.mongourl,args.db,args.cn)
           elif (args.dir != None and args.db!=None):
               MongoFileImport.singlepichuli(args.dir,args.mongourl,args.db,args.cn)
           else:
            print("args error")



        else:
            if(args.dir!=None and args.db!=None):
                MongoFileImport.pichuli(args.dir,args.mongourl,args.db)
            elif(args.file!=None and args.db!=None):
                MongoFileImport.filepprocess(args.file,args.mongourl,args.db)
            else:
                print("args error")


