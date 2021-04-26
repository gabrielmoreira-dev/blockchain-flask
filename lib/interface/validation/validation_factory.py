from lib.provider import validate_chain_uc
from .validation_controller import ValidationController


class ValidationFactory:
    def makeController():
        return ValidationController(validate_chain_uc)