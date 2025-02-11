from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

#Quick method to make a linked list for testing
#Input: Array of vals
#Output the head of the linkedlist
def create_linked_list(arr):
   if not arr:
       return None
   head = ListNode(arr[0])
   curr = head
   for i in range(1, len(arr)):
       curr.next = ListNode(arr[i])
       curr = curr.next
   return head

def print_linked_list(head):
   curr = head
   while curr:
       print(curr.val, end=" -> ")
       curr = curr.next
   print("None")


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = l1
        l2curr = l2
        sumNumsList = []
        rollOver = False
        while l1curr or l2curr:
            sumNum = 0
            l1currVal = 0
            l2currVal = 0
            if l1curr:
                l1currVal = l1curr.val
                l1curr = l1curr.next
            else:
                l1curVal = 0
            if l2curr:
                l2currVal = l2curr.val
                l2curr = l2curr.next
            else:
                l2currVal = 0
            
            sumNum = l1currVal + l2currVal
            print(f"sumNum: {sumNum}, rollOver: {rollOver}")

            if rollOver:
                sumNum += 1
                print(f"rolled over sumNum: {sumNum}")

            if sumNum >= 10:
                sumNum -= 10
                print(f"Rollover Check new sumNum: {sumNum}")
                rollOver = True
            else:
                rollOver = False

            sumNumsList.append(sumNum)


        if rollOver:
            sumNumsList.append(1)
        return self.create_linked_list(sumNumsList)
    
    def create_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return head
    
head1LL = create_linked_list([0,1,2,3,4,5,6,7,8,9])
head2LL = create_linked_list([0,1,2,3,4,5,6,7,8,9])
print_linked_list(head1LL)
print_linked_list(head2LL)

solution = Solution()
print_linked_list(solution.addTwoNumbers(head1LL, head2LL))

head1LL = create_linked_list([2,4,9])
head2LL = create_linked_list([5,6,4,9])
print_linked_list(head1LL)
print_linked_list(head2LL)

solution = Solution()
print_linked_list(solution.addTwoNumbers(head1LL, head2LL))