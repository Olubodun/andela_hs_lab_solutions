// A program which returns the longest string in a sentence
function longest(inStr){
	inStr = inStr.toString();
	inStr = inStr.split(" ");
	var tempLongest = 0;
	var i=0;
	var longest;
	var word;
	for (i;i<inStr.length;i++){
		if (inStr[i].length>tempLongest){
			tempLongest = inStr[i].length;
			longest = inStr[i];
		}
	}	
	return longest;
}