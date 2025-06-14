from memory_manager import MemoryManager
from file_manager import FileSystem
from security_module import SecurityModule
from disk_scheduler import DiskScheduler

# Initialize modules
memory = MemoryManager(memory_size=100, page_size=10)
fs = FileSystem()
security = SecurityModule()
disk = DiskScheduler(initial_head_position=50)

# Setup users
security.add_user("admin", "Admin")
security.add_user("student1", "Student")
security.add_user("guest1", "Guest")

# --- Simulated Login ---
current_user = "student1"
print(f"\n👤 Logged in as: {current_user}")

# --- File operations ---
print("\n📁 File Operations:")
if security.can_access(current_user, "write"):
    fs.create_folder("/", "course")
    fs.create_file("/course", "notes.txt", "read-write")
    fs.write_file("/course", "notes.txt", "Operating Systems Lecture 1")

if security.can_access(current_user, "read"):
    fs.read_file("/course", "notes.txt")

if security.can_access(current_user, "delete"):
    fs.delete_file("/course", "notes.txt")

# --- Memory access simulation ---
print("\n🧠 Memory Access Simulation:")
memory.access_page(current_user, 0)
memory.access_page(current_user, 1)
memory.access_page(current_user, 2)
memory.access_page(current_user, 0)  # hit
memory.access_page(current_user, 3)

# --- Disk I/O Simulation ---
print("\n💽 Disk I/O Simulation:")
disk.add_request(82)
disk.add_request(24)
disk.add_request(190)
disk.run_sstf()

# --- Logs and Summary ---
print("\n📋 Final Logs and Stats:")
security.show_log()
memory.log_stats()
disk.show_performance()
