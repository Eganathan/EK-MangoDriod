---
title: "Naming Conventions in Java"
date: 2022-01-29T16:47:00+05:30
categories: ["Java"]
tags: ["java", "naming-conventions", "basics"]
aliases: ["/2022/01/naming-conventions-in-java.html"]
ShowToc: true
---
As the movies are rated G, PG, U, A depending on the age restriction and by just gazing through the rating our parents decide the movie to watch together, or a book with different labels to keep track of the sections and just by seeing them we know what they represent, the same labeling method has been introduced by the Java team to differentiate variables, methods, classes, constants etc.. and we will be going through them all here.

| Type | Naming Convention | Example |
| --- | --- | --- |
| Variables | Must start with a lower case and every other word capitalized | *int counter;* |
| Constants | Must all be upper case and _ for differentiating every other word | *final int MAX_HEALTH = 100;* |
| Methods | Must start with a lower case and every other word capitalized. can be distinguished from the variable by the () next to the method name | *void printNum(){..}* |
| Class | Must start an upper case letter and every other word must be capitalized | *class HelloWorld{..}* |
| Interface | Must start an upper case letter and every other word must be capitalized | *interface ActionListener{..}* |

### 1. Packages

A package must all be in lowercase letters example *java.awt* and as it represents a group of classes and interfaces in case another developer wants to import your package this naming convention will be helpful for him to proceed further without worrying about the case in the name for example *java.awt* is easier to recall than *jAvA.AwT* so it avoids unnecessary confusion.

**here is an example**

```java
package myown.io;
import java.io.*;
```

### 2. Constants

A constant variable must be completely upper case and to differentiate the words we can use underscores(_), there are some pre-built constants such as MAX_VALUE , MIN_VALUE in the Number's subclasses etc..

**here is an example**

```java
final int WORKING_HOURS = 6;
```

### 3. Variables

A variable is a reference of an object or a value of any datatype and the name must start with lowercase and every other word must be capitalized and this method is called camel casing for example *int ageOfPet = 1;* or if its only one word then *int age = 10;* so anytime you see this naming convention then assume its a variable except with an exception that we will see in the methods.

**here is an example**

```java
int age = 6;
age = 12;
System.out.println(age);
```

### 4. Methods

The naming convention is the same as the variable, must start with the lowercase and every other word must be capitalized or in other words must be a camel case word but I know you are asking in your mind "*if both methods and variables have the same naming convention whats the whole point?"* Well, the thing is methods always have brackets next to them example *sum(5+5)* or *public static void main(String[] args)* so as you can see even though they have the same naming convention they both can be easily differentiated.

**here is an example**

```java
void printNum(int a)
{
    System.out.println(a);
}
```

### 5. Class

A class must start with a capital letter and every other word capitalized for example *class HelloWorld {}* or *class Hello{}* so just capitalize all the words, the same naming convention for the abstract classes as well.

**here is an example**

```java
class HelloWorld
{
    ....
}
```

### 6. Interface

An Interface must be named same as the classes naming convention, The first letter must be capitalized and all other words must be capitalized as well for example *interface ActionListener{}*

**here is an example**

```java
interface ActionListener
{
    ....
}
```

### Other Important Note

- Symbols such as $ or _ etc can be used if you want but everything must start with an alphabet
- Not following the naming convention will not throw compile time error.

---

*Note: This article was originally published on Blogger on January 29, 2022 and imported to MangoDriod.*
