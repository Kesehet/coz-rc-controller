class ConnectionType:
    def __init__(self, chosenType):
        self.types = [
            "RC",
            "GCP",
            "AWS",
            "AZ",
            "OP"
        ]

        if(self.isValidType(chosenType)):
            self.type = chosenType
        else:
            Exception("Invalid Connection Type")
            

    def __str__(self):
        return self.type
    
    def isValidType(self, chosenType):
        for t in self.types:
            if t == chosenType:
                return True
        return False
