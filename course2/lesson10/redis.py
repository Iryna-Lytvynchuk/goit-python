import redis


r = redis.Redis(
    host='localhost',
    port=6379
)

def cache(id):

  key = "cache:" + str(id)
  result = r.hgetall(key)

  if result:
      return result

  else:
      sql = "SELECT `id`, `name` FROM `cache` WHERE `id`=%s"
      result = db_record(sql, (id,))

      if result:
          r.hmset(key, result)
          r.expire(key, ttl)
      return result      