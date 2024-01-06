import time
import shutil
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = ""

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)
    



    event_Handler = FileMovementHandler()
    observer = Observer()
    observer.schedule(event_Handler,from_dir,recursive = True)
    observer.start()
    

    while True:
        time.sleep(2)
        print("running")

