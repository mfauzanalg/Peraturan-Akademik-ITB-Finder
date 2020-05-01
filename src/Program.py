import os
from BM import BM
from KMP import KMP
from nltk.tokenize import sent_tokenize

# print(os.listdir("../data"))

def getContain(teks, pattern):
    allSentences = sent_tokenize(teks.lower())
    notLow = sent_tokenize(teks)
    contain = []
    for i in range(len(allSentences)):
        ret = BM(allSentences[i], pattern.lower())
        if ret: #if not empty
            contain.append(allSentences[i])
    return contain

def combine(list1, filename):
    merged = [(list1[i], filename) for i in range(0, len(list1))]
    return merged


def process(filename, pattern):
    f = open(filename, "r")
    T = f.read().lower()
    P = pattern.lower()

    contain = getContain(T,P)
    Pasal = filename[8:(len(filename)-4)]
    hasil = combine(contain, Pasal)

    return hasil

def main():
    P = "kode etik"
    hasil = process("../data/Pasal 1.txt", P)
    print(hasil)

if __name__ == "__main__":
    main()
