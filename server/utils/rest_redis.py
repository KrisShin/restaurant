import json

from config.global_params import redis


class Redis(object):
    '''custom redis object'''

    def get_val(self, key: str):
        res = redis.get(key)
        if res:
            try:
                res = json.loads(res)
            except json.JSONDecodeError:
                res = res.decode()
        return res

    def set_val(self, key: str, val, ex=0):
        try:
            if not isinstance(val, str):
                val = json.dumps(val)
            return redis.set(key, val, ex=ex)
        except:
            raise Exception(f'{type(val)} val jsonify failed. :{val}')

    def del_val(self, key):
        try:
            redis.delete(key)
            return True
        except Exception as e:
            print(e)
            return False


r = Redis()
