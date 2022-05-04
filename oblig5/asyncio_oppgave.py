import asyncio
import random as rdm

TASKS = 10

class Counter:
    def __init__(self):
        self.counter = -1 #execute_io inkrementerer en gang for mye

    def increment(self):
        self.counter += 1

    def get(self):
        return self.counter

    def __str__(self) -> str:
        return str( self.get() ) 

async def execute_io(number: int, counter: Counter) -> int:
    await asyncio.sleep( 2 * rdm.random() )
    counter.increment()
    digit_sum = 0
    number = str(number)
    for digit in number:
        digit = int(digit)
        digit_sum += digit
    return digit_sum

async def main():
    counter = Counter()
    tasks = []
    for i in range(TASKS+1):                                 #Starter på 0
        task = asyncio.create_task( execute_io(i, counter) )
        tasks.append(task)
    result = sum( await asyncio.gather(*tasks) )
    print(f"Finished processing, result {result}, got counter: {counter}")

asyncio.run( main() )