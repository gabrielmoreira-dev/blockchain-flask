from domain.use_case.create_block_uc import CreateBlockUCParams
from .provider import create_block_uc
from .app import app

params = CreateBlockUCParams(proof=1, previous_hash='0')
create_block_uc.execute(params)

if __name__ == "__main__":
    app.run(debug=True)