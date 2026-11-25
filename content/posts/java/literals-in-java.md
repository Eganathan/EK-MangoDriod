---
title: "Literals of Base numbers in Java ( Octal , Hexadecimal, Decimal)"
date: 2022-01-29T18:37:00+05:30
categories: ["Java"]
tags: ["java", "literals", "basics"]
aliases: ["/2022/01/literals-in-java.html"]
ShowToc: true
---
### 1. Overview:

A literal key indicates the compiler how to interpret the value of the given data type, for numbers we can calculate the value by using Octal representation or hexadecimal representation but just typing out a hexadecimal value to an int will throw us an error because the compiler has no idea how to handle it but if we assign the java specified prefix for the required bases with some literals then the compiler will not throw us any error as it understands how to interpret the value.

| Base | Literals | Values | Example | Eg. Value |
| --- | --- | --- | --- | --- |
| **Decimal** | none | 0-9 | *int x = 10;* | x is 10 |
| **Octal** | 0 (zero) as the prefix | 0-7 | *int x = 012;* | x is 10 |
| **Hexadecimal** | 0x or (zero) along with an x | 0-9 and a-f or A-F | *int x = 0xA;* | x is 10 |

### 1. Binary or Base(2)

**Allowed Digits** ***0 and 1***  
*int i = 0b1010;* and now the variable i has value 10.

```java
int n = 0b1111101;
// n has the value 125
```

### 2. Decimal or Base(10)

**Allowed Digits** ***0 to 9***  
Decimal does not require any special literals to represent its base as the default base is 10, so the value is taken exactly as the raw value from the code.  
*int i = 10;* and now the variable i has value 10.

```java
int n = 125;
// n has the value 125
```

### 3. Octal or Base(8)

**Allowed Digits :** ***0 to 7***
**Prefix :** 0(zero)
The first doubt that arises seeing the number 0-7 and calling it octal or base 8 confused me and I'm sure there are many out there like me so here there are 8 digits including 0 so it has the name octal or base 8, to represent a number on octal in java a literal 0 (zero) must be prefixed before the octal value.
for example *int i = 0377;* and now the variable I has value 255.

```java
int n = 0377;
// n has the value 255
```

### 4. Hexadecimal or Base(16)

**Allowed Digits :** ***0 to 9 and a-f or A-F***
**Prefix :** ***0x or 0X (zero) along with an x or X***
The hexadecimal numbers can be assigned to any primitives using the literal 0(zero) and an x or X here the case is not important as the compiler takes it either way.
for example *int i = 0xa;* and now the variable i has value 10.

```java
int n = 0xb;
// n has the value 11
```

### Some Important points

- The default base is decimal.
- The 0 is the prefix for both octal and hexadecimal but the hexadecimal needs an x after the 0
here x is case insensitive.
- Hexadecimal characters a-z are case insensitive so a-f or A-F makes no difference to the compiler.

---

*Note: This article was originally published on Blogger on January 29, 2022 and imported to MangoDriod.*
