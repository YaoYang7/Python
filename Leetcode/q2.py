from typing import Optional


'''MEMORY LIMIT EXCEEDED'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        carryOver = 0 # if number exceeds 10 during addition

        while l1 != None or l2 != None: #While neither of these are empty, loop through them 11
            if l1 is not None: 
                num1 = l1.val
            else:
                num1 = 0

            if l2 is not None: 
                num2 = l2.val 
            else:
                num2 = 0
            
            # splitting the numbers into 2 parts
            sum = num1 + num2 + carryOver
            lessThanTen = sum % 10 
            carryOver = sum // 10 

            # going onto the next node
            newNode = ListNode(lessThanTen) 
            tail.next = newNode
            tail = tail.next 

        result = head.next 
        head.next = None
        return result



'''FIXED VERSION'''
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)  # Dummy head node to simplify the list construction
        tail = head  # Tail pointer to track the end of the result list
        carryOver = 0  # To handle cases where sum exceeds 10

        while l1 is not None or l2 is not None:  # Continue while either list is non-empty
            num1 = l1.val if l1 is not None else 0  # If l1 is None, use 0
            num2 = l2.val if l2 is not None else 0  # If l2 is None, use 0
            
            # Add the two numbers along with any carryOver from the previous iteration
            total = num1 + num2 + carryOver
            lessThanTen = total % 10  # Get the current digit (less than 10)
            carryOver = total // 10  # Update the carryOver for the next iteration

            # Create a new node for the current digit
            newNode = ListNode(lessThanTen)
            tail.next = newNode  # Link the new node to the result list
            tail = tail.next  # Move the tail pointer to the new node

            # Move to the next nodes in l1 and l2 if they exist
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # If there's any remaining carryOver, add it as a new node
        if carryOver > 0:
            tail.next = ListNode(carryOver)

        return head.next  # Return the result list, skipping the dummy head node
'''