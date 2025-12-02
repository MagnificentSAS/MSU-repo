import asyncio

evsnd = asyncio.Event()
evmid0 = asyncio.Event()
evmid1 = asyncio.Event()


async def snd():
    evsnd.set()
    print("snd generated evnsd")

async def mid(k):
    await evsnd.wait()
    print("mid got evsnd")
    if k == 0:
        evmid0.set()
        print("mid generated evmid0")
    else:
        evmid1.set()
        print("mid generated evmid1")

async def rcv():
    await evmid0.wait()
    print("rcv got evmid0")
    await evmid1.wait()
    print("rcv got evmid1")

async def main():
    _ = await asyncio.gather(snd(), mid(1), mid(0), rcv())
    print("GOOD")

asyncio.run(main())
