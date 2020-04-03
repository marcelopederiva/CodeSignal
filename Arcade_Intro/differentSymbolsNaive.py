from collections import OrderedDict
def differentSymbolsNaive(s):
    result = "".join(OrderedDict.fromkeys(s))
    return len(result)
