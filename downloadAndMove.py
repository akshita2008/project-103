import shutil
import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/Hp/Downloads"
to_dir="D:\f1"

dir_tree={
  "img_files":[".jpg",".jpeg",".png",".gif",".jfif"],
  "doc_files":[".pdf",".ppt",".csv",".txt",".xls"]
}

class FMH(FileSystemEventHandler):
   def on_created(self,event):
      name,extension=os.path.splitext(event.src_path)
      time.sleep(1)
      for key,value in dir_tree.items():
        if extension in value:
           file_name=os.path.basename(event.src_path)
           print("downloaded"+file_name)
           path1=from_dir+"/"+file_name
           path2=to_dir+"/" +key
           path3= to_dir+"/" +key+"/"+file_name  
           if os.path.exists(path2):
              print("directory exist")
              shutil.move(path1,path3)
           else:
              os.makedirs(path2)
              print("Folder Is Created!!")
              shutil.move(path1,path3)
              
event_handler= FMH()
observer= Observer()

observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

