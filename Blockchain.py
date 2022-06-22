def get_parent_hash(block):
	return block[0]
def get_transactions(block):
	return block[1]
def get_hash_itself(block):
	return block[2]
# creating new blockchain
def create_block(transactions, parent_hash):
hash_itself = hash((transactions, parent_hash))
	return (parent_hash, transactions, hash_itself)
#  creating new genesis block
def create_genesis_block(transactions):
	return create_block(transactions, 0)
genesis_block = create_genesis_block("Nick transferred medical files to John")
genesis_block_hash = get_hash_itself(genesis_block)
print "genesis_block_hash:", genesis_block_hash
block1 = create_block("John gave files to James, Nick is able to track all file distributions", genesis_block_hash)
block1_hash = get_hash_itself(block1)
print "block1_hash:", block1_hash
# proof of work verification process
>>>   def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
         
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
                 
        return new_proof
