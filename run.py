from client import Client
import time
import config

if __name__ == '__main__':
    last = Client(config.BEARER_TOKEN,config.USER_ID)

    i=0
    while(1):
        i += 1
        print('Attempt ' + str(i)) # For control reasons
        time.sleep(5)
        last.checker()


