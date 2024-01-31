import sys

from typing import Optional
from redis.asyncio.client import Redis
from redis.exceptions import AuthenticationError, TimeoutError

from backend.common.log import log
from backend.core.config import settings



class RedisCli(Redis):
    def __init__(self):
        super(RedisCli, self).__init__(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT, # type: ignore
            password=settings.REDIS_PASSWORD,
            db=settings.REDIS_DB,
            socket_timeout=settings.REDIS_TIMEOUT,
            decode_responses=True,
        )

    async def open(self):
        """Open redis connection.
        
        Returns:
            Redis: Redis connection.
        """
        try:
            await self.ping()
        except (AuthenticationError, TimeoutError) as e:
            log.error(f'Open redis connection failed: {e}')
            sys.exit(1)
        else:
            log.info(f'Open redis connection: {self}')
            return self
        
    async def delete_prefix(self, prefix: str, exclude: Optional[str | list] = None):
        """Delete all keys with the given prefix.
        
        Args:
            prefix (str): Prefix of the keys to be deleted.
            exclude (str | list, optional): Keys to be excluded. Defaults to None.
        """
        keys = await self.keys(f'{prefix}*')
        if exclude:
            if isinstance(exclude, str):
                exclude = [exclude]
            keys = [key for key in keys if key not in exclude]
        if keys:
            await self.delete(*keys)
            log.info(f'Delete redis keys: {keys}')
        else:
            log.info(f'No redis keys to be deleted.')