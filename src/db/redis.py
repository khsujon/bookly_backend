import redis.asyncio as redis
from src.config import Config


JTI_EXPIRY = 3600  # Time in seconds for how long the JTI should be stored in Redis (e.g., 1 hour)
# Redis connection for token blocklist
# Async Redis client
token_blocklist = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
    decode_responses=True,   # returns str instead of bytes
)


async def add_token_to_blocklist(jti: str) -> None:
    """Add token JTI to Redis blocklist"""
    await token_blocklist.set(
        name=jti,
        value="revoked",
        ex=JTI_EXPIRY
    )
    

async def is_token_blocked(jti: str) -> bool:
    """Check whether token JTI exists in blocklist"""
    value = await token_blocklist.get(jti)
    return value is not None