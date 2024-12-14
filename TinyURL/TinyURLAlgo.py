import random

hash_map = {}
def TinyURL(long_url):
    if long_url in hash_map:
        return hash_map[long_url]
    base_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    length_of_base_chars = len(base_chars)
    while True:
        tinyURL = ""
        for i in range(6):
            index = random.randint(0, length_of_base_chars-1)
            tinyURL += base_chars[index]
        
        if tinyURL not in hash_map:
            hash_map[long_url] = tinyURL
            break
    
    return hash_map[long_url]


if __name__ == "__main__":
    print(TinyURL("kaushalaggarwal"))
