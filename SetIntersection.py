class SetIntersection:
    def is_word_exists(self, a:set, b:set, word:str):
        if a and b and word:
            intersection_list = list(a.intersection(b))
            intersection_list.sort()
            word_list = list(set(list(word)))
            word_list.sort()
            result = "".join(intersection_list) == "".join(word_list)
        return result
if __name__ == '__main__':
    print(SetIntersection().is_word_exists(set(['c','a','d','e','k','r','u','q','r','y']),
                                           set(['b','h','k','a','d','e','k','r','u']),
                                           'edureka'))
