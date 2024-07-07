# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

##SOLUTION##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        temp1 = l2
        prev_node = None
        new_node = None
        num1 = ""
        num2 = ""
        while temp.val != None:
            num1 = num1 + str(temp.val)
            temp = temp.next
            if temp is None:
                num1  = int(num1[::-1])
                break

        while temp1.val != None:
            num2 = num2 + str(temp1.val)
            temp1 = temp1.next
            if temp1 is None:
                num2  = int(num2[::-1])
                break
           
        sum = num1 + num2

        for letter in str(sum):
            if new_node is None :
                new_node = ListNode(letter)
                prev_node = new_node
            else:
                new_node = ListNode(letter)
                new_node.next = prev_node
                prev_node = new_node
        return new_node