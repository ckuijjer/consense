process.env.NODE_ENV = 'test';

const fork = require('child_process').fork;
const chai = require('chai');
const chaiHttp = require('chai-http');
const should = chai.should();
chai.use(chaiHttp);

const server = 'http://localhost:3000';

describe('Consense Server App', () => {

    let forkedServer;

    before((done) => {
        // syncing
        forkedServer = fork('app.js');
        forkedServer.on('message', function (msg) {
            if (msg === 'listening') {
              done();
            }
        });
    });

    describe('GET /getAvailableResearchData', () => {
        it('it should GET { numberOfPeople: 7 } ', (done) => {
            chai.request(server)
                .get('/getAvailableResearchData')
                .end((err, res) => {
                    res.should.have.status(200);
                    res.body.should.be.a('object');
                    res.body['numberOfPeople'].should.equal(7);
                    done();
                });
        });
    });

    after( () => forkedServer.kill() );
});
