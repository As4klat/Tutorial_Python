def domino(token_1, token_2):
    return (token_1[0] == token_2[0] or token_1[0] == token_2[1]
            or token_1[1] == token_2[0] or token_1[1] == token_2[1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()