## Question
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

## Solution
The function starts by assuming that box 0 is unlocked and creating two\
sets, one to keep track of the unlocked boxes and one to keep track of \
the keys we have. The function then enters a while loop that runs as long \
as there are keys in the keys set. In each iteration, it pops a key from \
the keys set and checks if the corresponding box is unlocked. If it's not, 
it adds the box to the unlocked set and adds all the keys from that box to 
the keys set. Once the loop is finished, it checks if the number of unlocked 
boxes is equal to the total number of boxes. 
If it is, it returns true, indicating that all boxes can be opened. If not, it returns false.
