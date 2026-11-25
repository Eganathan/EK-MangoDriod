---
title: "Chocolate Feast - Problem Solving - Hacker Rank Solution."
date: 2022-02-20T00:04:00+05:30
categories: ["DSA", "Java"]
tags: ["java", "dsa", "hackerrank", "problem-solving"]
aliases: ["/2022/02/chocolate-feast-problem-solving-hacker.html"]
ShowToc: true
---
The expectation is to find the total number of chocolate one can consume by taking full advantage of the offer, Here there are 3 inputs `n` which holds the value of initial amount of money for buying chocolate, `c` is the cost price of each candy if paid by cash and `m` is the exchange rate for the candy.

#### Inputs

- **n** Initial cash to buy candy.
- **c** Cost of each candy if paid by cash.
- **m** Exchange rate for a new candy in offer.

The initial count of chocolate will be the cash / cost and the wrappers in hand will be the same value of chocolate, and from there we loop through until the wrap count is less than the exchange rate, inside the loop the chocolate count will still hold the same formula as before but divided with exchange rate. The wrap count is the tricky part... the wrap will be wrap / exchange rate (the no. of chocolates) + the remainder of this division (THIS IS VERY IMPORTANT) because for example if the count of wrapper is 3 and the exchange rate is 2 you can only buy 1 chocolate but the remainder 1 needs to be included or it will pop errors in the test cases.

### Algorithm

- declare 2 new variables chocolate and wrappers.
- Initialize the chocolate to `n / c`.
- Initialize the wrapper to chocolate.
- Run a while loop while the wrapper >= exchange rate (or `m`)
- Add the value of chocolate to `wrapper / exchange rate` (or `m`)
- Set the value of wrapper to the number of chocolates exchanged and the balance un-used wrapper.
- return the count of chocolates consumed.

**I Highly recommend you dont go through the below code now but try to solve it on your own to get the ability to solve problems, but im just pasting it here for those who haven't managed to find the solution despite many tries**

```java
public static int chocolateFeast(int n, int c, int m) {
    int cho = n / c, wrap = cho;

    while (wrap >= m) {
        cho += wrap / m;
        wrap = wrap / m + wrap % m;
    }

    return cho;
}
```

---

*Note: This article was originally published on Blogger on February 20, 2022 and imported to MangoDriod.*
