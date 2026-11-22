---
title: "Why Are We Still Writing Backends from Scratch?"
date: 2026-11-22T20:50:00+05:30
categories: ["software-development"]
tags: ["abstraction", "rest-api", "backend", "software-architecture", "graphql", "grpc", "nocoderest"]
description: "Every new project starts with the same exhausting plumbing. What if we mapped the protocol landscape, embraced REST's hierarchical clarity, and built an engine where a million apps are just a prompt away?"
ShowToc: true
cover:
  image: "/img/post-covers/why-backends-from-scratch.webp"
  alt: "Modular interlocking architectural blocks and translucent layers connected by streamlined glowing conduits on a dark background."
---

In my previous post, [Seeing Software Through Abstraction]({{< relref "/posts/software-development/seeing-software-through-abstraction" >}}), I stepped back from frameworks and languages to look at the responsibilities underneath them.

That view left me with a question that I cannot shake: **why are we still writing backends from scratch?**

Every new project—whether a weekend hack, an MVP, or an internal tool—starts with the exact same exhausting ceremony. We set up authentication. We configure tenant containers and user tables. We write CRUD routes, pagination cursors, filter logic, and sync timestamps.

Beneath the frameworks and libraries, every backend executes the exact same lifecycle. A client expresses an intention. The system identifies who is asking, verifies what they may touch, applies product rules, works with stored data, and returns an answer.

Every other layer of our stack has moved toward reuse: package managers for shared libraries, cloud platforms for automated infrastructure, and AI tools for scaffolding client interfaces. Yet when it comes to the core backend foundation, we are still handcrafting the exact same repetitive plumbing from scratch—writing repetitive validation rules, re-authoring database queries, and manually wiring indexes for filtering and sorting, even though relational database tables remain the undisputed best tool for structured data.

Why?

Part of the reason is that we often get distracted by the communication layer—debating whether we should build our APIs in GraphQL, gRPC, or tRPC, rather than asking why we are writing repetitive boilerplate in any of them. As I wrote in [You Can't Google What You Haven't Heard Of]({{< relref "/posts/you-cant-google-what-you-havent-heard-of" >}}), the single most dangerous state in software engineering is not knowing what you don't know. If you don't understand the broader communication landscape and its trade-offs, it is easy to get trapped in a local optimum—either reinventing wheels or choosing tools out of pure habit.

Before we can stop rewriting backends from scratch, we need to map the territory: starting with identity at the gate, comparing how different protocols organize data, and understanding why REST emerges as the most dependable bedrock for a universal abstraction.

---

## The Security Gatekeeper: Authentication and Authorization

Every backend interaction begins with identity and trust. Long before touching a database, the system must answer two distinct questions:

1. **Authentication (AuthN):** *Who is asking?*  
   This establishes identity through verified credentials—whether session cookies, API tokens, or OAuth assertions.
2. **Authorization (AuthZ):** *What are they allowed to do?*  
   This determines access rights. Verifying that someone is a valid user does not mean they may edit another person's notes or delete a shared project.

In many applications, authentication and authorization are treated as afterthought middleware glued onto individual endpoints. When moving fast—or when code is generated through AI tools ("vibe coding")—it is dangerously easy to leave endpoints unprotected or assume a simple sign-in check is sufficient.

In a reusable foundation, identity and access boundaries cannot be an afterthought:

- **Identity establishes context:** Every incoming request resolves to an authenticated caller before reaching business logic.
- **Access scoping precedes execution:** Authorization rules must automatically constrain what records the storage layer retrieves or modifies.

Once identity is verified, how does the client converse with the backend?

---

## The Communication Landscape: Knowing What Exists

Over the decades, the industry has developed several ways for applications to communicate with servers. Each paradigm organizes separation of concerns and data retrieval differently:

### 1. REST (Representational State Transfer)
Introduced by Roy Fielding in 2000, REST organizes systems around **hierarchical resources** identified by clear, predictable URLs:

```text
/org/{org_id}/team/{team_id}/project/{project_id}/todos/{todo_id}
```

- **Separation of Concerns & Data Fetching:** This is what makes REST so enduring. The URL path mirrors the exact mental model of multi-tenancy and database partitioning. When a request asks for `GET /org/1/team/2/project/3/todos`, the backend can immediately chunk out the database lookup using those exact composite keys (`WHERE org_id = 1 AND team_id = 2 AND project_id = 3`). Standard operations (`POST` to create, `GET` to read, `PATCH` to update selected fields, `DELETE` to remove) map cleanly to primary-key lookups and write locks. It is simple, intuitive, and fits the vast majority of real-world use cases.
- **Trade-offs:** Can lead to over-fetching (returning fields a client doesn't need) or under-fetching (requiring separate round-trips to load related resources).

### 2. GraphQL
Created by Meta in 2012, GraphQL replaces multiple resource endpoints with a single endpoint where clients submit structured query trees describing the exact fields they need:

- **Separation of Concerns & Data Fetching:** Separation lives in the GraphQL schema—types, fields, and resolver functions—rather than URL paths. A client can fetch deeply nested graphs in a single round-trip without over-fetching. But that flexibility shifts immense complexity to the server: without careful batching (like `DataLoader`), nested fields trigger the notorious $N+1$ database query problem, scattering data fetching across the database and complicating HTTP caching, rate limiting, and query cost analysis.
- **Trade-offs:** Maximum client flexibility, but high operational and query-planning complexity.

### 3. gRPC and Protocol Buffers
Developed by Google, gRPC uses binary serialization over HTTP/2 to provide high-performance, contract-first Remote Procedure Calls:

- **Separation of Concerns & Data Fetching:** Separation is organized by `.proto` service interfaces (e.g., `ProjectService.GetTodo`). Data fetching is chunked by specific, rigid RPC request payloads containing composite keys. It provides blazing speed, tiny payloads, and bi-directional streaming—making it the gold standard for internal microservices. But you must define a custom RPC method for every unique way you want to fetch data.
- **Trade-offs:** Blazing speed and strict type safety, but poor for direct browser access, non-human-readable over the wire, and difficult to inspect with tools like `curl`.

### 4. WebSockets and Server-Sent Events (SSE)
While request-response protocols wait for the client to ask, real-time collaboration, chat, and live feeds require servers to push updates instantly:

- **Separation of Concerns & Data Fetching:** Separation is organized into pub/sub channels, topics, or rooms (`org.1.team.2.events`). WebSockets and SSE do not "fetch" data using database keys on demand; they stream state deltas as events occur. They are ideal for real-time reactivity and keeping local caches fresh, but terrible for ad-hoc, multi-key database queries.
- **Trade-offs:** Real-time reactivity, but complex stateful connection management and not designed for transactional CRUD.

### 5. Type-safe RPC (tRPC)
Popularized in modern TypeScript stacks, tRPC allows frontends to call backend procedures with compile-time type safety without generating schemas:

- **Separation of Concerns & Data Fetching:** Separation is organized via nested TypeScript router files. It feels like calling a local function, chunking data by procedure input schemas (`zod`).
- **Trade-offs:** Unrivaled developer velocity in full-stack monolithic TypeScript environments, but tightly couples the entire architecture to one language.

---

## Navigating Trade-Offs: Choosing What Matters Long-Term

Looking across this landscape, teams often fall into a familiar trap: analysis paralysis. Engineers endlessly debate whether REST is obsolete, whether GraphQL will solve their data-fetching problems, or whether systems should all be rewritten in gRPC or tRPC.

The antidote to analysis paralysis is recognizing a fundamental engineering truth: **everything in software has a trade-off.** There is no silver bullet, and no protocol is universally superior.

- **GraphQL** grants clients surgical query precision, but demands deep investments in server-side query planning, caching strategies, and $N+1$ mitigation.
- **gRPC** delivers raw binary throughput and rigorous contracts, but requires specialized tooling and sacrifices universal web, mobile, and third-party accessibility.
- **tRPC** offers unparalleled velocity across full-stack TypeScript teams, but binds the architecture to a single language runtime.
- **REST** provides universal ubiquity and straightforward caching, but accepts occasional over-fetching and extra network round-trips.

Avoiding overcomplication does not mean taking the lazy path or settling for what is familiar out of comfort. It means cutting through architectural dogma to evaluate what actually serves your system in the long run across two practical axes:

1. **Engineering Clarity:** Can you easily reason about the system, debug failures in production with basic tools, onboard contributors, and evolve contracts without breaking existing clients?
2. **Customer Value in the Long Run:** Does the protocol deliver predictable latency, resilient error handling, robust security, and reliable uptime to the people using your product?

If your system's core value requires continuous bi-directional coordination, investing in WebSockets is necessary engineering, not overcomplication. If you are coordinating high-volume inter-service RPCs inside a private cluster, gRPC is the right technical investment.

The mistake is choosing complex paradigms where they introduce operational friction without delivering proportional customer value. The goal is to make a deliberate, clear-eyed choice based on your use case, embrace its trade-offs, and focus your energy on building the product.

---

## The Convergence: Why REST Wins as the Reusable Bedrock

For the challenge of building a universal, multi-tenant backend foundation, REST is not a compromise of convenience—it is a deliberate architectural optimization for long-term reliability and maintainability:

1. **Clear Hierarchical Separation:** The path `/org/{org_id}/team/{team_id}/project/{project_id}` isn't just an aesthetic choice; it mirrors multi-tenant access boundaries directly in the URL. It allows engineers and systems to immediately chunk out database lookups using primary and composite keys (`WHERE org_id = ? AND team_id = ? AND project_id = ?`) without writing complex, ad-hoc query planning.
2. **Predictable Performance for Customers:** Standard HTTP semantics ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)) let edge CDNs, reverse proxies, and client caches work automatically. The server retains strict control over query execution costs and indexes, preventing runaway client queries from degrading system stability for other users.
3. **Zero-Friction Client Reach:** Any mobile app, web frontend, CLI script, webhook consumer, or AI coding agent can interact with the contract using native HTTP primitives—no specialized SDKs, runtime dependencies, or client-side query compilers required.
4. **Predictable Operations:** Standard operations (`POST` to create, `GET` to read, `PATCH` to apply delta updates, `DELETE` to remove) map cleanly to database locks and transaction boundaries. Caching, compression, and logging work transparently out of the box.
5. **Portability and Escaping the BaaS Trap:** When developers consider backend reuse, someone inevitably asks: *“Isn’t this what Backend-as-a-Service platforms like Firebase or Zoho Catalyst already do?”*[^1] The critical difference is the contract. Traditional BaaS platforms rarely provide an open, unbundled REST contract; they provide a **proprietary client SDK**. Your mobile apps, web frontends, and scripts become tightly coupled to vendor-specific libraries. If your application grows, bills mount, or you want to benchmark a parallel service on a self-hosted VPS or Cloud Run, you are trapped—migrating requires rewriting client code across every platform. REST completely unshackles the client. The client speaks only standard HTTP and JSON; whether the backend runs on serverless functions, a container, or a basic VPS, you can swap, scale, or benchmark infrastructure without changing a single line of client code.

Knowing what else exists allows us to choose REST not out of habit or resistance to learning, but out of deliberate architectural conviction.

---

## The Architecture of the Abstraction: What Replaces the Scratchpad?

If we stop writing backends from scratch, what actually replaces all that bespoke code?

A person expresses an intention through an interface. The backend identifies the caller, checks their permissions, applies domain rules, and works with stored information. A response travels back to the interface.

![A vertical architecture diagram connecting interfaces, the shared REST contract, identity and access checks, entity rules, and scoped storage.](/img/backend-abstraction/backend-map.svg)
*Conceptual layers of responsibility. A real implementation may combine them within one service.*

The reusable unit begins by separating data meaning from API capabilities:

> Entity definition + supported capabilities + access rules → a predictable API contract.

An entity definition captures:
- Properties, data types, validation limits, and relationships.
- **Supported capabilities:** which fields clients may filter by, sort on, or search through. (An index makes queries fast, but exposure is a deliberate contract decision.)
- **Single-record lifecycle:** standard `POST`, `GET`, `PATCH`, and `DELETE` handling, concurrent update detection via server revisions, and soft-delete/trash recovery.
- **Collection vocabularies:** predictable filter operators (`AND` logic, explicit nulls), search parameters, and continuation pagination using opaque, stateless, tamper-proof cursors.

---

## Enforcing the Boundaries: Project and User Isolation

The most critical responsibility of this foundation is establishing access scope before executing a query.

![A request diagram showing caller verification, server-established project and record scope, a scoped storage operation, and a filtered response.](/img/backend-abstraction/scoped-request.svg)
*The client's filter narrows the records it is already allowed to see.*

When a request asks for `GET /v1/projects/p_123/todos?filter.status=open`, the client's filter only narrows records within their permitted boundary. The server establishes three distinct isolation layers:

- **Project isolation:** an application's records stay strictly within its permitted project container.
- **User isolation:** private records within that project are visible only to the authenticated owner.
- **Explicit sharing:** team access is granted through defined membership rules, never assumed from a shared database.

A `created_by` column or an unguessable record ID does not enforce this by itself. The boundary must apply uniformly to reads, writes, searches, counts, bulk updates, and caches.

### Two Repeated Platform Capabilities

Beyond basic CRUD and isolation, two additional patterns constantly reappear across applications:

1. **User Preferences:** Every application needs a small, bounded store to remember a user's locale, theme, timezone, or default views. A built-in preference endpoint (`/projects/{project_id}/me/preferences`) scoped to the authenticated caller provides this out of the box, cleanly separated from credentials and permissions.
2. **Sync Invalidation Hints:** Instead of pretending to solve the massive complexity of full offline-first delta synchronization, the platform exposes honest change metadata (`last_modified_at` and collection `revision` numbers). Clients compare these hints with local cache state and decide whether to invalidate screens, refetch lists, or stay idle.

---

## Grounding the Abstraction: What Becomes Possible with Persona

When we stop writing backends from scratch, what do we actually build?

For me, the answer is a project I have wanted to build for a long time: **Persona**.

I imagine it holding my preferences, notes, todos, articles, contacts, and things I have explicitly asked it to remember. Rather than scattering these across disconnected apps, I want to connect these pieces and build experiences around them.

A saved article might relate to a note. That note might lead to a todo. A contact might connect to the project where that work belongs. My preferences could shape how these are presented across the interfaces I use.

![A conceptual Persona architecture showing personal information, entity relationships, the shared REST API, approved integrations, and connected experiences.](/img/backend-abstraction/persona-map.svg)
*Persona is a motivating project I want to build. This diagram describes the foundation I imagine for it.*

Each kind of information has its own meaning. A contact is different from a todo, and a saved preference is different from a remembered instruction. Yet all of them need the exact same baseline capabilities: ownership, storage, retrieval, updates, queries, and a way to tell when information has changed.

This is where the abstraction transforms from an intellectual exercise into personal leverage. It provides the integration space Persona needs: a consistent place for its information to live and a predictable contract through which mobile apps, web interfaces, and scripts can interact with it.

Persona is one personal manifestation of what this abstraction unlocks. The exact same foundation could power an indie SaaS product, a specialized AI agent workspace, an internal company tool, or a collaborative team hub. When the foundation is dependable, starting any of these projects stops feeling daunting.

---

## Beyond Boilerplate: The App Factory and the Freedom to Build

This brings us full circle to our opening question: *why are we still writing backends from scratch?*

The truth is, we shouldn't be.

I have built a proof of concept around this idea through [NoCodeREST](https://ncr-10137353709.development.catalystappsail.com/), and it is going through an evolution of its own. It serves as a testing ground for these patterns against real requests, databases, and clients.

There are limits to discover. Updating a generic field is straightforward; sending a message, paying an invoice, or reserving stock involves external effects and business rules. To avoid becoming a rigid walled garden, the platform must provide escape hatches—such as event hooks, transactional validation functions, and webhook dispatchers.

The recurring pattern is what matters:

> Describe the information and its rules → expose a consistent REST contract → connect interfaces and integrations → build the experience.

This unlocks something far bigger than saving a few hours of setup.

We are living in an era where AI coding tools and natural language prompts allow anyone—from seasoned engineers to weekend vibe-coders—to generate full user interfaces and frontend screens in minutes. But generating an interface is only half the battle. If every new idea still requires you to manually wire up database partitions, configure JWT token validation, enforce multi-tenant isolation, and debug pagination cursors, momentum stalls. The backend becomes the bottleneck.

If a team or platform solves these recurring backend responsibilities as **pluggable, reusable components**, the entire equation flips.

Building a hundred or a million apps becomes as effortless as a prompt away. This is the destination NoCodeREST is working toward: lifting the weight of backend plumbing entirely off the creator's shoulders.

Whether you are hacking on a weekend hobby, validating an early-stage MVP, scaling a real production system, or operating an internal "app factory" that spins up custom workflows on demand, the machinery is already there—secure, isolated, and dependable.

You stop fighting boilerplate, and you earn the freedom to focus on what truly matters: the problem you are solving, the people you are serving, and the human experience of what you build.

---

## The Open Question

Building NoCodeREST to test this vision has made one thing clear: standardizing Auth, REST contracts, and tenant isolation works. But it leaves us with one stubborn engineering question.

Relational database tables are notoriously rigid. Predefined columns index and sort effortlessly, but user-defined custom properties are dynamic—and stuffing them into an unindexed text blob ruins query performance. Moving to NoSQL isn't the silver bullet either; it throws away relational integrity and composite isolation.

So how can a reusable platform handle dynamic user properties flexibly without wrecking database indexing and query performance? What real architectural options do we have?

That is the exact puzzle I am tackling next.

If you have wrestled with this in production—whether through JSONB expression indexes, EAV patterns, hybrid storage, or something else entirely—I would love to learn from your experience. **Drop your thoughts, architecture ideas, or battle scars in the discussion below**, or ping me on [X (@eknath_dev)](https://x.com/eknath_dev). Let's figure this out together.

---

[^1]: Special thanks to my friend [Siva G](https://www.linkedin.com/in/itsivag/) for sparking this exact discussion on why not just stick with Firebase, and challenging the assumptions behind backend vendor lock-in.
