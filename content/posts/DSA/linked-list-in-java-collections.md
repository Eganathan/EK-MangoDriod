---
title: "Linked List in Java - Collections Framework- DSA"
date: 2022-02-23T13:02:00+05:30
categories: ["DSA", "Java"]
tags: ["java", "dsa", "collections", "linkedlist"]
aliases: ["/2022/02/linked-list-in-java-collections.html"]
ShowToc: true
---
### Gist:

A Linked list is dynamic array where a group of objects can be stored while following the insertion order and allow duplicates, the 2 types of linked list are singly and doubly linked lists, the default one is singly linked list where the elements can be traversed only in forward direction this is because unlike array here the elements are stored at random locations and only the node of each element knows the address of the next element. A simple example would be our circuit board here a point X may be connected to Y and Y connected to point Z here the insertion order is preserved and we can know the next point only by following the signals from the previous point.

Same as the example but in Linked list each element has 2 parts in singly linked list where 1 part is the node with the address to the next node and the other which is the actual data of that element like a post letter the envelope has the address and inside the contents. but in doubly linked list there are 3 parts 2 of them are nodes which has the address of previous and next element and the other one is the actual data of that element.

The insertion or deletion are in constant time so compared to ArrayList the mega shifting process will be avoided.

### Hierarchical order

![](/img/blogger/linked-list-in-java-collections-1.png)

### Type of constructors

- Empty argument constructor or the default constructor is the same as invoking any other object here a new linked list object will be created, do note that there is no scope for reserving memory for the number of elements as we add new element the size is maintained dynamically a new LinkedList is an empty list.
```java
LinkedList list = new LinkedList();
```
- Conversion of other Collections like ArrayList, Vector, etc...to a LinkedList is possible with the following constructor.
```java
LinkedList arraysFromVector = new LinkedList( VariableNameOfTheCollection );
//here any collection will be converted into a LinkedList
```

### Important Points

- By default an empty LinkedList is created.
- Is Dynamically Growable and Shrinkable.
- Heterogeneous Objects are allowed.
- There is no initial capacity
- No load factor is applicable here.
- Order of insertion is preserved
- We can also use generic data-type such that the list acts like a homogenous collection.
- Random access interface is not implemented.
- Ideal if the operations are Insertion or deletion.

### Implementing Interfaces

- Serializable
- Cloneable
- Iterable &lt;E&gt;
- Collection &lt;E&gt;

### Methods available to only the LinkedList object.

- .addFirst(Element) -> adds the element in the front of the LinkedList.
- .addLast(Element) -> add an element in the last part of the LinkedList.
- getFirst() --> returns the Object at the front of the Linked List.
- getLast() --> returns the last object in the linked list.
- removeFirst() -> returns the object in the first and removes it from the linked list
- removeLast() --> returns the last objects and removes the object from the linked list.

| Pros | Cons |
| --- | --- |
| Ideal if insertion or deletion operations are more. | Worst if there are lots of search operations as it needs to iterate through all the other elements. |
| By default the elements can be traversed through forward direction. | Java LinkedList class is non-synchronized. |
| Can hold duplicate elements. | Does not implement random access interface. |
| Can hold null values. | |
| The process of insertion or deletion is simple and fast. | |

---

*Note: This article was originally published on Blogger on February 23, 2022 and imported to MangoDriod.*
