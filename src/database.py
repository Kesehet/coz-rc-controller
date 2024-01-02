import json 
class DB:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            self.data = []

    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=4)

    def insert_row(self, row):
        if 'id' not in row:
            row['id'] = self._generate_unique_id()
        self.data.append(row)
        self.save_data()

    def delete_row(self, row_id):
        self.data = [row for row in self.data if row.get('id') != row_id]
        self.save_data()

    def find_row_by_id(self, row_id):
        for row in self.data:
            if row.get('id') == row_id:
                return row
        return None

    def get_rows(self):
        return self.data

    def clear_db(self):
        self.data = []
        self.save_data()

    def _generate_unique_id(self):
        if not self.data:
            return 1
        max_id = max([row.get('id', 0) for row in self.data])
        return max_id + 1