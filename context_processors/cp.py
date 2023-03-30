import redis
redis_client = redis.Redis(host='localhost', port=6379, db=1)
def subject_renderer(request):
    if request.user.is_authenticated:
        set_key = f"user:{request.user.id}:notifications"
        set_length = redis_client.scard(set_key)
    return {
       'notif_count':set_length,
    }