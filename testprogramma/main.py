import asyncio
from xknx import XKNX
from xknx.devices import Light


async def main():
    xknx = XKNX(config='xknx.yaml')
    await xknx.start()
    light = Light(xknx,
                  name='bureau_licht',
                  group_address_switch='1/1/1')
    await light.set_on()
    await asyncio.sleep(2)
    await light.set_off()
    await asyncio.sleep(2)
    await xknx.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
