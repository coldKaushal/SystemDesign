import time

from KeyValueStore import KeyValueStore
from FileHandler import FileHandler
from ShardedDatabase import ShardedDatabase

"""
Initialising the sharded database with 5 partitions
"""
sharded_database = ShardedDatabase(5)


"""
Showing how the data is being stored and retrieved
"""

sharded_database.store_key_value_in_partition("kaushal", "aggarwal")
sharded_database.store_key_value_in_partition("rohan", "joshi")
sharded_database.store_key_value_in_partition("rahul", "aggarwal")
sharded_database.store_key_value_in_partition("akshay", "kumar")

key = "kaushal"
value = sharded_database.get_key_value_from_shard(key)

print(value)

key = "absurd"
value = sharded_database.get_key_value_from_shard(key)

print(value)

"""
Showing delete operation
"""

sharded_database.delete_key_in_partition("kaushal")
value = sharded_database.get_key_value_from_shard("kaushal")
print(value)

sharded_database.delete_key_in_partition("kaushal")
value = sharded_database.get_key_value_from_shard("kaushal")
print(value)

"""
Adding new partition
"""

sharded_database.add_partition(2)
value = sharded_database.get_key_value_from_shard("akshay")
print(value)



"""
Deleting partitions
"""

sharded_database.delete_partitions(4)
value = sharded_database.get_key_value_from_shard("akshay")
print(value)


