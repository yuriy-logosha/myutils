import myrequests
import myjson
import xml.etree.ElementTree as ET


class Result:
    el = None
    childs = []

    def __init__(self, el):
        self.el = el
        self.childs = [d[el.tag](child) for child in el]


class Corpus(Result):
    pass


class Sentence(Result):
    pass


class Word(Result):
    def __init__(self, el):
        super().__init__(el)
        for attrib in el.attrib:
            self.__dict__.update({attrib.lower(): el.attrib[attrib]})

        for kv in el.attrib['mi'].split('|'):
            kv_arr = kv.split('=')
            if len(kv_arr) > 1:
                self.__dict__.update({kv_arr[0].lower(): kv_arr[1]})


d = {"corpus": Corpus, 'SENTENCE': Sentence, 'NODE': Word}


def sentence_analyze(sentence):
    r = myrequests.get(
        "http://lindat.mff.cuni.cz/services/udpipe/api/process?tokenizer&tagger&parser&model=russian-syntagrus-ud-2.5-191206&data=" + sentence)

    if r and r.status_code == 200:
        parsed = myjson.json.loads(r.text)
        return [line.split('\t') for line in parsed['result'].split('#')[4].split('\n')[1:]]

    return None


def sentence_analyze_matxin(sentence):
    r = myrequests.get(
        "http://lindat.mff.cuni.cz/services/udpipe/api/process?tokenizer&tagger&parser&model=russian-syntagrus-ud-2.5-191206&output=matxin&data=" + sentence)

    if r and r.status_code == 200:
        root = ET.fromstring(myjson.json.loads(r.text)['result'])
        return Result(root).childs[0].childs[0]

    return None
