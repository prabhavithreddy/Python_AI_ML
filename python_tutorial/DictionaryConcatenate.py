class DictionaryConcatenate:
    def concatenate(self, *args):
        if not args:
            return {}
        concatenated_dictionary = {}
        for arg in args:
            concatenated_dictionary.update(arg)
        return concatenated_dictionary
if __name__ == '__main__':
    print(DictionaryConcatenate().concatenate(
        {'A':1, 'B':2}, {'C':3, 'D':4}, {'E':5, 'F':6}
    ))
