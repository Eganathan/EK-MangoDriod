---
title: "Introduction to Threads in Java"
date: 2022-02-12T12:26:00+05:30
categories: ["Java"]
tags: ["java", "threads", "concurrency"]
aliases: ["/2022/02/introduction-to-threads-in-java.html"]
ShowToc: true
---
Threads are basically a way to run multiple tasks concurrently this can be helpful to speed up your program, usually, a Java program runs on a single thread by utilizing only one core of your processor here the other processors are just sitting idly by introducing thread java helps us to make use of these idle processors.

**How to create a new thread process?**

There are two ways of creating a new thread is by extending the Thread class and another way is by implementing Runnable interface either way the class must override the run method which will be called during the start method of the thread object.

***1. extending the Thread class***

```java
public class Main extends Thread {
  public void run() {
    System.out.println("This code is running in a thread");
  }
}
```

***2. Implementing Runnable Interface***

```java
public class Main implements Runnable {
  public void run() {
    System.out.println("This code is running in a thread");
  }
}
```

The ideal way would be by implementing the Runnable interface because this enables us to extend other required base classes if required, here the method run() will be called after the thread is started, here you may call the methods which you want to sublet or do any required process inside it, please note the run() returns nothing.

**Creating a thread Object.**

Creation of Thread object is same as creating any other object, *Thread &lt;name&gt; = new Thread(&lt;Object&gt;)* here a thread object will be created, now we can access the methods of the Thread class.

```java
public class Main extends Thread {
  public static void main(String[] args) {
    Main thread = new Main();
  }

  public void run() {
    System.out.println("This code is running in a thread");
  }
}
```

### How to start the thread ?

The thread can be started by calling the start method which is available in the thread class, for example *ThreadName.start()* here when the start method is called the process will start and eventually it will automatically call the run method and the thread will become active and start processing the methods inside the run method.

```java
public class Main extends Thread {
  public static void main(String[] args) {
    Main thread = new Main();
    thread.start();
    System.out.println("This code is outside of the thread");
  }
  public void run() {
    System.out.println("This code is running in a thread");
  }
}
```

#### LifeCycle of Thread

A thread exists only in any one of these states at a time, lets look at them one by one.
- **New** as the name specifies this is a new state where the thread object is created, but none of the code inside it has started to execute yet.
- **Runnable** At this point the code inside this block is ready to run at any instant, once the thread scheduler flags green the code inside it will start to run one by one until there is any interruption.
- Blocked
- Waiting
- Timed Waiting
- Terminated

---

*Note: This article was originally published on Blogger on February 12, 2022 and imported to MangoDriod.*
