chmod +x scripts/deploy_blockchain.sh
chmod +x scripts/deploy_frontend.sh
sh ./scripts/deploy_blockchain.sh &  PIDIOS=$!
sh ./scripts/deploy_frontend.sh &  PIDMIX=$!
