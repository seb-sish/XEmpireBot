import asyncio
from bot.core import launcher
from bot.utils.logger import logger

async def main():
	await launcher.start()


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		logger.info("Bot stopped by user")