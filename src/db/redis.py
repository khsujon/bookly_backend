import aioredis
from src.config import Config


JTI_EXPIRY = 3600  # Time in seconds for how long the JTI should be stored in Redis (e.g., 1 hour)
# Redis connection for token blocklist
token_blocklist = aioredis.StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
)

async def add_token_to_blocklist(jti: str) -> None:
    """Add a token's JTI to the blocklist"""
    await token_blocklist.set(name = jti,value = "",ex = JTI_EXPIRY)
    

async def is_token_blocked(jti: str) -> bool:
    """Check if a token's JTI is in the blocklist"""
    jti= await token_blocklist.get(jti)
    return jti is not None