def campaign(names, pos, num):
    messages = []
    for i in range(pos, pos + num):
        messages.append("Estimado %s, vote por mí" % names[i])
    return messages


if __name__ == "__main__":
    import doctest
    doctest.testmod()