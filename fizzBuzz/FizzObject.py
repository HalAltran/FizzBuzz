class FizzObject:
    def __init__(self, name: str, permanent: bool, delete_others: bool, priority: int):
        self.name = name
        self.permanent = permanent
        self.delete_others = delete_others
        self.priority = priority
