class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # 'Admin', 'Student', or 'Guest'

class SecurityModule:
    def __init__(self):
        self.users = {}  # username -> User
        self.access_log = []

    def add_user(self, username, role):
        if role not in ['Admin', 'Student', 'Guest']:
            print(f"[ERROR] Invalid role: {role}")
            return
        self.users[username] = User(username, role)
        print(f"[USER] Added {username} with role {role}")

    def can_access(self, username, operation):
        user = self.users.get(username)
        if not user:
            print(f"[ERROR] Unknown user '{username}'")
            return False

        # Permissions by role
        permissions = {
            'Admin': ['read', 'write', 'delete'],
            'Student': ['read', 'write'],
            'Guest': ['read']
        }

        if operation in permissions[user.role]:
            return True
        else:
            self._log_violation(username, operation)
            return False

    def _log_violation(self, username, operation):
        msg = f"[VIOLATION] {username} tried to perform '{operation}'"
        print(msg)
        self.access_log.append(msg)

    def show_log(self):
        print("\n🔐 Security Log:")
        for entry in self.access_log:
            print(entry)

# --- Example usage ---
if __name__ == "__main__":
    sm = SecurityModule()

    sm.add_user("ali", "Admin")
    sm.add_user("bilal", "Student")
    sm.add_user("guest1", "Guest")

    print("\nAccess attempts:")
    print("ali delete:", sm.can_access("ali", "delete"))  # ✅
    print("bilal delete:", sm.can_access("bilal", "delete"))  # ❌
    print("guest1 write:", sm.can_access("guest1", "write"))  # ❌
    print("bilal read:", sm.can_access("bilal", "read"))  # ✅

    sm.show_log()
