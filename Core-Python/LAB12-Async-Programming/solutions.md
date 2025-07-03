# LAB12 - Asynchronous Programming Solutions

This file provides a reference solution for the Asynchronous Programming lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation

### `helpers/async_utils.py`

```python
"""
Async utility functions.

This module contains utility functions for asynchronous programming.
"""

import asyncio
import aiohttp
import random
import time
from datetime import datetime


async def fetch_url(url, session=None, timeout=30):
    """
    Fetch data from a URL asynchronously.
    
    Args:
        url (str): URL to fetch
        session (aiohttp.ClientSession, optional): Session to use
        timeout (int, optional): Timeout in seconds
        
    Returns:
        dict: Response data (usually JSON)
    """
    # Create a session if not provided
    close_session = False
    if session is None:
        session = aiohttp.ClientSession()
        close_session = True
    
    try:
        # Make the request with appropriate timeout
        start_time = time.time()
        async with session.get(url, timeout=timeout) as response:
            # Check if the request was successful
            if response.status == 200:
                # Parse and return the response data
                data = await response.json()
                elapsed = time.time() - start_time
                return {
                    "url": url,
                    "status": response.status,
                    "data": data,
                    "elapsed": elapsed
                }
            else:
                # Return error information
                return {
                    "url": url,
                    "status": response.status,
                    "error": f"HTTP Error: {response.status}",
                    "elapsed": time.time() - start_time
                }
    except aiohttp.ClientError as e:
        # Handle aiohttp specific errors
        return {
            "url": url,
            "status": "error",
            "error": f"Request error: {str(e)}",
            "elapsed": time.time() - start_time
        }
    except asyncio.TimeoutError:
        # Handle timeout
        return {
            "url": url,
            "status": "timeout",
            "error": f"Request timed out after {timeout} seconds",
            "elapsed": timeout
        }
    except Exception as e:
        # Handle any other exceptions
        return {
            "url": url,
            "status": "error",
            "error": f"Unexpected error: {str(e)}",
            "elapsed": time.time() - start_time
        }
    finally:
        # Close the session if we created it
        if close_session:
            await session.close()


async def run_tasks(tasks, max_concurrent=5):
    """
    Run multiple tasks concurrently with a limit on concurrency.
    
    Args:
        tasks (list): List of coroutines to run
        max_concurrent (int, optional): Maximum number of concurrent tasks
        
    Returns:
        list: Results from all tasks
    """
    # Create a semaphore to limit concurrency
    semaphore = asyncio.Semaphore(max_concurrent)
    
    # Define a wrapper function that acquires and releases the semaphore
    async def task_wrapper(task):
        async with semaphore:
            return await task
    
    # Create tasks with the semaphore wrapper
    wrapped_tasks = [task_wrapper(task) for task in tasks]
    
    # Run all tasks and return results
    return await asyncio.gather(*wrapped_tasks, return_exceptions=True)


async def retry_async(coro, max_retries=3, delay=1, backoff_factor=2):
    """
    Retry an async operation with exponential backoff.
    
    Args:
        coro: Coroutine to retry
        max_retries (int, optional): Maximum number of retry attempts
        delay (float, optional): Initial delay between retries in seconds
        backoff_factor (float, optional): Factor to increase delay with each retry
        
    Returns:
        Any: Result from the coroutine
        
    Raises:
        Exception: If all retries fail
    """
    retries = 0
    current_delay = delay
    last_exception = None
    
    while retries <= max_retries:
        try:
            # Try to execute the coroutine
            return await coro
        except Exception as e:
            # Store the exception
            last_exception = e
            
            # If we've exhausted retries, give up
            if retries == max_retries:
                break
                
            # Calculate delay with exponential backoff
            wait_time = current_delay * (1 + random.random() * 0.1)  # Add jitter
            print(f"Retry {retries + 1}/{max_retries}, waiting {wait_time:.2f}s...")
            
            # Wait before retrying
            await asyncio.sleep(wait_time)
            
            # Increase delay for next retry
            current_delay *= backoff_factor
            retries += 1
    
    # If we get here, all retries failed
    raise last_exception


async def timeout_after(coro, timeout):
    """
    Run a coroutine with a timeout.
    
    Args:
        coro: Coroutine to run
        timeout (float): Timeout in seconds
        
    Returns:
        Any: Result from the coroutine
        
    Raises:
        asyncio.TimeoutError: If the operation times out
    """
    try:
        # Use asyncio.wait_for to set a timeout
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        # Re-raise the timeout exception with a more descriptive message
        raise asyncio.TimeoutError(f"Operation timed out after {timeout} seconds")


async def async_map(coro, items, max_concurrent=5):
    """
    Map an async function over a list of items with concurrency control.
    
    Args:
        coro: Async function to apply
        items (list): Items to process
        max_concurrent (int, optional): Maximum number of concurrent operations
        
    Returns:
        list: Results from applying the function to each item
    """
    # Create tasks for each item
    tasks = [coro(item) for item in items]
    
    # Use run_tasks to execute with concurrency limit
    return await run_tasks(tasks, max_concurrent=max_concurrent)


async def rate_limited(coro, rate_limit, time_period=1.0):
    """
    Run a coroutine with rate limiting.
    
    Args:
        coro: Coroutine to run
        rate_limit (int): Maximum number of operations
        time_period (float): Time period in seconds
        
    Returns:
        Any: Result from the coroutine
    """
    # Get class-level storage for operation times
    cls = rate_limited
    if not hasattr(cls, 'operation_times'):
        cls.operation_times = []
    
    # Clean up old operation times
    current_time = time.time()
    cls.operation_times = [t for t in cls.operation_times if current_time - t < time_period]
    
    # Check if we're at the rate limit
    if len(cls.operation_times) >= rate_limit:
        # Calculate how long to wait
        oldest_time = cls.operation_times[0]
        wait_time = time_period - (current_time - oldest_time)
        if wait_time > 0:
            print(f"Rate limit reached. Waiting {wait_time:.2f}s...")
            await asyncio.sleep(wait_time)
    
    # Add the current time to the list
    cls.operation_times.append(time.time())
    
    # Run the coroutine and return the result
    return await coro


def get_timestamp():
    """
    Get a formatted timestamp for the current time.
    
    Returns:
        str: Formatted timestamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
```

### `main.py`

```python
#!/usr/bin/env python3
"""
LAB12 - Asynchronous Programming

This module demonstrates asynchronous programming techniques
using Python's asyncio library, which is valuable for DevOps
automation tasks that require concurrency.
"""

import asyncio
import aiohttp
import time
import random
from helpers.async_utils import (
    fetch_url, run_tasks, retry_async, 
    timeout_after, async_map, rate_limited,
    get_timestamp
)


async def demo_simple_tasks():
    """Demonstrate basic async tasks and coroutines."""
    print("\n=== Simple Tasks Demo ===")
    print("Creating and running simple async tasks...")
    
    # Define a simple async task
    async def sleep_task(task_id, duration):
        print(f"Task {task_id} starting, will sleep for {duration:.2f}s")
        await asyncio.sleep(duration)
        print(f"Task {task_id} completed after {duration:.2f}s")
        return {'task_id': task_id, 'duration': duration}
    
    # Create a list of tasks with random durations
    tasks = [
        sleep_task(i, random.uniform(0.5, 3.0))
        for i in range(1, 6)
    ]
    
    # Compare sequential vs concurrent execution
    print("\nRunning tasks sequentially...")
    seq_start = time.time()
    sequential_results = []
    for task in tasks:
        result = await task
        sequential_results.append(result)
    seq_elapsed = time.time() - seq_start
    print(f"Sequential execution took {seq_elapsed:.2f} seconds")
    
    # Reset tasks as they've already been consumed
    tasks = [
        sleep_task(i, random.uniform(0.5, 3.0))
        for i in range(1, 6)
    ]
    
    print("\nRunning tasks concurrently...")
    conc_start = time.time()
    concurrent_results = await asyncio.gather(*tasks)
    conc_elapsed = time.time() - conc_start
    print(f"Concurrent execution took {conc_elapsed:.2f} seconds")
    
    # Show the speed improvement
    if seq_elapsed > 0:
        speedup = seq_elapsed / conc_elapsed
        print(f"Concurrent execution was {speedup:.2f}x faster!")
    
    return "Simple tasks completed"


async def demo_web_requests():
    """Demonstrate async web requests with aiohttp."""
    print("\n=== Web Requests Demo ===")
    print("Fetching multiple URLs asynchronously...")
    
    # Define list of URLs to fetch
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/json",
        "https://httpbin.org/uuid",
        "https://httpbin.org/headers",
    ]
    
    # Sequential fetch
    print("\nFetching URLs sequentially...")
    seq_start = time.time()
    sequential_results = []
    
    # Create a session to reuse for all requests
    async with aiohttp.ClientSession() as session:
        for url in urls:
            result = await fetch_url(url, session=session)
            sequential_results.append(result)
            print(f"Fetched {url} in {result.get('elapsed', 0):.2f}s")
    
    seq_elapsed = time.time() - seq_start
    print(f"Sequential fetching took {seq_elapsed:.2f} seconds")
    
    # Concurrent fetch
    print("\nFetching URLs concurrently...")
    conc_start = time.time()
    
    async with aiohttp.ClientSession() as session:
        # Create fetch tasks for each URL
        tasks = [
            fetch_url(url, session=session)
            for url in urls
        ]
        
        # Gather all tasks
        concurrent_results = await asyncio.gather(*tasks)
    
    conc_elapsed = time.time() - conc_start
    print(f"Concurrent fetching took {conc_elapsed:.2f} seconds")
    
    # Show results
    print("\nResults:")
    for result in concurrent_results:
        print(f"URL: {result['url']}, Status: {result['status']}, Time: {result.get('elapsed', 0):.2f}s")
    
    # Show the speed improvement
    if seq_elapsed > 0:
        speedup = seq_elapsed / conc_elapsed
        print(f"Concurrent fetching was {speedup:.2f}x faster!")
    
    return f"Fetched {len(urls)} URLs"


async def demo_error_handling():
    """Demonstrate error handling in async code."""
    print("\n=== Error Handling Demo ===")
    print("Demonstrating error handling in async code...")
    
    # Define a task that might fail
    async def unreliable_task(task_id, fail_probability=0.5):
        print(f"Task {task_id} starting (fail probability: {fail_probability})")
        await asyncio.sleep(random.uniform(0.1, 1.0))
        
        # Randomly fail
        if random.random() < fail_probability:
            error_type = random.choice([
                ValueError("Value error occurred"),
                RuntimeError("Runtime error occurred"),
                ConnectionError("Connection error occurred")
            ])
            print(f"Task {task_id} failed with {type(error_type).__name__}")
            raise error_type
        
        print(f"Task {task_id} completed successfully")
        return f"Result from task {task_id}"
    
    # Example 1: Basic try/except
    print("\nExample 1: Basic try/except")
    try:
        result = await unreliable_task(1, fail_probability=0.8)
        print(f"Got result: {result}")
    except Exception as e:
        print(f"Caught exception: {type(e).__name__} - {str(e)}")
    
    # Example 2: Multiple tasks with gather and return_exceptions
    print("\nExample 2: Multiple tasks with gather and return_exceptions")
    tasks = [
        unreliable_task(i, fail_probability=0.6)
        for i in range(2, 5)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i+2} raised {type(result).__name__}: {str(result)}")
        else:
            print(f"Task {i+2} succeeded: {result}")
    
    # Example 3: Using retry_async utility
    print("\nExample 3: Using retry_async utility")
    try:
        # Create a task with a high failure probability
        result = await retry_async(
            unreliable_task(5, fail_probability=0.7),
            max_retries=3,
            delay=0.5,
            backoff_factor=2
        )
        print(f"After retries, got result: {result}")
    except Exception as e:
        print(f"All retries failed with: {type(e).__name__} - {str(e)}")
    
    return "Error handling completed"


async def demo_timeouts_and_cancellation():
    """Demonstrate timeouts and task cancellation."""
    print("\n=== Timeouts and Cancellation Demo ===")
    print("Demonstrating timeouts and task cancellation...")
    
    # Define a long-running task
    async def long_running_task(task_id, duration):
        print(f"Task {task_id} starting, will run for {duration:.2f}s")
        try:
            for i in range(int(duration * 2)):
                # Check for cancellation
                if asyncio.current_task().cancelled():
                    raise asyncio.CancelledError()
                
                await asyncio.sleep(0.5)
                print(f"Task {task_id} progress: {(i+1) / (duration * 2) * 100:.0f}%")
            
            print(f"Task {task_id} completed successfully")
            return f"Result from task {task_id}"
        except asyncio.CancelledError:
            print(f"Task {task_id} was cancelled")
            # Perform any necessary cleanup here
            raise
    
    # Example 1: Using timeout_after utility
    print("\nExample 1: Using timeout_after utility")
    try:
        # Try to run a task with a timeout
        result = await timeout_after(
            long_running_task(1, 5.0),  # Task will run for 5 seconds
            timeout=2.0  # But we only wait for 2 seconds
        )
        print(f"Got result: {result}")
    except asyncio.TimeoutError as e:
        print(f"Task timed out: {str(e)}")
    
    # Example 2: Manual task cancellation
    print("\nExample 2: Manual task cancellation")
    
    # Create and start a task
    task = asyncio.create_task(long_running_task(2, 10.0))
    
    # Wait for a bit, then cancel it
    await asyncio.sleep(3.0)
    print("Cancelling the task...")
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Task was successfully cancelled")
    
    # Example 3: Graceful shutdown with cancellation
    print("\nExample 3: Graceful shutdown with cancellation")
    
    # Start multiple tasks
    tasks = [
        asyncio.create_task(long_running_task(i, random.uniform(3.0, 8.0)))
        for i in range(3, 6)
    ]
    
    # Wait for a bit, then start graceful shutdown
    await asyncio.sleep(2.0)
    print("\nStarting graceful shutdown...")
    
    # Cancel all tasks
    for i, task in enumerate(tasks):
        print(f"Cancelling task {i+3}...")
        task.cancel()
    
    # Wait for all tasks to finish or be cancelled
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Check results
    for i, result in enumerate(results):
        if isinstance(result, asyncio.CancelledError):
            print(f"Task {i+3} was cancelled")
        elif isinstance(result, Exception):
            print(f"Task {i+3} failed: {str(result)}")
        else:
            print(f"Task {i+3} completed: {result}")
    
    return "Timeouts and cancellation demo completed"


async def demo_async_patterns():
    """Demonstrate common async patterns like semaphores and queues."""
    print("\n=== Async Patterns Demo ===")
    print("Demonstrating common async patterns...")
    
    # Example 1: Using run_tasks for concurrency control
    print("\nExample 1: Using run_tasks for concurrency control")
    
    # Define a simple task that reports when it starts and finishes
    async def demo_task(task_id, duration):
        print(f"{get_timestamp()} - Task {task_id} starting, will take {duration:.2f}s")
        await asyncio.sleep(duration)
        print(f"{get_timestamp()} - Task {task_id} completed")
        return f"Result from task {task_id}"
    
    # Create a lot of tasks
    tasks = [
        demo_task(i, random.uniform(0.5, 2.0))
        for i in range(1, 11)
    ]
    
    # Run them with limited concurrency
    print(f"Running {len(tasks)} tasks with max concurrency of 3...")
    results = await run_tasks(tasks, max_concurrent=3)
    
    print(f"All tasks completed, got {len(results)} results")
    
    # Example 2: Producer-consumer with asyncio.Queue
    print("\nExample 2: Producer-consumer with asyncio.Queue")
    
    # Create a queue
    queue = asyncio.Queue()
    
    # Define producer
    async def producer(num_items):
        for i in range(num_items):
            item = f"Item {i+1}"
            await queue.put(item)
            print(f"{get_timestamp()} - Producer: Added {item} to queue")
            await asyncio.sleep(random.uniform(0.1, 0.5))
        
        # Signal that production is done
        for _ in range(3):  # Number of consumers
            await queue.put(None)
    
    # Define consumer
    async def consumer(consumer_id):
        while True:
            # Get item from the queue
            item = await queue.get()
            
            # Check for termination signal
            if item is None:
                print(f"{get_timestamp()} - Consumer {consumer_id}: Received shutdown signal")
                queue.task_done()
                break
            
            # Process the item
            print(f"{get_timestamp()} - Consumer {consumer_id}: Processing {item}")
            await asyncio.sleep(random.uniform(0.5, 1.5))
            
            # Mark the task as done
            queue.task_done()
            print(f"{get_timestamp()} - Consumer {consumer_id}: Finished {item}")
    
    # Start producer and consumers
    print("Starting producer-consumer example...")
    producer_task = asyncio.create_task(producer(10))
    consumer_tasks = [
        asyncio.create_task(consumer(i))
        for i in range(1, 4)
    ]
    
    # Wait for producer to finish
    await producer_task
    
    # Wait for consumers to finish
    await asyncio.gather(*consumer_tasks)
    
    print("Producer-consumer example completed")
    
    # Example 3: Rate limiting
    print("\nExample 3: Rate limiting")
    
    # Define a task that will be rate limited
    async def rate_limited_task(task_id):
        print(f"{get_timestamp()} - Rate-limited task {task_id} running")
        await asyncio.sleep(0.1)
        return f"Result from rate-limited task {task_id}"
    
    # Run tasks with rate limiting
    print("Running tasks with rate limiting (2 per second)...")
    for i in range(1, 7):
        result = await rate_limited(rate_limited_task(i), rate_limit=2, time_period=1.0)
        print(f"{get_timestamp()} - Got result: {result}")
    
    return "Async patterns demo completed"


async def main():
    """Main async function to demonstrate asynchronous operations."""
    print("LAB12 - Asynchronous Programming")
    print("================================\n")
    
    start_time = time.time()  # For tracking execution time
    
    try:
        # Run all the demo functions sequentially
        # For clarity, we run them one at a time here
        await demo_simple_tasks()
        await demo_web_requests()
        await demo_error_handling()
        await demo_timeouts_and_cancellation()
        await demo_async_patterns()
        
        # Alternatively, we could run them concurrently:
        # results = await asyncio.gather(
        #     demo_simple_tasks(),
        #     demo_web_requests(),
        #     demo_error_handling(),
        #     demo_timeouts_and_cancellation(),
        #     demo_async_patterns()
        # )
        
    except Exception as e:
        print(f"\nAn error occurred: {type(e).__name__} - {str(e)}")
    
    # Calculate and display total execution time
    elapsed = time.time() - start_time
    print(f"\nTotal execution time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    import asyncio
    import time  # For execution time measurement
    asyncio.run(main())
```

## Key Learning Points

1. **Asynchronous Programming Basics**:
   - Understanding coroutines and the `async/await` syntax
   - Creating and running tasks with `asyncio.create_task` and `asyncio.gather`
   - Comparing sequential vs. concurrent execution

2. **Async HTTP Requests**:
   - Using `aiohttp` for non-blocking HTTP requests
   - Session management and connection pooling
   - Handling responses asynchronously

3. **Error Handling in Async Code**:
   - Propagation of exceptions in async context
   - Using `try/except` with async code
   - Implementing retry patterns with exponential backoff

4. **Timeout and Cancellation**:
   - Setting timeouts with `asyncio.wait_for`
   - Cancelling tasks with `task.cancel()`
   - Handling cancellation gracefully
   - Cleaning up resources after cancellation

5. **Concurrency Control**:
   - Using `asyncio.Semaphore` to limit concurrency
   - Implementing rate limiting for API calls
   - Avoiding race conditions

6. **Producer-Consumer Pattern**:
   - Working with `asyncio.Queue`
   - Coordinating multiple producers and consumers
   - Signaling between async components

## Common Issues and Troubleshooting

1. **Blocking the Event Loop**:
   - Using blocking calls inside async functions
   - Not awaiting coroutines properly
   - Running CPU-bound operations without offloading

2. **Task Management**:
   - Forgetting to `await` tasks
   - Not handling exceptions from tasks
   - Losing track of created tasks

3. **Resource Management**:
   - Not closing sessions or connections
   - Leaking resources on cancellation
   - Not implementing proper cleanup

4. **Deadlocks and Race Conditions**:
   - Improper use of locks or semaphores
   - Circular dependencies between tasks
   - Not handling shared state correctly

5. **Debugging**:
   - Difficulty tracking asynchronous execution flow
   - Missing or incorrect error propagation
   - Timeouts hiding underlying issues

## Best Practices

1. **Task Creation and Management**:
   - Always `await` tasks or add them to a collection for later awaiting
   - Use `asyncio.create_task()` to schedule coroutines for execution
   - Consider using `asyncio.TaskGroup` (Python 3.11+) for easier task management

2. **Error Handling**:
   - Use `return_exceptions=True` with `asyncio.gather()` to prevent one failure from stopping all tasks
   - Implement retries with exponential backoff for unreliable operations
   - Add appropriate timeouts to prevent hanging operations

3. **Resource Management**:
   - Use async context managers (`async with`) for resource cleanup
   - Implement `__aenter__` and `__aexit__` for custom async resources
   - Handle cancellation by catching `asyncio.CancelledError` and cleaning up

4. **Concurrency Control**:
   - Use semaphores to limit concurrent operations
   - Implement rate limiting for API calls
   - Be mindful of memory usage when creating many tasks

5. **Performance Optimization**:
   - Reuse sessions and connections when possible
   - Batch operations for efficiency
   - Monitor and tune concurrency levels based on available resources

## Extension Ideas

1. Implement a real-time monitoring dashboard with async updates
2. Create an async web scraper with concurrency controls
3. Build a parallel data processing pipeline using asyncio
4. Develop an async API client with automatic retries and rate limiting
5. Create a task scheduler with dependencies between tasks
6. Implement an async file processor that handles large files in chunks 