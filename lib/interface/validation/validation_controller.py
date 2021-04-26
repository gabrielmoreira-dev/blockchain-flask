from domain.use_case.validate_chain_uc import ValidateChainUCParams
from .validation_mapper import ValidationMapper


class ValidationController:
    def __init__(self, validate_chain_uc):
        self.validate_chain_uc = validate_chain_uc

    def validate_chain(self):
        params = ValidateChainUCParams()
        is_valid = self.validate_chain_uc.execute(params)
        return ValidationMapper.toVM(is_valid=is_valid)