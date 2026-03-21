/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode pre = new ListNode();
        ListNode thala = new ListNode();
        ListNode dum = null;
        ListNode cur = head;
        pre.next = head;
        thala = pre;
        while(cur != null && cur.next != null){
            if(cur.val == cur.next.val){
                dum = cur;
                while(cur != null && dum.val == cur.val){
                    cur = cur.next;
                }
                pre.next = cur;
            }else{
                pre = pre.next;
                cur = cur.next;
            }
        }
        return thala.next;
    }
}