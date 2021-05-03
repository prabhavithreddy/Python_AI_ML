class Problem1:
    '''Using escape sequence print each word in different lines'''
    
    def split_lines(self, sentence):
        if not sentence:
            return None
        return sentence.split(" ")

    def split_lines_without_inbuilt_function(self, sentence):
        if not sentence:
            return None
        list_of_words = []
        word = ''
        for index in range(0,len(sentence)):
            char = sentence[index]
            if char == ' ':
                list_of_words.append(word)
                word = ''
            else:
                word = word+char
        if word:
            list_of_words.append(word)
        return list_of_words
    

if __name__ == '__main__':
    # for word in Problem1().split_lines('Hey! Welcome to edureka!'):
    #     print(word)

    for word in Problem1().split_lines_without_inbuilt_function('Hey! Welcome to edureka!'):
        print(word)