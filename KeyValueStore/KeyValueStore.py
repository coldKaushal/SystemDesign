from FileHandler import FileHandler


class KeyValueStore:
    def __init__(self):
        self.file_handler = FileHandler()

    def store_key_value(self, key, value, partition_name):
        try:
            data = self.file_handler.load_partition(partition_name)
            data[key] = value
            self.file_handler.save_data_in_partition(partition_name, data)
        except Exception as e:
            print(e)

    def get_value(self, key, partition_name):
        data = self.file_handler.load_partition(partition_name)
        if key in data:
            return data[key]
        else:
            raise ValueError("Key not found")

    def delete_key(self, key, partition_name):
        data = self.file_handler.load_partition(partition_name)
        if key in data:
            del data[key]
            self.file_handler.save_data_in_partition(partition_name, data)
            print(f"{key} deleted from the partition")
        else:
            raise ValueError(f"key not found: {key}")
