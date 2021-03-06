import threading 
from threading import*
import time

data_box={} #'data_box' is the dictionary in which we store data

#for create operation 

def create(key,value,timeout=0):
    if key in data_box:
        print("error: this key already exists") #error message!
    else:
        if(key.isalpha()):
            if len(data_box)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    data_box[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message!
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message!

#for read operation
            
def read(key):
    if key not in data_container:
        print("error: given key does not exist in database. Please enter a valid key") #error message!
    else:
        b=data_box[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with to-live time
                stri=str(key)+":"+str(b[0]) #JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message!
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation

def delete(key):
    if key not in data_box:
        print("error: given key does not exist in database. Please enter a valid key") #error message!
    else:
        b=data_box[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with  the to-live time
                del data_box[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message!
        else:
            del data_box[key]
            print("key is successfully deleted")

#This is the source code for Data Store using Key-Value
#It supports basic CRD operation (create, read and delete) in well defined manner.
