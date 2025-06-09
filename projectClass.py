from absctractClass import *

class Project(AbsctractTask):
    def __init__(self, table_id, name, description):
        super().__init__(table_id, name, description)
        self.peoples = []

    def full_description(self):
        description = super().full_description()
        description += f'{self.peoples}'
        return description
