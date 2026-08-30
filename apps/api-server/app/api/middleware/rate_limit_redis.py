import redis

r = redis.Redis()


def allowed(key):

    current = r.incr(key)

    if current == 1:
        r.expire(key, 60)

    return current < 100