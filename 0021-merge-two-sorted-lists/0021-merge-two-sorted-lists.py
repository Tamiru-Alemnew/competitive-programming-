 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    result=None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listOne = list1
        listTwo=list2 
        length1 = 1
        length2 = 1 
        current=list1
       
        while current and current.next:
            length1 +=1 
            current = current.next 
        current=list2
        while current and current.next:
            length2 +=1 
            current = current.next 
     
        i =j = 0 
        if list1 == None:
            return list2
        if list2 == None :
             return list1
        while i < length1 and j < length2:
            if listOne.val<listTwo.val:
                self.add_element(listOne.val)
                listOne=listOne.next
                i += 1
            else:
                self.add_element(listTwo.val) 
                listTwo=listTwo.next
                j += 1
        while i < length1:
                self.add_element(listOne.val)
                listOne=listOne.next
                i += 1
        while j < length2:
                self.add_element(listTwo.val)
                listTwo=listTwo.next
                j += 1
        return self.result
    
    def add_element(self, new_data):
        if self.result is None:
            self.result =ListNode(new_data)
        else:
            current_node = self.result
            while current_node.next:
                current_node = current_node.next
            current_node.next = ListNode(new_data)