import asyncio
import logging
# import inspect

formatter = logging.basicConfig(format='%(asctime)s:%(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

async def sleeper(name, delay, repeat):
     for i in range(1, 1 + repeat):
       log.info(f'{name}: START ({i}/{repeat}) wait:{delay}s')
       await asyncio.sleep(delay)
       log.info(f'{name}: END ({i}/{repeat}) wait:{delay}s')
       return name


loop = asyncio.get_event_loop()
fut = asyncio.gather(sleeper("A",6,1), sleeper("B",2,3), sleeper("C",0.5,12))
print(loop.run_until_complete(fut))


# if __name__ == '__main__':
#   loop = asyncio.get_event_loop()
#   fut = asyncio.gather(sleeper("A",6,1))
#   log.info('main: START run_until_complete')
#   loop.run_until_complete(fut)
#   log.info('main: END run_until_complete')

# async def sleeper(name, delay, repeat):
#    for i in range(1, 1 + repeat):
#      await asyncio.sleep(delay)
#      return name

# if __name__ == '__main__':
#   loop = asyncio.get_event_loop()
#   fut = asyncio.gather(sleeper("A",6,1))
#   loop.run_until_complete(fut)

# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(s))

# f = s.send(None)
# print(f)
# print(type(f))
# print(dir(f))



# async def sleep():
  #   await asyncio.sleep(3)
  #   return 'I am await function'
  
  # s = sleep()
  
# simple coroutine function
# async def greeting():
#   print('hi guys')
# g = greeting()
# g.send(None)
# print(g.send(None))
# print(dir(g))
# print(g)
# print(type(g))
# print(inspect.iscoroutine(g))