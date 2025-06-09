## 📌 Distributed Task Scheduler  
- Uses Redis as a message broker for fault-tolerant job queuing.  
- **To run:**  
  ```bash
  pip install redis
  redis-server &  # Start Redis
  python scheduler.py &  # In one terminal
  python worker.py      # In another terminal
