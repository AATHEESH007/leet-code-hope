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
    public ListNode removeElements(ListNode head, int val) {
        ListNode nn = head;
        ListNode np = head;

        if (head == null){
            return head;
        }
        if (head.val == val){
            while( head !=  null && head.val == val){
                head = head.next;
            }
        }
        while(nn != null){
            if (nn.val == val){
                nn = nn.next;
                np.next = nn;
            }else{
            np = nn;
            nn = nn.next;
            }
        }
        return head;
    }
}