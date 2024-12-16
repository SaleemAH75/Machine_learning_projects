import os

print('cwd is',os.getcwd())

# Define custom exceptions
class Error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class DataLoadingError(Error):
    pass

class DataProcessingError(Error):
    pass

class ModelTrainingError(Error):
    pass

class CustomFileNotFoundError(Error):
    pass

