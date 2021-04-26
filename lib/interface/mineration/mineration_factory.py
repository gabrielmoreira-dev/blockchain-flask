from lib.provider import get_previous_block_uc, get_proof_of_work_uc, get_hash_uc, create_block_uc
from .mineration_controller import MinerationController


class MinerationFactory:
    def makeController():
        return MinerationController(get_previous_block_uc,
                                    get_proof_of_work_uc, get_hash_uc,
                                    create_block_uc)
