from typing import *
import stanza

class Analyzer(object):
    def __init__(self, language="la"):
        self.nlp = stanza.Pipeline(language, verbose=False)
    
    def __parse_fts(self, ft_str: str) -> Dict[str, str]:
        splt_fts: List[str] = ft_str.split("|")
        fts: Dict[str, str] = {}

        for raw in splt_fts:
            key, value = raw.split("=")
            fts[key] = value
        
        return fts

    
    def analyze(self, raw_sent: str) -> List[Dict[str, str]]:
        doc = self.nlp(raw_sent)
        analysis: List[Dict[str, str]] = []

        for sent in doc.sentences:
            for word in sent.words:
                dict_word: Dict[str, Union[str, int]] = word.to_dict()
                lemma: str = dict_word["lemma"]
                orig: str = dict_word["text"]
                pos: str = dict_word["upos"].lower()
                raw_fts: str = dict_word.get("feats", None)

                if raw_fts != None:
                    parsed_fts: Dict[str, str] = self.__parse_fts(raw_fts)
                else:
                    parsed_fts: Dict[str, str] = {}

                parsed_fts["lemma"] = lemma
                parsed_fts["pos"] = pos
                parsed_fts["orig_text"] = orig

                analysis.append(parsed_fts)
        return analysis