---
title: "Seeing Software Through Abstraction"
date: 2026-11-15T12:00:00+05:30
draft: true
categories: ["software-development"]
tags: ["abstraction", "learning", "software-architecture", "experiments"]
description: "A reflection on zooming out from technologies to responsibilities, and bringing our own experience and care to what we build."
ShowToc: false
cover:
  image: "/img/abstraction/helicopter-view.webp"
  alt: "An abstract aerial landscape of layered forms and connecting paths, revealing a simpler pattern from above."
  caption: "Stepping back until the connections become visible."
---

Some time ago, I wrote about [abstraction in software development]({{< relref "/posts/software-development/abstractions-and-its-responsibility" >}}). My focus then was on trust: someone handles a piece of complexity so that we can work at a higher level, without having to understand every detail every time.

Lately, that idea has been changing how I look at software itself.

When I step back from individual frameworks, programming languages, and product names, I start seeing recurring pieces. Things that once felt like a vast collection of unrelated technologies begin to look like a smaller set of responsibilities.

That helicopter view is beautiful to me. It makes the landscape feel approachable enough to explore.

## The Same Responsibilities Keep Appearing

Consider a typical piece of software. Someone is trying to achieve something, and the software exists to help them do it.

From their side, the expectations are familiar. Their information should be safe. The software should be available when they need it, respond quickly, and give accurate results. They should be able to create, read, change, or delete what they are allowed to access.

The framework behind it rarely matters to them. What matters is whether they can trust it to do its job.

Starting there, the technical names begin finding their places:

- **Authentication and authorization:** who is asking, and what are they allowed to do?
- **Communication:** how do we express a request and understand the response? REST APIs, GraphQL, and other approaches give that exchange a structure.
- **Databases and file storage:** where does information live so we can retrieve, change, or remove it later?
- **Backend or server:** what coordinates the work, applies the product's rules, and brings these capabilities together?

Around and through them run other responsibilities: validation, encryption, backups, monitoring, cleanup, and protection against misuse. Keeping one customer's data separate from another's reaches across the whole operation.

The boundaries overlap, but the picture is becoming clearer. What felt like a collection of technologies starts looking like a set of responsibilities serving someone's goal.

## The Same Shape, Somewhere Else

Now consider an application that works entirely offline.

There may be no remote server, no REST API, and no application account. Yet the application still receives an instruction, checks it, applies rules, works with information, and presents a result. It still needs to handle failures and protect what someone has entrusted to it.

The exchange may happen between components inside the application. Storage may be a local file or database. Coordination happens on the device. Some protection comes from the operating system rather than a sign-in system we build ourselves.

The responsibilities feel familiar, even though they have moved.

Place a mobile app, a website, a desktop application, and a command-line tool beside each other. Their interfaces differ, but each can be a way to express an intention: save this note, show my transactions, send this message.

Follow that intention inward, and familiar questions appear. Is this allowed? What rules apply? What information needs to change? How do we return the result?

Zoom out again, and a shape emerges:

> A person's goal → an instruction → rules and permissions → work on information → a result.

That is the view I find beautiful.

We started with technologies. We looked beneath their names and found responsibilities. Then we stepped back and saw those responsibilities working together around a person's intention.

![Abstract ribbons of different textures coming together through translucent layers into one connected composition.](/img/abstraction/experience-and-layers.webp)
*Different paths, familiar responsibilities.*

## A View From Above

There is enormous depth beneath each part of this picture. Protecting a file on one person's device and processing untrusted uploads on a shared server can involve very different consequences. A failure can hurt an individual; in a shared system, it can reach an organization and its customers.

Recognizing the resemblance gives me a place to begin understanding those differences.

For now, I want to pause at this altitude. I don't have to understand every detail to appreciate the connections. I can see where a database belongs, why an API exists, and how a server's work relates to something happening on my phone.

Abstraction is giving me a map. I can choose a place to look more closely without losing sight of what surrounds it.

## What Could We Assemble From Here?

Seeing these recurring responsibilities makes me wonder how much of a software foundation we could configure, reuse, and assemble.

Could we choose the capabilities a product needs, connect them through clear contracts, and spend more effort on the goals particular to that product?

That curiosity is behind my [NoCodeREST experiment](https://ncr-10137353709.development.catalystappsail.com/). Its first phase explores a small part of this possibility. The larger ambition is a unified platform that could help put together the foundation of a typical application in a couple of minutes.

I still need to discover what “typical” means, which responsibilities the platform could take on, and what work would remain. Existing tools and other people's experience have plenty to teach me.

Perhaps some of this looks simple because of how little I know. I would like to explore it anyway. Learning what sits beneath the picture—and letting that change the picture—is part of the appeal.

## What We Bring to the Picture

With AI tools making it easier to move from an idea to an implementation, I worry that we sometimes hurry past this opportunity to understand. We can keep producing things while forgetting to notice what we are learning, or what we already know from experience.

I might love the navigation on one website, the theme selection on another, or a small interaction that makes an action feel reassuring. I remember the frustration of losing a form after a failed request, and the relief of being able to undo a mistake.

Those moments accumulate. Their particular combination becomes part of how I imagine software could work. Each of us carries a different collection.

I don't feel that an AI tool automatically sees all those layers of my experience. Even when I describe what I want, there are memories, preferences, and reasons I may not yet know how to put into words. I still need to pay attention and decide what matters.

Understanding the foundations helps me bring that experience into the work. If I want someone's writing to survive a lost connection, I can ask where it is stored and what happens when a request fails. If deleting something should feel safe, I can think about permissions, recovery, and what “deleted” actually promises.

A small interaction on the screen reaches down into the architecture.

That connection is another reason I want to understand these layers. The helicopter view helps me see how the pieces fit. What I have lived, noticed, enjoyed, and struggled with helps me decide what to do with them.

I don't yet know where the platform experiment will lead. But I want to carry this understanding into the next thing I build: software that fits real situations, with thoughtful architecture underneath and empathy in the decisions that shape it.

For now, the learning—and the view—is enough reason to explore.
