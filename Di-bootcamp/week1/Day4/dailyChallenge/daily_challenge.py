# Step 1: Create the Pagination Class

#     Define a class called Pagination to represent paginated content.
#     It should optionally accept a list of items 
#      and a page size when initialized.
# Step 2: Implement the __init__ Method
#     Accept two optional parameters:
#     items (default None): a list of items
#     page_size (default 10): number of items per page
class Pagination():
    def __init__(self,items=None,page_size=10):
        if items is None:
            self.items=[]
        else:
            self.items=items
#     Behavior:
#     If items is None, initialize it as an empty list.
#     Save page_size and set current_idx (current page index) to 0.
#     Calculate total number of pages using math.ceil.
        self.page_size=page_size
        self.current_idx=0
        import math
        self.total_pages=math.ceil(len(self.items)/self.page_size)
# Step 3: Implement get_visible_items Method
# This method should return the items on the current page.
    def get_visible_items(self):
        start_index=self.current_idx*self.page_size
        end_index=start_index+self.page_size
        return self.items[start_index:end_index]
    
# Step 4: Implement Navigation Methods
    def go_to_page(self,page_num):

# These methods should help navigate through pages:

#     go_to_page(page_num)
#     → Goes to the specified page number (1-based indexing).
#     → If page_num is out of range, raise a ValueError.
        if page_num<1 or page_num>self.total_pages:
            raise ValueError("Page number out of range")
        self.current_idx=page_num-1
        return self

#     first_page()
#     → Navigates to the first page.
    def first_page(self):
        self.current_idx=0
        return self

#     last_page()
#     → Navigates to the last page.
    def last_page(self):
        self.current_idx=self.total_pages-1
        return self

#     next_page()
#     → Moves one page forward (if not already on the last page).
    def next_page(self):
        if self.current_idx<self.total_pages-1:
            self.current_idx+=1
        return self

#     previous_page()

#     → Moves one page backward (if not already on the first page).
    def previous_page(self):
        if self.current_idx>0:
            self.current_idx-=1
        return self

# 📝 Note:

#     Pages are indexed internally from 0, but user input is expected to start at 1.
#     All navigation methods (except go_to_page) should return self to allow method chaining.


# Bonus
# Step 5: Add a Custom __str__() Method**

#     This magic method should return a string displaying 
# the items on the current page, each on a new line.

# Example:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
# # Output:
# # a
# # b
# # c
# # d


# Step 6: Test Your Code

# Use the following test cases:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# # ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# # ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# # Output: ValueError

p.go_to_page(0)
# # Raises ValueError
