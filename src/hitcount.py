import redis

r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)

def ahit(key):
    r.incr(key)

def agetHit(key):
    return (r.get(key))
