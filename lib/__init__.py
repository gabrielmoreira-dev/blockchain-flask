from domain.use_case.set_node_address_uc import SetNodeAddressUC
from lib.provider import address_repository, blockchain_repository
from domain.use_case.create_block_uc import CreateBlockUC, CreateBlockUCParams
from domain.use_case.set_node_address_uc import SetNodeAddressUC
from .app import app

set_node_address_uc = SetNodeAddressUC(address_repository)
set_node_address_uc.execute()

# Genesis block
create_block_uc = CreateBlockUC(blockchain_repository)
params = CreateBlockUCParams(proof=1, previous_hash='0', transactions=[])
create_block_uc.execute(params)

if __name__ == "__main__":
    app.run(debug=True)