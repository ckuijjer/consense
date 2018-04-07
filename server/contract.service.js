const Web3 = require('web3');
const Tx = require('ethereumjs-tx');
const ABI = require('../contracts/abi.js');
const web3 = new Web3(new Web3.providers.HttpProvider("https://rinkeby.infura.io/km4Q8LLtFj8l2MUPJp2K"));

export class ContractService {

    constructor() {
        this.contractAddress = '0x2Eab1392d6850722d19BEc5738912fbdb021277F';
        this.contract = new web3.eth.Contract(ABI, contractAddress);
        this.privateKey = new Buffer('3e97d8bff009922304b47078792009c57af30ed0ea40b0d9d12d79cdb3f9c9d0', 'hex');
        this.publicKey = web3.eth.accounts.privateKeyToAccount(this.privateKey);
    }

    sendTransaction(callback) {
        web3.eth.getTransactionCount(this.publicKey).then(transactionCount => {
            data = contract.methods['methodName'](params).encodeABI();
            const rawTx = {
                nonce: web3.utils.toHex(transactionCount),
                gasPrice: web3.utils.toHex(web3.utils.toWei('20', 'gwei')),
                gasLimit: '0x186a0',
                to: contractAddress,
                value: web3.utils.toHex(web3.utils.toWei('0.0001', 'ether')),
                data: data
            }

            const tx = new Tx(rawTx);
            tx.sign(privateKey);

            const serializedTx = tx.serialize();

            web3.eth.sendSignedTransaction('0x' + serializedTx.toString('hex'))
                .on('receipt', (r) => {
                    console.log(r);
                    i++;
                    send(array[i][0], array[i][1], array[i][2]);
                });
        });
    }
}


