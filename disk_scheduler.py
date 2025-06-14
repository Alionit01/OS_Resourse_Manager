class DiskScheduler:
    def __init__(self, initial_head_position=0):
        self.queue = []
        self.head = initial_head_position
        self.total_seek_time = 0
        self.completed_requests = 0

    def add_request(self, position):
        self.queue.append(position)
        print(f"[REQUEST] Disk I/O request added at position {position}")

    def run_fcfs(self):
        print("\n▶ Running FCFS (First-Come First-Served):")
        for pos in self.queue:
            seek_time = abs(self.head - pos)
            print(f"Moving from {self.head} to {pos} (Seek: {seek_time})")
            self.total_seek_time += seek_time
            self.head = pos
            self.completed_requests += 1
        self.queue.clear()

    def run_sstf(self):
        print("\n▶ Running SSTF (Shortest Seek Time First):")
        while self.queue:
            # Find request with shortest seek time
            closest = min(self.queue, key=lambda x: abs(self.head - x))
            seek_time = abs(self.head - closest)
            print(f"Moving from {self.head} to {closest} (Seek: {seek_time})")
            self.total_seek_time += seek_time
            self.head = closest
            self.queue.remove(closest)
            self.completed_requests += 1

    def show_performance(self):
        print("\n📊 Disk Scheduler Performance")
        print(f"Total seek time: {self.total_seek_time}")
        if self.completed_requests > 0:
            avg_seek = self.total_seek_time / self.completed_requests
            print(f"Average seek time: {avg_seek:.2f}")
        else:
            print("No requests processed.")

# --- Example usage ---
if __name__ == "__main__":
    ds = DiskScheduler(initial_head_position=50)

    ds.add_request(82)
    ds.add_request(170)
    ds.add_request(43)
    ds.add_request(140)
    ds.add_request(24)
    ds.add_request(16)
    ds.add_request(190)

    ds.run_fcfs()
    ds.show_performance()

    print("\n--- Resetting ---\n")
    ds = DiskScheduler(initial_head_position=50)

    ds.add_request(82)
    ds.add_request(170)
    ds.add_request(43)
    ds.add_request(140)
    ds.add_request(24)
    ds.add_request(16)
    ds.add_request(190)

    ds.run_sstf()
    ds.show_performance()
