import redis 
import time

r = redis.Redis(host='localhost', port=6379)

def enqueue_task(task_id: str, data: str):
    r.lpush("task_queue", f"{task_id}:{data}")
    print(f"Enqueued task {task_id}")

# Simulate job producer
if __name__ == "__main__":
    for i in range(10):
        enqueue_task(f"task_{i}", f"data_{i}")
        time.sleep(1)