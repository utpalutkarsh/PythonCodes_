class HashTable:
    def __init__(self,size=7):
        self.data_map = [None]*size
    def __hash(self,key):
        my_hash = 0
        for letter in key :
            my_hash = (my_hash +ord(letter)*23)%len(self.data_map)
        return my_hash

    def print_table(self):
        for i, value in enumerate (self.data_map):
            print(i,":",value)
    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
           for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0]==key:
                 return self.data_map[index][i][1]
        return None

    def get_keys(self):
        all_key = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
               for j in range(len(self.data_map[i])):
                   all_key.append(self.data_map[i][j][0])
        return all_key

my_hash_table = HashTable(7)

my_hash_table.set_item("bolts",1200)
my_hash_table.set_item("washers",1000)
my_hash_table.set_item("cubic",8000)
my_hash_table.set_item("hero",4000)
my_hash_table.set_item("utpal",4000)

my_hash_table.print_table()

print(my_hash_table.get_keys())