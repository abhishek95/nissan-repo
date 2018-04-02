'''
Sync manager (host server) to syncronise data between flask app and MQTT client

'''
from multiprocessing.managers import SyncManager


class MyManager(SyncManager):
    pass


syncdict = {}
def get_dict():
    return syncdict

if __name__ == "__main__":
    MyManager.register("syncdict", get_dict)
    manager = MyManager(("127.0.0.1", 8000), authkey="password")
    manager.start()
    raw_input("Press any key to kill server".center(50, "-"))
    manager.shutdown()