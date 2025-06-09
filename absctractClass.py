class AbsctractTask:  # не делать экземпляры
    def __init__(self, table_id, name, description):
        self.table_id = table_id
        self.next_task = [] # дочерняя задача
        self.name = name
        self.description = description

    def full_description(self):
        description = ''
        description += self.name
        description += '\n'
        description += self.description

        return description