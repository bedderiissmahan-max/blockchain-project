import hashlib
import time

# ------------------------
# 1) Block Class
# ------------------------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Step 4 — Mining
    def mine_block(self, difficulty):
        print(f"Mining block {self.index}...") 
        
        
        while  self.hash [:difficulty] !="0"*difficulty:
            self.nonce += 1
            self.hash =self.compute_hash()
            print(f" Block mined: {self.hash}")
            print(f"Nonce: {self.nonce}")
            
            
            
            
        

        


# ------------------------
# 2) Blockchain Class
# ------------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data, difficulty=1):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            data=data,
            previous_hash=last_block.hash
        )
        new_block.mine_block(difficulty)
        self.chain.append(new_block)
        
    def print_chain(self):
      for block in self.chain:
        print("======================")
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")
    # Step 5 — Validation
    def is_chain_valid(self, difficulty=1):
        required_prefix = "0" * difficulty

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # 1) التحقق من الهاش
            if current.hash != current.compute_hash():
                print("❌ Error: Block", current.index, "hash is invalid!")
                return False

            # 2) التحقق من previous hash
            if current.previous_hash != previous.hash:
                print("❌ Error: Block", current.index, "previous hash is invalid!")
                return False

            # 3) التحقق من mining
            if not current.hash.startswith(required_prefix):
                print("❌ Error: Block", current.index, "was not mined correctly!")
                return False

        return True


# ------------------------
# 3) Test the blockchain
# ------------------------c
if __name__ == "__main__":
    bc = Blockchain()

    print("\nMining Block 1...")
    bc.add_block("Block 1 data", difficulty=1)

    print("\nMining Block 2...")
    bc.add_block("Block 2 data", difficulty=1)

    print("\nMining Block 3...")
    bc.add_block("Block 3 data", difficulty=1)    
    bc.chain[1].data = "Hacked data"

    # Print chain
print("\n================== FULL CHAIN ==================\n")
for block in bc.chain:
        print("Index:", block.index)
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Nonce:", block.nonce)
        print("Hash:", block.hash)
        print("Prev Hash:", block.previous_hash)
        print("-----------------------------------")
       
       
        print("\nBlockchain Validity:", bc.is_chain_valid())