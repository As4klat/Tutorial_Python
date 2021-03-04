def campaign_3a(names):
    messages = []
    for name in names:
        messages.append("Estimad" + ("o" if name[0] == "H" else "a") +
                        " %s, vote por mí" % name[1])
    return messages


def campaign_3b(names, pos, num):
    messages = []
    for i in range(pos, pos + num):
        messages.append("Estimad" + ("o" if names[i][0] == "H" else "a") +
                        " %s, vote por mí" % names[i][1])
    return messages


if __name__ == "__main__":
    import doctest
    doctest.testmod()