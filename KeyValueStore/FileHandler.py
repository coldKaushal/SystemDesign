import json
import os.path
from pathlib import Path
from turtledemo.sorting_animate import partition
import shutil

class FileHandler:
    def __init__(self):
        pass

    def load_partition(self, partition_name: str):
        if not partition_name.endswith(".json"):
            raise ValueError("incorrect partition format")
        try:
            with open(partition_name, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Partition not found, creating partition")
            self.create_partition(partition_name)
            return {}
        except Exception as e:
            print(e)

    def save_data_in_partition(self, partition_name, data):
        try:
            with open(partition_name, "w", encoding="utf-8") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)

    def delete_partition(self, partition_name):
        try:
            file = Path(partition_name)
            if file.exists():
                file.unlink()
        except Exception as e:
            print(e)

    def create_partition(self, partition_name):
        try:
            with open(partition_name, "w") as file:
                json.dump({}, file)
        except Exception as e:
            print(e)

    def clean_up(self, directory_name):
        try:
            shutil.rmtree(directory_name)
        except Exception as e:
            print(e)

    def create_directory(self, directory_name):
        try:
            Path(directory_name).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(e)