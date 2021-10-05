import asyncio

async def hello():
	await asyncio.sleep(1)
	print('hello')

async def main():
	sayhello = asyncio.create_task(hello())
	await asyncio.sleep(0.3)
	hello2 = asyncio.create_task(hello())
	print('world')
	await hello2
	await asyncio.sleep(0.3)
	print("wait that's the wrong order")

asyncio.run(main())