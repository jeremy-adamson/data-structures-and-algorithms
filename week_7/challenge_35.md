# Code Challenge 35

Problem as stated from [leetcode 141](https://leetcode.com/problems/linked-list-cycle/)

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Internally, pos is used to denote the index of the node that tail's next pointer is connected to.

* Example 1:
  * Input: head = [3,2,0,-4], pos = 1
  * Output: true

* Example 2:
  * Input: head = [1,2], pos = 0
  * Output: true

* Example 3:
  * Input: head = [1], pos = -1
  * Output: false
