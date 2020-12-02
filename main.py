greeting = "Hello world"


def find(sourceStr, subStr):
    sourceLength = len(sourceStr)
    substrLength = len(subStr)
    result = -1

    i = 0
    matches = False

    while i < sourceLength:
        matches = False
        j = 0

        while j < substrLength:
            if sourceStr[i + j] == subStr[j]:
                matches = True
            else:
                matches = False
                break
            j = j + 1

        if matches:
            result = i

        i = i + 1

    return result


print(find("     Hello world  ", "world"))
