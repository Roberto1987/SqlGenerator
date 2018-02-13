class String:

    def __init__(self, field):
        self.APEX = '\''
        self.field = self.APEX + field + self.APEX

    def getField(self):
        return self.field

