from lib.provider import address_repository, blockchain_repository
from domain.use_case.create_block_uc import CreateBlockUC, CreateBlockUCParams
from .app import app

# Genesis block
create_block_uc = CreateBlockUC(blockchain_repository)
params = CreateBlockUCParams(proof=1, previous_hash='0', transactions=[])
create_block_uc.execute(params)

if __name__ == "__main__":
    app.run(debug=True)