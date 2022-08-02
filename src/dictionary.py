from typing import *
import slob

class Dictionary:
    def __init__(self, dict_fp="data/Simpson1959-slob/Simpson1959-lat-eng.slob"):
        self.dict_fp = dict_fp
        self.__load()

    def __load(self):
        f = slob.open(self.dict_fp)
        d = f.as_dict()
        print(d)

    def tgt_to_src(self, tgt_word: str) -> Optional[str]:
        pass