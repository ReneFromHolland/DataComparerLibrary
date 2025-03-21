class Tools:
    @staticmethod
    def is_integer(string):
        if string[0] == '-':
            # if a negative number
            return string[1:].isdigit()
        else:
            return string.isdigit()
