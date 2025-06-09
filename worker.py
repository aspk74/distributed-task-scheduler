import redis 

r = redis.Redis(host='localhost', port=6379)

def process_task(task_data: str):
    task_id, data = task_data.split(":")
    print(f"Processing {task_id} with data: {data}")
    # Simulate work
    time.sleep(2)
    return f"Processed {task_id}"

if __name__ == "__main__":
    while True:
        task_data = r.brpop("task_queue")[1].decode()
        result = process_task(task_data)
        print(result)