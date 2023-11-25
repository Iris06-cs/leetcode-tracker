/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var checkAlmostEquivalent = function(word1, word2) {
    
    let wordFreq1=new Map()
    let wordFreq2=new Map()
    
    for(let i=0;i<word1.length;i++){
        // if(wordFreq1.get(word1[i]))wordFreq1.set(word1[i],wordFreq1.get(word1[i])+1)
        // if(wordFreq2.get(word2[i]))wordFreq2.set(word2[i],wordFreq2.get(word1[i])+1)
        // if(!wordFreq1.get(word1[i]))wordFreq1.set(word1[i],1)
        // if(!wordFreq2.get(word2[i]))wordFreq2.set(word2[i],1)
        wordFreq1.set(word1[i],(wordFreq1.get(word1[i])||0)+1)
        wordFreq2.set(word2[i],(wordFreq2.get(word2[i])||0)+1)
    }
    
    // console.log(wordFreq1,wordFreq2)
    let freqs={}
    let wordEntries1=wordFreq1.entries()
    let wordEntries2=wordFreq2.entries()

    for(let entry of wordEntries1){
   
        if(!freqs[entry[0]]) freqs[entry[0]]=entry[1]
    }
    for(let entry of wordEntries2){
    
        if((!freqs[entry[0]]) && freqs[entry[0]]!==0) freqs[entry[0]]=entry[1]
        else freqs[entry[0]]=Math.abs(freqs[entry[0]]-entry[1])
    }
    // console.log(freqs)
    let maxFreq=0
    for(let val of Object.values(freqs)){
        if(val>maxFreq) maxFreq=val
    }

    return  maxFreq<=3
};