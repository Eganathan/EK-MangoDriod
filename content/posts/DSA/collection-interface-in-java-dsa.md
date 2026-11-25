---
title: "Collection Interface - Java Collections Framework - DSA"
date: 2022-02-11T17:59:00+05:30
categories: ["DSA", "Java"]
tags: ["java", "dsa", "collections"]
aliases: ["/2022/02/collection-interface-in-java-dsa.html"]
ShowToc: true
---
Most people consider the collection as the root interface of Collections Framework and it is true to a great extent but another part of Collections Framework is Map Interface, we will see that later, Most Common methods which are applicable to all collections are defined in this interface for example `add()` to add an element, `size()` to get the size and much more, below is a table of most common methods.

#### Hierarchy of the Collection Interface.

![](/img/blogger/collection-interface-in-java-dsa-1.jpg)

The Parent of Collection Interface is **Iterable** Interface and the Collection is the base interface for List Interface, Set Interface and Queue Interface, the respective classes which implement either of the sub interfaces will also implement the defined methods from the Collection Interface, below are some of the commonly used methods.

#### Defined Methods:

| Method | Description |
| --- | --- |
| add() | This method returns a Boolean value true if it inserts the specified element in this collection. |
| addAll() | This method returns a Boolean value true if all elements were added successfully. |
| clear() | Removes all the elements of the collection. |
| contains() | returns a Boolean value if the specified object exists true else false. |
| containsAll() | returns a Boolean value if the specified Objects from the argument of collection and if all the elements exist inside the collection then it returns true else false. |
| equals() | returns true if the specified Object is equal to this current Collection. |
| hashCode() | returns the hash code value of this collection. |
| isEmpty() | returns true if this collection has no elements otherwise returns false. |
| iterator() | returns an Iterator over the elements in proper sequence. |
| remove() | Removes the first element where the specified element is found, but only the 1st element of the specified object will be removed. |
| removeAll() | same like remove() but all objects matching will be removed from this collection. |
| removeIf() | It removes all the elements of this collection that satisfy the given predicate filter. |
| retainAll() | The Objects inside the arguments collection will be kept and all other Objects will be removed from this collection. |
| size() | This returns the number of objects present inside this collection. |
| spliterator() | It returns a spliterator over the elements in this collection. |
| toArray() | It returns an array containing all the elements of this collection which are in proper sequence. |

#### Classes that implements Collection

`ArrayList` , `LinkedList` , `Vector` , `Stack` , `PriorityQueue` , `ArrayDeque` , `TreeSet` , `HashSet` , `LinkedHashSet`

Which means all the above methods in the table can be used from the objects of these classes which implement Collection interface, along with these different collections have their own interfaces they implement depending on the underlying collections.

#### Sample Code:

```java
import java.util.*;

class TestJavaCollection1 {
    public static void main(String args[]) {
        ArrayList<String> list = new ArrayList<String>(); // Creating arraylist
        list.add("Ravi"); // Adding object in arraylist
        list.add("Vijay");
        list.add("Ravi");
        list.add("Ajay");
        // Traversing list through Iterator
        Iterator<String> itr = list.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
    }
}

// output
// Ravi
// Vijay
// Ravi
// Ajay
```

---

*Note: This article was originally published on Blogger on February 11, 2022 and imported to MangoDriod.*
