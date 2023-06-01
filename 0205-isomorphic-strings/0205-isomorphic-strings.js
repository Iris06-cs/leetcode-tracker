/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if(s.length!==t.length) return false
    let letterTracker={}
    for(let i=0;i<s.length;i++){
        let values=Object.values(letterTracker)
        if(!letterTracker[s[i]]&&!values.includes(t[i])) letterTracker[s[i]]=t[i]
        else{
            if(letterTracker[s[i]]!==t[i]) return false
        }
    }
    return true
};