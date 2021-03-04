def domino(token):
    token = token.split()
    token_1 = token[0].split("-")
    token_2 = token[1].split("-")
    return (token_1[0] == token_2[0] or token_1[0] == token_2[1]
            or token_1[1] == token_2[0] or token_1[1] == token_2[1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()