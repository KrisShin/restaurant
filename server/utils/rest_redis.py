from config.global_params import redis
import json


class Redis(object):
    '''custom redis object'''

    def get_val(self, key: str):
        res = redis.get(key)
        return json.loads(res) if res else None

    def set_val(self, key: str, val, ex: int):
        try:
            val = json.dumps(val)
            return redis.set(key, val, ex=ex)
        except:
            raise Exception(f'{type(val)} val jsonify failed. :{val}')


r = Redis()
