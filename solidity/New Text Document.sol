// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract myHealthv8 {
    struct AccessControlList {
        string uid; // The one giving permission
        string receiverUid; // The one receiving permission
        string note; // Permission notes
    }

    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}

    // Fallback function is called when msg.data is not empty
    fallback() external payable {}

    function GetBalance() public view returns (uint) {
        return address(this).balance;
    }

    function AddBalanceToSender() external{
        payable(msg.sender).transfer(1000000000000000);
    }

    // An array of 'ACL' structs
    AccessControlList[] private AccessControlLists;

    // Add new entry  permission for uid
    // Make sure to use GetPermission first to avoid double entry, always return ture
    function AddPermission(string calldata _senderUid, string calldata _receiverUid, string calldata _note) public returns (bool){
        AccessControlList memory acl;
        acl.uid = _senderUid;
        acl.receiverUid = _receiverUid;
        acl.note = _note ;
        AccessControlLists.push(
            acl);
        return true;
    }

    // delete entry permission
    // check first for the permission if exist, otherwise return false
    function DeletePermission(string calldata _uid, string calldata _receiverUid) public returns (bool result) {
        uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                if(CompareStrings(AccessControlLists[i].receiverUid, _receiverUid)){
                    AccessControlLists[i] = AccessControlLists[AccessControlLists.length-1];
                    AccessControlLists.pop();
                    return true;
                }
            }
        }
        return false;
    }

    // Make sure to check whether the uid exist, retuning list of permitted uid, otherwise return empty list
    function GetPermissionList(string calldata _uid) public view returns (string[] memory){
        string[] memory list = new string[](CountPermissionUid(_uid));
        uint _aclLength = AccessControlLists.length;
        uint j = 0;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                list[j] = AccessControlLists[i].receiverUid;
                j++;
            }
        }
        return list;
    }

    // Make sure to check whether the uid exist, retuning list of permitted uid, otherwise return empty list
    function GetPendingPermissionList(string calldata _uid) public view returns (string[] memory){
        // this list is the one that adding _uid to permission
        string[] memory listAdding = new string[](CountPermissionReceivingUid(_uid));

        // this list is the one that _uid have added to the permission
        string[] memory listAdded = GetPermissionList(_uid);

        // get the one that add the uid to the permission
        uint j;
        uint _aclLength = AccessControlLists.length;
        j = 0;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].receiverUid, _uid)){
                listAdding[j] = AccessControlLists[i].uid;
                j++;
            }
        }

        // get count of the one that uid did not add to the permission
        // Dont use the getpermission function to save computing power

        uint _countAdded = listAdded.length;
        uint _countAdding = listAdding.length;
        j = 0;
        for(uint i=0; i<_countAdding; i++){
            bool _match = false;
            for(uint k=0; k<_countAdded; k++){
                if(CompareStrings(listAdding[i], listAdded[k])){
                    _match = true;
                    break;
                }
            }
            // Add count if theres NO match
            if(!_match){
                j++;
            }
        }

        // this list is the one that _uid not add user is listAdding
        string[] memory listPending = new string[](j);
        j = 0;
        for(uint i=0; i<_countAdding; i++){
            bool _match = false;
            for(uint k=0; k<_countAdded; k++){
                if(CompareStrings(listAdding[i], listAdded[k])){
                    _match = true;
                    break;
                }
            }
            // Add count if theres NO match
            if(!_match){
                listPending[j] = listAdding[i];
                j++;
            }
        }
        
        return listPending;
    }

    // Check uid for receiving permission
    // Make sure to check whether the uid exist, otherwise return false
    function GetPermission(string calldata _uid, string calldata _receiverUid) public view returns (bool result) {
        uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                if(CompareStrings(AccessControlLists[i].receiverUid, _receiverUid)){
                    return true;
                }
            }
        }
        return false;
    }

    // Check notes for receiving permission
    // Make sure to check whether the uid exist, otherwise return empty string
    function GetPermissionNote(string calldata _uid, string calldata _receiverUid) public view returns (string memory note) {
       uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                if(CompareStrings(AccessControlLists[i].receiverUid, _receiverUid)){
                    return AccessControlLists[i].note;
                }
            }
        }
       return "";
    }

    // Change notes for receiving permission
    // Make sure to check whether the both uid and receiveruid exist, otherwise return false
    function ChangePermissionNote(string calldata _uid, string calldata _receiverUid, string calldata _note) public returns (bool result) {
        uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                if(CompareStrings(AccessControlLists[i].receiverUid, _receiverUid)){
                    AccessControlLists[i].note = _note;
                    return true;
                }
            }
        }
        return false;
    }

    // check for entry if exist
    function isExist(string calldata _uid) public view returns (bool){
        uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                return true;
            }
        }
        return false;
    }

    // Make sure to check whether the uid exist otherwise zero return
    function CountPermissionUid(string calldata _uid) private view returns (uint){
        uint _count = 0;
        uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].uid, _uid)){
                _count++;
            }
        }
        return _count;
    }

    // Make sure to check whether the uid exist otherwise zero return
    function CountPermissionReceivingUid(string calldata _uid) private view returns (uint){
        uint _count = 0;
        uint _aclLength = AccessControlLists.length;
        for(uint i=0; i<_aclLength; i++){
            if(CompareStrings(AccessControlLists[i].receiverUid, _uid)){
                _count++;
            }
        }
        return _count;
    }

    function CompareStrings(string memory a, string memory b) private pure returns (bool) {
        return (keccak256(abi.encodePacked((a))) == keccak256(abi.encodePacked((b))));
    }
}