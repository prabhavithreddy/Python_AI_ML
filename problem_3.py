class Problem3:
    '''Write a program to create a list of even numbers starting from x to y'''
    
    def replace_string(self, sentence: str, word_to_replace):
        if not sentence:
            return sentence

        return sentence.replace(word_to_replace, '')


if __name__ == '__main__':
    print(Problem3().replace_string("Hello! I love apples apples oranges", 'apples '))