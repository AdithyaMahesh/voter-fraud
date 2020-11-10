chmod +x deploy_blockchain.sh
chmod +x deploy_frontend.sh
sh ./deploy_blockchain.sh &  PIDIOS=$!
sh ./deploy_frontend.sh &  PIDMIX=$!
