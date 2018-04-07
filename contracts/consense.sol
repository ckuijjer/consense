pragma solidity ^0.4.21;

/**
 * Consense contract version 0.1.0
 */

contract Consense {

    address creator;

    struct Consent {
        string metaDataHash;
        string preferencesHash;
        string matchmakingHash;
        bool isParticipating;
        bool consentGiven;
    }

    mapping(address => Consent) public consents;

    function Consense(address[] _participantList) public {
        for (uint index = 0; index < _participantList.length; index++) {
            consents[_participantList[index]].isParticipating = true;
        }
        creator = msg.sender;
    }

    function giveConsent() public {
        consents[msg.sender].consentGiven = true;
    }

    function withdrawConsent() public {
        consents[msg.sender].consentGiven = false;
    }

    function checkConsent() public view returns (bool) {
        return consents[msg.sender].consentGiven;
    }

}