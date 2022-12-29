from redis_om import get_redis_connection

redis =  get_redis_connection(
    host = "",
    port = 11134,
    password = "",
    decode_responses = True,
)
