import shutil
from threading import Thread
import glob
import queue, threading, os, time
import shutil
import sys
import os

fileQueue = queue.Queue()
destPath = r'workspace\data_src'


class ThreadedCopy:
    totalFiles = 0
    copyCount = 0
    lock = threading.Lock()

    def __init__(self, src_path):
        fileList = glob.glob(r"{}\**\*.jpg".format(src_path), recursive=True)

        if not os.path.exists(destPath):
            os.mkdir(destPath)

        self.totalFiles = len(fileList)

        print(str(self.totalFiles) + " files to copy.")
        self.threadWorkerCopy(fileList)

    def CopyWorker(self):
        while True:
            fileName = fileQueue.get()
            shutil.copy(fileName, destPath)
            fileQueue.task_done()
            with self.lock:
                self.copyCount += 1
                percent = (self.copyCount * 100) / self.totalFiles
                print(str(percent) + " percent copied.", end='r')

    def threadWorkerCopy(self, fileNameList):
        for i in range(16):
            t = threading.Thread(target=self.CopyWorker)
            t.daemon = True
            t.start()
        for fileName in fileNameList:
            fileQueue.put(fileName)
        fileQueue.join()


if __name__ == '__main__':
    src_path = sys.argv[1]
    if not os.path.exists(src_path):
        raise ValueError
    ThreadedCopy(src_path)
