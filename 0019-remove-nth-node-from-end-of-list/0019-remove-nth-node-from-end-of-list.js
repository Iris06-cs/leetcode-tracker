/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let current=head
    let counter=0
    if(!current) return null
    
    while(current){
        counter+=1
        current=current.next
    }
    
    if(counter==1&&n==1 ||counter==n) return head.next
    
    let removePos=counter-n
    let temp=head
    let nextNode=temp.next
    while(removePos>1){
        temp=temp.next
        removePos-=1
    }
    if(temp.next){
        temp.next=temp.next.next
    }
   else{
       temp.next=null
   }
    return head
};