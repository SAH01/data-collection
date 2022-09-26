import random

import redis

class my_redis:

    def get_ip(self):
        r = redis.Redis(host='127.0.0.1', port=6379, db=0,decode_responses=True)
        my_redis_data = r.zrange("proxies:universal",1,3000,True)
        return random.choice(my_redis_data)
        # print(len(my_redis_data))

if __name__ == '__main__':
    test_redis=my_redis()
    data=test_redis.get_ip()
    print(data)
