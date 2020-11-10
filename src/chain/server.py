# imports
from chain import Blockchain
from flask import Flask, request

# initializing flask

app = Flask(__name__)


# constructing the blockchain
blockchain = Blockchain()

# creating the genesis (starting) block
blockchain.create_genesis_block()

peers = {}

# to add a new "transaction" to the chain
@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    required_fields = ["student", "vote"]
    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 403
    tx_data["timestamp"] = time.time()
    blockchain.add_new_transaction(tx_data)
    return "Success", 201




@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data,
                       "peers": list(peers)})
