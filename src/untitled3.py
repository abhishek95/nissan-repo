from multiprocessing.managers import SyncManager
import sys, time

class MyManager(SyncManager):
    pass

MyManager.register("syncdict")

if __name__ == "__main__":
    manager = MyManager(("127.0.0.1", 8000), authkey="password")
    manager.connect()
    syncdict = manager.syncdict()

    print ("dict = %s" % (dir(syncdict)))
    key = raw_input("Enter key to update: ")
    inc = float(raw_input("Enter increment: "))
    sleep = float(raw_input("Enter sleep time (sec): "))

    try:
         #if the key doesn't exist create it
         if not syncdict.has_key(key):
             syncdict.update([(key, 0)])
         #increment key value every sleep seconds
         #then print syncdict
         while True:
              syncdict.update([(key, syncdict.get(key) + inc)])
              time.sleep(sleep)
              print ("%s" % (syncdict))
    except KeyboardInterrupt:
         print ("Killed client")