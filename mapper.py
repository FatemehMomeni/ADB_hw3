def mapping(data_set):
    ds_words = list(tuple())

    for word in data_set:
        ds_words.append((word, 1))  # mapper output

    return ds_words

