def reduce(ds_words):
    repeat = list(tuple())

    for i in range(len(ds_words)):
        new = True
        for j in range(len(repeat)):
            if ds_words[i][0] == repeat[j][0]:
                new = False
                break
        if new:
            counter = 1
            for j in range(i+1, len(ds_words)):
                if ds_words[i][0] == ds_words[j][0]:
                    counter += 1
            repeat.append((ds_words[i][0], counter))

    return repeat
