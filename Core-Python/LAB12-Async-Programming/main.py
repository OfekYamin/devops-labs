#!/usr/bin/env python3
"""
LAB12 - Asynchronous Programming

This module demonstrates asynchronous programming techniques
using Python's asyncio library, which is valuable for DevOps
automation tasks that require concurrency.
"""

# TODO: Import required libraries
# import asyncio
# import aiohttp
# import time
# import random
# from helpers.async_utils import (
#     fetch_url, run_tasks, retry_async, 
#     timeout_after, async_map, rate_limited,
#     get_timestamp
# )


async def demo_simple_tasks():
    """Demonstrate basic async tasks and coroutines."""
    # TODO: Implement simple async tasks demo
    # 1. Create several simple async tasks (e.g., sleep for random time)
    # 2. Run them concurrently and measure total execution time
    # 3. Compare with sequential execution time
    
    print("\n=== Simple Tasks Demo ===")
    print("Creating and running simple async tasks...")
    
    return "Simple tasks completed"


async def demo_web_requests():
    """Demonstrate async web requests with aiohttp."""
    # TODO: Implement async web requests demo
    # 1. Define list of URLs to fetch
    # 2. Use fetch_url to get them asynchronously
    # 3. Compare execution time with sequential requests
    
    print("\n=== Web Requests Demo ===")
    print("Fetching multiple URLs asynchronously...")
    
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        # Add more URLs as needed
    ]
    
    return f"Fetched {len(urls)} URLs"


async def demo_error_handling():
    """Demonstrate error handling in async code."""
    # TODO: Implement async error handling demo
    # 1. Create tasks that might fail
    # 2. Use try/except within async functions
    # 3. Show how to propagate and handle exceptions
    # 4. Demonstrate retry_async utility
    
    print("\n=== Error Handling Demo ===")
    print("Demonstrating error handling in async code...")
    
    return "Error handling completed"


async def demo_timeouts_and_cancellation():
    """Demonstrate timeouts and task cancellation."""
    # TODO: Implement timeouts and cancellation demo
    # 1. Create long-running tasks
    # 2. Apply timeouts using timeout_after
    # 3. Show how to cancel tasks
    # 4. Handle cancellation and cleanup
    
    print("\n=== Timeouts and Cancellation Demo ===")
    print("Demonstrating timeouts and task cancellation...")
    
    return "Timeouts and cancellation demo completed"


async def demo_async_patterns():
    """Demonstrate common async patterns like semaphores and queues."""
    # TODO: Implement async patterns demo
    # 1. Use asyncio.Semaphore for concurrency control
    # 2. Show asyncio.Queue for producer-consumer pattern
    # 3. Demonstrate rate limiting
    
    print("\n=== Async Patterns Demo ===")
    print("Demonstrating common async patterns...")
    
    return "Async patterns demo completed"


async def main():
    """Main async function to demonstrate asynchronous operations."""
    print("LAB12 - Asynchronous Programming")
    print("================================\n")
    
    start_time = time.time()  # For tracking execution time
    
    # TODO: Run all the demo functions
    # 1. Either sequentially or concurrently
    # 2. Capture and display results
    # 3. Handle any exceptions
    
    # Placeholder implementations
    await demo_simple_tasks()
    await demo_web_requests()
    await demo_error_handling()
    await demo_timeouts_and_cancellation()
    await demo_async_patterns()
    
    # Calculate and display total execution time
    elapsed = time.time() - start_time
    print(f"\nTotal execution time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    import asyncio
    import time  # For execution time measurement
    asyncio.run(main()) 