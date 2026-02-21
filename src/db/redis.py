import aioredis
from src.config import Config

# Redis connection for token blocklist
token_blocklist = aioredis.StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
)