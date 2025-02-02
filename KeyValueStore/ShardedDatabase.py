import hashlib
from KeyValueStore import KeyValueStore
from FileHandler import FileHandler
import os

class ShardedDatabase(KeyValueStore):
    def __init__(self, partitions: int):
        if partitions <= 0:
            raise ValueError("Partitions should be greater than 0")
        super().__init__()
        self.partitions = partitions
        self.file_handler = FileHandler()
        self.directory_name = "filestorage"
        self.file_handler.clean_up(self.directory_name)
        self.file_handler.create_directory(self.directory_name)
        self.partition_name_prefix = "partition"
        self.create_partitions()

    def create_partitions(self):
        for i in range(self.partitions):
            partition_name = self.generate_partition_name(i)
            self.file_handler.create_partition(partition_name)

    def store_key_value_in_partition(self, key, value):
        partition_value = self.find_partition(key)
        partition_name = self.generate_partition_name(partition_value)
        super().store_key_value(key, value, partition_name)

    def get_key_value_from_shard(self, key):
        partition = self.find_partition(key)
        partition_name = self.generate_partition_name(partition)
        try:
            return self.get_value(key, partition_name)
        except ValueError:
            print(f"Key not found in the shard: {key}")

    def find_partition(self, key: str):
        hash_object = hashlib.sha256(key.encode())
        hash_int = int(hash_object.hexdigest(), 16)
        partition_value = hash_int % self.partitions
        print(f"Partition for {key} is {partition_value}")
        return partition_value

    def delete_key_in_partition(self, key):
        partition_value = self.find_partition(key)
        partition_value = self.generate_partition_name(partition_value)
        try:
            super().delete_key(key, partition_value)
        except ValueError:
            print("Key not found in shard, we can not delete it")

    def add_partition(self, partition_to_increase):
        total_new_partitions = self.partitions + partition_to_increase
        for partition_value in range(self.partitions, total_new_partitions):
            partition_name = self.generate_partition_name(partition_value)
            self.file_handler.create_partition(partition_name)
        self.partitions = total_new_partitions

        for partition_value in range(total_new_partitions):
            partition_name = self.generate_partition_name(partition_value)
            data = self.file_handler.load_partition(partition_name)

            for key, value in data.items():
                new_partition_value = self.find_partition(key)
                if new_partition_value == partition_value:
                    continue
                new_partition_name = self.generate_partition_name(new_partition_value)
                super().store_key_value(key, value, new_partition_name)


    def delete_partitions(self, partitions_to_delete: int):
        if partitions_to_delete >= self.partitions:
            raise ValueError("Existing partitions are less than or equal partitions you are requesting to delete")

        print(f"Existing partitions {self.partitions}")
        total_previous_partition = self.partitions
        self.partitions -= partitions_to_delete
        print(f"Total new partitions {self.partitions}")
        for partition_value in range(self.partitions, total_previous_partition):
            partition_name = self.generate_partition_name(partition_value)
            data = self.file_handler.load_partition(partition_name)
            print(f"Data extracted from file {partition_name}")
            for key, value in data.items():
                new_partition_value = self.find_partition(key)
                new_partition_name = self.generate_partition_name(new_partition_value)
                super().store_key_value(key, value, new_partition_name)
                print(f"Stored new key in partition {new_partition_name}")
            self.file_handler.delete_partition(partition_name)

    def get_partitions(self):
        return self.partitions

    def generate_partition_name(self, partition):
        return self.directory_name + "/" + self.partition_name_prefix + str(partition) + ".json"

