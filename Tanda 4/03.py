def campaign(names):
    messages = []
    for name in names:
        messages.append("Estimado %s, vote por mí" % name)
    return messages


if __name__ == "__main__":
    import doctest
    doctest.testmod()