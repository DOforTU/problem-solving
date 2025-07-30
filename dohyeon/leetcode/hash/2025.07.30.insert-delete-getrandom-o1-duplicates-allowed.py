import random

class RandomizedCollection:

    def __init__(self):
        self.val_to_index = {} # {key1: (index1, index2, ...), key2: (index1, index2, ...)}
        self.values = []        

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            self.val_to_index[val].add(len(self.values))
            self.values.append(val)
            return False
        self.val_to_index[val] = set([len(self.values)])
        self.values.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index or not self.val_to_index[val]:
            return False
    
        # val의 인덱스 중 하나를 꺼냄
        remove_idx = self.val_to_index[val].pop()
        last_val = self.values[-1]
    
        # 삭제할 값이 마지막 값이 아니면 위치 교환
        if remove_idx != len(self.values) - 1:
            self.values[remove_idx] = last_val
            # last_val의 인덱스 set 갱신
            self.val_to_index[last_val].remove(len(self.values) - 1)
            self.val_to_index[last_val].add(remove_idx)
    
        # 마지막 요소 제거
        self.values.pop()
        # val의 인덱스 set이 비면 dict에서 삭제
        if not self.val_to_index[val]:
            del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()