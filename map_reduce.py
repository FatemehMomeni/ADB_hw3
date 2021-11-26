from __future__ import unicode_literals
import mapper
import reducer


path = 'D:/Mine/computerUI/terms/masters/term1/advancedDB/hw/3'
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '#', '@', '!', '*', '.', ',', '?', '/',
          '(', ')', '[', ']', '$', '€', ':', ';', '-', '+', '"', '▼&►']


if __name__ == "__main__":
    data_set_file = open(path + "/tmp.txt", 'r', encoding='utf-8')
    data_set = data_set_file.read().split()
    data_set_file.close()

    no_number = [x for x in data_set if x[0] not in digits]

    stop_words_file = open(path + '/stopWords.txt', 'r', encoding='utf-8')
    stop_words = stop_words_file.read().split()
    stop_words_file.close()

    for i in range(len(no_number)):
        no_number[i] = no_number[i].lower()

    pure_words = [x for x in no_number if x not in stop_words]

    ds_words = mapper.mapping(pure_words)
    repeat = reducer.reduce(ds_words)

    repeat.sort(key=lambda x: x[1])
    repeat.reverse()
    print(repeat[:10])
