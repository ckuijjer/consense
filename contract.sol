pragma solidity ^0.4.21;
contract CollectConsentFromList{
    struct Consent{
        address consentGiver;
        int consentHash;
        bool consentGiven;
    }
    
    
    address creator;
    address[] participantList;
    // participantList is a sorted array of hashes that can be searched with binary search
    function CollectConsentFromList(address[] _participantList) {
        creator = msg.sender;
        participantList = _participantList;
        Consent[participantList.length] public consentList;
        for 
    }
    function addConsent(address consentGiver, int consentHash, int consentGiven) private returns(Consent[] _consentList){
        if(msg.sender is on the list) return;
        agreements.push(Consent(consentGiver, consentHash, consentGiven));
    }    
    function withdrawConsent(Consent[] _consentList, address consentGiver) private returns(Consent[] _consentList){
    //flip consentList for given address to bool = 0;
    }
    function binarySearch(address[] _participantList, address participantToFind) private returns(bool isOnTheList){
        for i in range(0,_particpantList.length)
            if found => isOnTheList = 1;
            else isOnTheList = 0;
    }

}
