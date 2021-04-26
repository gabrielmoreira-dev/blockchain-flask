class ValidationMapper:
    def toVM(is_valid):
        message = 'The blockchain is valid' if is_valid else 'The blockchain is not valid'
        return {'message': message}
