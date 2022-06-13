import pytest
from pip._internal.vcs import git


def DominoAlgorithm(text, iteracje):
    for i in range(iteracje):
        output = ""
        text = "|" + text + "|"
        for j in range(1, len(text) - 1):
            poprzedni = text[j - 1]
            aktualny = text[j]
            nastepny = text[j + 1]
            if poprzedni == "|":
                if aktualny == "\\":
                    output += "\\"
                elif aktualny == "|":
                    if nastepny == "\\" :
                        output += "\\"
                    else:
                        output += "|"
                else:
                    output += "/"
            elif poprzedni == "/":
                if aktualny == "|":
                    if nastepny == "\\":
                        output += "|"
                    else:
                        output += "/"
                elif aktualny == "\\":
                    output += "\\"
                else:
                    output += "/"
            else:
                if aktualny == "|":
                    if nastepny == "\\":
                        output += "\\"
                    else:
                        output += "|"
        text = output
    return text

def BackwardDominoAlgorithm(text, iteracje):
    for i in range(iteracje):
        output = ""
        text = "|" + text + "|"
        for j in range(1, len(text) - 1):
            poprzedni = text[j - 1]
            aktualny = text[j]
            nastepny = text[j + 1]
            if aktualny == "|":
                output += "|"
            elif aktualny == "/":
                if poprzedni == "/":
                    if nastepny == "/":
                        output += "/"
                    else:
                        output += "|"
                else:
                    output += "/"
            else:
                if nastepny == "\\":
                    output += "|"
                else:
                    output += "\\"
        text = output
    return output