import hashlib

class RedundancyRemover:
    def __init__(self):
        self.database = {}
        self.false_positives = 0

    def check_redundancy(self, data):
        # Hash for validation mechanism
        data_hash = hashlib.sha256(data.encode()).hexdigest()
        
        if data_hash in self.database:
            # Classifies as redundant
            return "REDUNDANT - Duplicate Blocked"
        else:
            # Unique and verified - append to database
            self.database[data_hash] = data
            return "UNIQUE - Added to cloud database"

    def get_stats(self):
        return f"Database accuracy: {len(self.database)} unique entries"

# Testing
system = RedundancyRemover()
print(system.check_redundancy("user1@gmail.com"))
print(system.check_redundancy("user1@gmail.com")) # Block avvali
print(system.get_stats())
