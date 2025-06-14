from collections import deque

class MemoryManager:
    def __init__(self, memory_size, page_size):
        self.page_size = page_size
        self.num_pages = memory_size // page_size
        self.page_table = {}  # key: process_id, value: list of pages
        self.memory = deque(maxlen=self.num_pages)  # FIFO queue
        self.page_faults = 0
        self.total_requests = 0

    def access_page(self, process_id, page_number):
        self.total_requests += 1
        page_id = f"{process_id}_{page_number}"

        if page_id in self.memory:
            print(f"[OK] Page {page_id} is in memory.")
        else:
            self.page_faults += 1
            print(f"[MISS] Page {page_id} caused a page fault.")
            self.memory.append(page_id)

    def log_stats(self):
        print("\n📊 Memory Usage and Page Fault Stats")
        print(f"Total Pages in Memory: {len(self.memory)}/{self.num_pages}")
        print(f"Total Page Requests: {self.total_requests}")
        print(f"Total Page Faults: {self.page_faults}")
        if self.total_requests > 0:
            fault_rate = (self.page_faults / self.total_requests) * 100
            print(f"Page Fault Rate: {fault_rate:.2f}%")

# --- Example usage ---
if __name__ == "__main__":
    mm = MemoryManager(memory_size=100, page_size=10)

    mm.access_page("P1", 0)
    mm.access_page("P1", 1)
    mm.access_page("P1", 2)
    mm.access_page("P2", 0)
    mm.access_page("P1", 0)  # should hit
    mm.access_page("P3", 1)
    mm.access_page("P4", 2)
    mm.access_page("P5", 3)
    mm.access_page("P1", 1)  # maybe fault again if FIFO pushed it out

    mm.log_stats()
