from algosdk.transaction import LogicSigAccount
from base64 import b64decode

POOL_LOGICSIG_TEMPLATE = (
    "BoAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQBbNQA0ADEYEkQxGYEBEkSBAUM="
)

def get_pool_logicsig(
    validator_app_id: int, asset_a_id: int, asset_b_id: int
) -> LogicSigAccount:
    assets = [asset_a_id, asset_b_id]
    asset_1_id = max(assets)
    asset_2_id = min(assets)

    program = bytearray(b64decode(POOL_LOGICSIG_TEMPLATE))
    program[3:11] = validator_app_id.to_bytes(8, "big")
    program[11:19] = asset_1_id.to_bytes(8, "big")
    program[19:27] = asset_2_id.to_bytes(8, "big")
    return LogicSigAccount(program)


asset_a = 10458941 # Testnet USDC
asset_b = 0 # Algo
TINYMAN_ROUTER = 148607000 # Testnet router
#TINYMAN_ROUTER = 1002541853 # Mainnet router

logic_sig = get_pool_logicsig(TINYMAN_ROUTER, asset_a, asset_b)


print(logic_sig.address())