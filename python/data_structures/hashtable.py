from mpmath import mp

class Hashtable:

    def __init__(self):
        self.core = [False]*1000

    def set(self, key, value):
        index = self.hash(key)
        self.core[index] = [key, value]

    def get(self, key):
        index = self.hash(key)
        value = self.core[index][1]
        return value

    def has(self, key):
        index = self.hash(key)
        key_value = self.core[index]
        if not key_value:
            return False
        elif key_value[0] == key:
            return True
        else:
            return False

    def keys(self):
        key_list = []
        for index in range(len(self.core)):
            if self.core[index]:
                key_list.append(self.core[index][0])
        return key_list


    def hash(self, key):
        mp.dps = 100
        pi = mp.pi
        summation = 0

        for index, character in enumerate(key):
            summation+=ord(character)*pi*10**index

        hash_value = int(summation%len(self.core))

        return hash_value
