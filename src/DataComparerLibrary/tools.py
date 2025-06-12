class Tools:
    @staticmethod
    def is_integer(string):
        if string[0] == '-':
            # if a negative number
            return string[1:].isdigit()
        else:
            return string.isdigit()


    @staticmethod
    def get_full_typename(variable):
        variable_type = type(variable).__name__
        match variable_type:
            case 'float':
                long_variable_type = "float"
            case 'int':
                long_variable_type = "integer"
            case 'str':
                long_variable_type = "string"
            case _:
                long_variable_type = None
        return long_variable_type