import asyncio
from bleak import BleakClient
from utils.address import *

# Charcteristic UUID (https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/include/bluetooth/services/nus.html)
TX_CHARCTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

def notify_callback(sender: int, data: bytearray):
    print('Sender: ', sender, ', Data: ', data)
    
async def run(ADDRESS): 
    # Timeout: 연결 제한 시간 8초가 넘어가면 더 이상 연결하지 말고 종료
    async with BleakClient(ADDRESS, timeout=10.0) as client:
        print('----- Connected -----')
        print('----- MAC Addr : ', ADDRESS)
        try:
            await client.start_notify(TX_CHARCTERISTIC_UUID, notify_callback)
        except Exception as e:
            print('Error ===> '+e)
            await client.disconnect()
    # Client 가 연결된 상태라면
    if client.is_connected:
        # 1초간 대기
        await asyncio.sleep(0.5)
        await client.stop_notify(TX_CHARCTERISTIC_UUID)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(run(ADDRESS))
    tasks = asyncio.gather(*(run(address) for address in CN103H_ADDRESS))
    loop.run_until_complete(tasks)
    loop.close()
    print('----- Done -----')