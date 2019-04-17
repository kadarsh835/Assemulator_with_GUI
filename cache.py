import math
from bitstring import BitArray
from memory import memory

class cache:
    def __init__(self, cache_size = 512, block_size = 4, mapping_type, number_of_ways): # Cache_size: number of blocks; Block size: Number of Words
        self.cache_size = cache_size    #number of blocks
        self.block_size = block_size    # Number of Words
        self.mapping_type = mapping_type
        self.number_of_ways = number_of_ways
        self.cache_list = {}
        self.memory_object = memory()

    def word_to_be_written(self,value):
        value = BitArray(int = value, length = 32).bin
        b3 = value[0:8]
        b2 = value[8:16]
        b1 = value[16:24]
        b0 = value[24:32]
        temp_list = [b0, b1, b2, b3]
        return temp_list

    def direct_mapped(self,address):
        address = BitArray(int=address, length=32).bin
        number_of_blocks = int(cache_size/block_size)

        block_bits = int(math.log2(cache_size))
        word_bits = int(math.log2(block_size))
        total_bits = word_bits + block_bits + 2
        
        self.no_of_cache_hits=0
        self.no_of_cache_miss=0
        
        tag_bits=32-total_bits
        index=address[tag_bits : tag_bits + block_bits]

        if index in cache_list.keys():
            if(cache_list[index][0] == address[0:tag_bits]):      #tag field
                no_of_cache_hits += 1
                print('cache hit')
                return cache_list[index][1]
            else:
                no_of_cache_miss += 1
                prit('cache miss')
                value = memory_object.readWord(address)
                cache_list[index] = [address[0:tag_bits], word_to_be_written(value)]
                memory_object.writeWord(address,value)

        else:
            value = memory_object.readWord(address)
            cache_list[index] = [address[0:tag_bits], word_to_be_written(value)]