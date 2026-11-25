---
title: "Introduction to Primitives - Java"
date: 2022-01-29T17:17:00+05:30
categories: ["Java"]
tags: ["java", "primitives", "basics"]
aliases: ["/2022/01/introduction-to-primitives-java.html"]
ShowToc: true
---
### Overview:

There are eight primitive data types byte, short, int, long, float, double, boolean, char. These eight data types store values as raw instead of Objects these primitives help to save memory to a great extent and simplify other processes as they are directly stored in the stack.

| Data Type | Size(in bits) | Minimum Range | Maximum Range |
| --- | --- | --- | --- |
| **byte** | 8 | -128 | 127 |
| **short** | 16 | -32768 | 32767 |
| **int** | 32 | -2147483648 | 2147483647 |
| **long** | 64 | -9223372036854775808 | 9223372036854775807 |
| **float** | 32 | -3.4e38 to -1.4e-45 | 1.4e-45 to 3.4e38 |
| **double** | 64 | -1.8e308 to -4.9e-324 | 4.9e-324 to 1.8e308 |
| **boolean** | 1 | - | - |
| **char** | 16 | `\u0000` (0) | 65535 |

### 1. byte

A byte has the capacity of 8 bits or 1 byte and it can store numbers between -2^7 and 2^7 -1 or simply -128 to 127.
This is very useful while dealing with large arrays as they are way better than int or short arrays while considering memory efficiency and if the value is in the said range.
**The default value is 0**

```java
byte number = 125;
byte num;
```

### 2. short

A short is if you want to save memory but byte is too small for your activity and int is too large then the short data type is there for your rescue which has a memory space of 16 bits or 2 bytes which can store the numbers between -2 ^15 and 2^15-1 or simply -32,768 to 32,767.
**The default value is 0.**

```java
short number = 125;
short num;
```

### 3. int

An int is the go-to data type for a number by the programmers as they need not worry about the range for their basic calculation for everyday problem solving, the size is 32 bits or 4 bytes and has a range of -2^31 and 2^31-1 or in simple numbers -2,147,483,648 to 2,147,483,647.
**The default value is 0**

```java
int number = 599999;
int num;
```

### 4. float

A float is a data type that can store decimals but can guarantee the precision only until the decimal place is 6 or less otherwise the value becomes an estimate but the size is the same as int which is 32 bits or 4 bytes but the range is 1.40239846 x 10^-45, and the largest value is 3.40282347 x 10^38.
**The default value is 0.0f**
**float values must end with literal f**

```java
float number = 3.14129f;
float num;
```

### 5. double

A double is also a data type that can store decimals, as the name suggests the size is double of the float, which is 64 bits or 8 bytes and the range is 4.9406564584124654 x 10^-324 to 1.7976931348623157 x 10^308
**The default value is 0.0d**
**double values must end with literal d**

```java
double number = 3.14129d;
double num;
```

### 6. boolean

A boolean can store only 2 values *true* and *false* which are primarily used for the control of the loops or other methods the size is just 1 bit but java stores it as 1 byte.
**The default value is *false***

```java
boolean run = true;
boolean flag;
```

### 7. char

The last data type is char which is a 16-bit integer representing a Unicode-encoded character. Its range is from 0 to 65,535 which in Unicode represents '\u0000' to '\uffff'.
**The default value is *`\u0000` (null character)***

```java
char c = 'H';
char s;
```

### Some Important points

- The default value is applicable only for instance variables or simply variables declared inside the class but outside the constructor.
- String: Even though the string is declared and acts like a primitive in java it is basically a class every time we create a string an object is created with a sequence of characters in a char array.
- Using underscore between two numbers are legal in java example *int k = 59_6565_231;* just not the beginning or end of the numbers and in case of decimals not next to them either..

---

*Note: This article was originally published on Blogger on January 29, 2022 and imported to MangoDriod.*
