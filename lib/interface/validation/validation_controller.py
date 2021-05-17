from domain.use_case.validate_chain_uc import ValidateChainUC
from .validation_mapper import ValidationMapper


class ValidationController:
    def __init__(self, validate_chain_uc: ValidateChainUC):
        self.validate_chain_uc = validate_chain_uc

    def validate_chain(self):
        is_valid = self.validate_chain_uc.execute()
        return ValidationMapper.toDict(is_valid=is_valid)