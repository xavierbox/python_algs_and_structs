
import time
import asyncio 

def sync_coffee(x=1, container = None):
    
    container.append( len(container) )
    print('preparing sync coffee')
    
    time.sleep(x/3)
    print('*sync_coffee*1/3 done')
    
    time.sleep(x/3)
    print('*sync_coffee*2/3 done')
    
    time.sleep(x/3)
    print('*sync_coffee*3/3 done')
    
    
    print('**sync_coffee done')
    return '**sync_coffee'

async def async_sync_coffee(x=1):
    
    #task = asyncio.create_task( lambda x: sync_coffee(x) )
    x = asyncio.to_thread(sync_coffee, 12)
    print( x, type(x))
  
    print('task created, about to return')
  



async def coffee(x=1):
    print('preparing coffee')
    
    await asyncio.sleep(x/3)
    print('1/3 done')
    
    await asyncio.sleep(x/3)
    print('2/3 done')
    
    await asyncio.sleep(x/3)
    print('3/3 done')
    
    
    print('coffee done')
    return 'coffee'

async def bagels(x=2, y = None):
    
    if y:
        print('y:', y)  
    
    print('preparing bagels')
    await asyncio.sleep(x)
    print('bagles done', y)
    return 'bagels'

async def main():
    
    
    
    #start_time = time.time()
    #task1 = asyncio.create_task(bagels(11))
    #task2 = asyncio.create_task( coffee(11) )
    #result_coffee = await task2
    #result_bagels = await task1
    #print('all tasks done')
     
    l = [] 
    task1 =  asyncio.create_task(asyncio.to_thread(sync_coffee, 2, l ))
    task2 =  asyncio.create_task(bagels( 3 ))
    task3 =  asyncio.create_task(asyncio.to_thread(sync_coffee, 2, l ))
    
    r1 = await task1
    r2 = await task2
    r3 = await task3
    
    print('all tasks done', l )
    #print(r1, r2)
    #print('time:', time.time() - start_time)

asyncio.run( main() ) 