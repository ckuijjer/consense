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

    describe('GET /getTestResponseFromServer', () => {
        it('it should GET status 200 with body "ok"', (done) => {
            chai.request(server)
                .get('/getTestResponseFromServer')
                .end((err, res) => {
                    res.should.have.status(200);
                    res.body.should.equal('ok');
                    done();
                });
        });
    });

    describe('GET /getAvailableResearchData', () => {
        it('it should GET proper response ', (done) => {
            chai.request(server)
                .get('/getAvailableResearchData')
                .end((err, res) => {
                    res.should.have.status(200);
                    // res.body.should.be.a('object');
                    // res.body['numberOfPeople'].should.equal(7);
                    res.body.should.equal('(: ysae saw ti dias ydobon');
                    done();
                });
        });
    });

    after( () => forkedServer.kill() );
});
