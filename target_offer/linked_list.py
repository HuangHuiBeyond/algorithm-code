## 用类来模拟链表
class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return True if not self.head else False
    
    def add_item_from_arr(self, arr):
        self.clear()
        dummy = listNode(None)
        pointer = dummy
        for i in arr:
            pointer.next = listNode(i)
            pointer = pointer.next
        self.head = dummy.next
        return self.head
      
    def append(self, value):
        if not self.head:
            self.head = listNode(value)
            return self.head
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = listNode(value)
        return self.head
    
    def get_length(self):
        if not self.head:
            return 0
        count = 0
        pointer = self.head
        while pointer != None:
            count += 1
            pointer = pointer.next
        return count

    def search_item_by_value(self, item_value):
        if self.is_empty():
            return False
        node = self.head
        while node is not None:
            if node.val == item_value:
                return True
            node = node.next
        return False


    def remove_list_item_by_id(self, item_id):
        if item_id < 0 or item_id > self.get_length():
            raise Exception('wrong item_id')
        cur_node = self.head
        cur_id = 1
        pre_node = None ## 要用pre_node来保存前一个节点信息
        while cur_node is not None:
            if cur_id == item_id: 
                if pre_node is not None:
                    pre_node.next = cur_node.next
                    return
                else:
                    self.head = cur_node.next
                    return
            pre_node = cur_node
            cur_node = cur_node.next
            cur_id += 1

    
    def remove_list_item_by_value(self, item_value):
        if not self.search_item_by_value(item_value):
            raise Exception("cat't found this item_value!")
        

        cur_node = self.head
        pre_node = None
        
        while cur_node is not None:
            if cur_node.val == item_value:
                if pre_node is not None:
                    pre_node.next = cur_node.next
                else:
                    self.head = cur_node.next
                return
            pre_node = cur_node
            cur_node = cur_node.next

    
    def update_list_item_value(self, old_value, new_value):
        if not self.search_item_by_value(old_value):  ## 在代码易懂的同时增大了时间复杂度
            raise Exception("can't found this old_value")
        
        node = self.head
        while node is not None:
            if node.val == old_value:
                node.val = new_value
            node = node.next
    
    def add_item_to_sorted_linked_list(self, item_value):
        cur_node = self.head
        pre_node = None
        while cur_node is not None:
            if cur_node.val > item_value:  ## 找到第一个比要插入节点大的值
                break
            pre_node = cur_node
            cur_node = cur_node.next
        temp = listNode(item_value)
        if pre_node is not None:
            
            pre_node.next = temp
            temp.next = cur_node
        else:
            temp.next = cur_node
            self.head = temp

    
    def arr_to_sorted_linked_list(self, arr):
        self.clear()
        for i in arr:
            self.add_item_to_sorted_linked_list(i)
        


    def pop(self):
        if self.is_empty():
            raise Exception("can't pop from empty list")
        cur_node = self.head
        pre_node = None
        while cur_node.next is not None:
            pre_node = cur_node 
            cur_node = cur_node.next
        pre_node.next = None
        return cur_node.val
        

        
    
    def clear(self):
        self.head = None




# ## test
# sll = SingleLinkedList()
# print(sll.is_empty())
# sll.add_item_from_arr([1, 2, 3])
# print(sll.is_empty())
# print(sll.get_length())
# sll.append(4)
# sll.append(6)
# print(sll.search_item_by_value(4))
# print(sll.search_item_by_value(8))
# sll.remove_list_item_by_id(5)
# sll.remove_list_item_by_value(4)
# sll.remove_list_item_by_value(2)
# sll.update_list_item_value(3, 2)
# sll.update_list_item_value(2, 3)
# sll.add_item_to_sorted_linked_list(2)
# sll.add_item_to_sorted_linked_list(0)
# sll.arr_to_sorted_linked_list([4, 1, 3, 2, 5])
# print(sll.pop())

# ## 小知识：对象之间的赋值是引用赋值
# a = listNode(3)
# print(a)
# b = listNode(4)
# print(b)
# a = b
# print(a)
# print(b)








# sll.update_list_item_value(6, 5)
# sll.remove_list_item_by_value(7)
# sll.remove_list_item_by_id(8)

# print(sll.get_length())
# sll.remove_list_item_by_id(3)
# sll.remove_list_item_by_value(4)
# sll.remove_list_item_by_value(1)
# sll.remove_list_item_by_id(1)
# sll.remove_list_item_by_id(1)


pass