---
title: "Array List - Collections Framework in Java - DSA"
date: 2022-02-11T10:15:00+05:30
categories: ["DSA", "Java"]
tags: ["java", "dsa", "collections", "arraylist"]
aliases: ["/2022/02/array-list-of-collections-in-java-dsa.html"]
ShowToc: true
---
### Gist:

An array list can store individual objects by following insertion order, here the initial capacity is 10 by default but can be modified as per the requirement, once the array list reaches its load factor then internal all the elements of the current array is copied to a new array with the new capacity and the reference variable will now be referring to this new array list and the old array will be dealt by the garbage collector.

### Hierarchical order

![](/img/blogger/array-list-of-collections-in-java-dsa-1.jpg)

### Type of constructors

- Empty argument constructor or the default constructor is the same as invoking any other object here a new ArrayList is created with a default size of 10. Below is the most commonly used constructor by beginners and others alike.
```java
ArrayList array = new ArrayList();
//array has a capacity of 10
```
- The default constructor above will allot only 10 slots but if you want the initial size to be 20 or 1000 you can do so with the following constructor this is ideal when you know the number of entries expected, compared to the default here you will save a lot of performance. since this part is important I will stretch it with an example.

If you are preparing to insert 100 inputs by calling the default constructor, then every time the ArrayList reaches its capacity it will clone itself and grow to a certain capacity and this internal task will take a toll on your performance so instead if you already set the capacity while creating the array list this internal process of growing can be avoided thus saving a lot of performance and time.

```java
ArrayList arrayOfPages = new ArrayList(380);
//array has a capacity of 380
```
- Conversion of other Collections like LinkedList, Vector, etc...to an ArrayList is possible with the following constructor.
```java
ArrayList arraysFromVector = new ArrayList( VariableNameOfTheCollection );
//here any collection will be converted into an ArrayList
```

### Important Points

- Is Dynamically Growable and Shrinkable.
- Heterogeneous Objects are allowed.
- The initial capacity is 10
- Load Factor is 0.75
- Order of insertion is preserved
- We can also use generic data-type such that the array acts like a homogenous.

### Implementing Interfaces

- Serializable
- Cloneable
- RandomAccess
- Iterable &lt;E&gt;
- Collection &lt;E&gt;
- List &lt;E&gt;

### Commonly Used methods from List and the respective base classes.

- .add(element) -> add an element in the last.
- .add(Index, element) -> add an element at the specified index.
- .addAll(Collection x) -> adds all the elements of the collection x
- .addAll(Index , Collection x) -> adds all the elements of the collection x from the specified index.
- .set(index,element) -> change an element at the specified index.
- .get(index) -> Retrieve the element from the requested index.
- .contains(object) -> Retrieves a boolean value if the element is available..
- .indexOf(object) -> Retrieves index value if the element is available or -1.
- .remove(object) -> to remove an element at the requested position.
- .sort() -> Sorts the collection.
- .subList(startIndex, endIndex) -> returns an array list with values from the range of index.
- .trimToSize() -> The capacity of the array will be set to the size of the array to save memory.

| Pros | Cons |
| --- | --- |
| Ideal if a lot of index-based retrieval or update operations will be performed. | If elements need to be **added** or **removed** at an index the entire array elements will be shifted internally. |
| Can be traversed through both directions. | Java ArrayList class is non-synchronized. |
| Can hold duplicate elements. | |
| Can take hold of null. | |
| Once the load factor is met then the capacity will be increased by (current capacity *3/2)+1 | |

---

*Note: This article was originally published on Blogger on February 11, 2022 and imported to MangoDriod.*
