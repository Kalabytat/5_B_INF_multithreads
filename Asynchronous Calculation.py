import asyncio
import math

async def calculate_factorial(number):
    await asyncio.sleep(0.1)  # Simula un'operazione asincrona
    return math.factorial(number)

async def main():
    numbers = [5, 7, 10, 3, 8]
    tasks = [calculate_factorial(num) for num in numbers]
    
    results = await asyncio.gather(*tasks)
    
    for num, result in zip(numbers, results):
        print(f"Factorial of {num} is {result}")

asyncio.run(main())