class SaveUtil:
    @staticmethod
    def toDict(movies):
        return [movie.__dict__ for movie in movies]