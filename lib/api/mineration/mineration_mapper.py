import dataclasses


class MinerationMapper:
    def toDict(block):
        blockDict = dataclasses.asdict(block)
        blockDict['message'] = 'Congratulations, you just mined a block!'
        return blockDict