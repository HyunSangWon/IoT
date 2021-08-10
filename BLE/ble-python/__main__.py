import asyncio
import multiprocessing
from bleak import BleakClient
from utils.address import *

# Charcteristic UUID (https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/include/bluetooth/services/nus.html)
TX_CHARCTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
MAX_PROCCESS_NUM = 2

def notify_callback(sender: int, data: bytearray):
    print('Sender: ', sender, ', Data: ', data)
    
async def run(ADDRESS): 
    # Timeout: 연결 제한 시간 10초가 넘어가면 더 이상 연결하지 말고 종료
    async with BleakClient(ADDRESS, timeout=10.0) as client:
        print('----- Connected -----')
        print('----- MAC Addr : ', ADDRESS)
        try:
            await client.start_notify(TX_CHARCTERISTIC_UUID, notify_callback)
        except Exception as e:
            await client.disconnect()
    # Client 가 연결된 상태라면
    if client.is_connected:
        # 1초간 대기
        await asyncio.sleep(1)
        await client.stop_notify(TX_CHARCTERISTIC_UUID)

def getEventLoop(address):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address))
    loop.close()

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=MAX_PROCCESS_NUM)
    pool.map(getEventLoop, CN103H_ADDRESS)
    pool.close()
    pool.join()