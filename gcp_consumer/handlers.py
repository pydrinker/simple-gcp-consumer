import asyncio
import logging

logger = logging.getLogger(__name__)


async def print_handler(message, *args):
    print(f"message, {message}")
    print(f"args, {args}")

    # mimic IO processing
    await asyncio.sleep(0.1)
    return True


async def error_handler(exc_info, message):
    print(f"exception {exc_info} received")
    # do not delete the message that originated the error
    return False
