class PrintWordsInReverse:
    def print(self, sentence):
        words = sentence.split()
        result = []
        for word in words:
            result.append(word[::-1])

        return " ".join(result)
if __name__ == '__main__':
    print(PrintWordsInReverse().print("Always keep one finger on the Escape key"))
