from lib.provider import blockchain_repository
from domain.use_case.validate_chain_uc import ValidateChainUC
from .validation_controller import ValidationController


class ValidationFactory:
    def makeController():
        validate_chain_uc = ValidateChainUC(blockchain_repository)
        return ValidationController(validate_chain_uc)