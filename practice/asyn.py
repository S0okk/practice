import asyncio

async def foo():
    print("Foo: старт")
    await asyncio.sleep(2)
    print("Foo: конец")

async def bar():
    print("Bar: старт")
    await asyncio.sleep(1)
    print("Bar: конец")

async def main():
    await asyncio.gather(foo(), bar())

asyncio.run(main())
