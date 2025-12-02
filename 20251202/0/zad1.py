import asyncio

async def squarer(n):
    return n * n

async def doubler(n):
    return 2 * n

async def main(list):
    r1 = await asyncio.gather(*[squarer(i) for i in list])
    print(r1)
    r2 = await asyncio.gather(*[doubler(i) for i in r1])
    print(r2)

asyncio.run(main(range(10)))
