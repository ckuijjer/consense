pragma solidity ^0.4.21;

/**
 * Consense contract version 0.2.1
 */

contract Consense {

    struct Consent {
        /*
        string metaDataHash;
        string preferencesHash;
        string matchmakingHash;
        */
        bool isParticipating;
        bool consentGiven;
    }

    mapping(address => Consent) public consents;

    modifier onlyParticipant(){
        require(consents[msg.sender].isParticipating == true);
        _;
    }

    function Consense(address[] _participantList) public {
        for (uint i = 0; i < _participantList.length; i++) {
            consents[_participantList[i]].isParticipating = true;
        }
    }

    function giveConsent() 
        public 
        onlyParticipant {
        consents[msg.sender].consentGiven = true;
    }

    function withdrawConsent() 
        public 
        onlyParticipant {
        consents[msg.sender].consentGiven = false;
    }

    function checkConsent(address participant) public view returns (bool) {
        return consents[participant].consentGiven;
    }

}