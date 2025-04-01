#21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         new_listnode = ListNode()
#         current = new_listnode
#
#         while list1 and list2:
#             if list1.val >= list2.val:
#                 current.next = ListNode(list2.val)
#                 list2 = list2.next
#             else:
#                 current.next = ListNode(list1.val)
#                 list1 = list1.next
#             current = current.next
#
#         if list1:
#             current.next = list1
#         else:
#             current.next = list2
#
#         return new_listnode.next


######35 Search Insert Position
####my solution
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         try:
#             return nums.index(target)
#
#         except:
#             nums.append(target)
#             print(nums)
#             nums.sort()
#             return nums.index(target)

######chatgpt solution
# nums = [1,3,5,6]
# target = 5
#
# left, right = 0, len(nums)-1
# while left <= right:
#     mid = (left+right)//2
#
#     if nums[mid] == target:
#         print(mid)
#
#     elif nums[mid] > target:
#         right-=1
#
#     else:
#         left+=1


