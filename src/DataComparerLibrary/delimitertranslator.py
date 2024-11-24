class DelimiterTranslator(object):
    def __init__(self, file, old, new):
        self.file = file
        self.old = old
        self.new = new

    def write(self, s):
        self.file.write(s.replace(self.old, self.new))

    def close(self):
        self.file.close()

    def flush(self):
        self.file.flush()
