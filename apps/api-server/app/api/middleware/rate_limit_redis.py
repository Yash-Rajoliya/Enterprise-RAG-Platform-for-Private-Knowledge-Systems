import redis

r = redis.Redis()


def allowed(key: str, limit: int = 100, window: int = 60) -> bool:
    pipe = r.pipeline()
    pipe.incr(key)
    pipe.ttl(key)
    current, ttl = pipe.execute()

    # Set expiration if key is newly created or missing a TTL
    if ttl == -1:
        r.expire(key, window)

    return current <= limit