# Google SRE Book: Chapter Discussion Questions

Use these questions for team book club sessions. Each section covers a group of related chapters. Allow 45-60 minutes per discussion session.

**Facilitation tips:**
- Rotate the discussion leader each session
- Start with a 2-minute round where everyone shares their top takeaway
- Focus on "how does this apply to us?" over theoretical debate
- Capture action items and revisit them next session

---

## Session 1: Introduction and Principles (Chapters 1-3)

*Chapters: Introduction, The Production Environment at Google, Embracing Risk*

1. The book defines SRE as "what happens when you ask a software engineer to design an operations function." How does this differ from how operations works in your organization today? What would change if you adopted this literally?

2. Google explicitly targets less than 100% availability. What would happen in your organization if you proposed that a service should be allowed to fail 0.1% of the time? Who would resist, and why?

3. Chapter 3 introduces the idea that reliability is a feature you can have "too much" of. What service in your environment is arguably over-reliable relative to user needs? What would you do with the freed engineering time?

4. How does your team currently decide between shipping features and working on reliability? Is that decision explicit or implicit? Who makes it?

5. The book argues that SREs should spend no more than 50% of their time on operational work. Estimate your team's current ratio. What specific work would you reclassify or eliminate to move toward 50/50?

---

## Session 2: SLOs and Error Budgets (Chapters 4-5)

*Chapters: Service Level Objectives, Eliminating Toil*

1. Pick a service your team owns. What SLI would you choose, and what target would you set? Walk through how you would measure it. Where does your current instrumentation fall short?

2. Error budgets create a shared incentive between product and reliability teams. Describe a recent conflict between "ship fast" and "keep it stable" in your organization. How would an error budget have changed the conversation?

3. The book defines toil as work that is manual, repetitive, automatable, tactical, without lasting value, and scales linearly with service growth. List three tasks your team does that meet this definition. Which would you automate first, and why?

4. What is the difference between a meaningful SLO and a vanity metric dressed up as an SLO? How would you tell the difference in your own service?

5. If your service has burned through its error budget for the quarter, what concrete actions should your team take? Draft a policy for your team.

---

## Session 3: Monitoring and Alerting (Chapters 6-10)

*Chapters: Monitoring Distributed Systems, The Evolution of Automation at Google, Release Engineering, Simplicity, Practical Alerting*

1. The book states that monitoring should answer "what's broken" and "why." Look at your current alerts: what percentage tell you something is broken versus telling you why? How would you improve the ratio?

2. Chapter 6 introduces the "four golden signals" (latency, traffic, errors, saturation). Which of these does your team measure well, and which has gaps? What is the cost of those gaps?

3. The chapter on simplicity argues that SRE has an incentive to keep systems simple. In practice, what forces drive complexity in your environment? How could SRE practices push back against unnecessary complexity?

4. Think about the last false-positive alert your team received. What made it false? How would you redesign that alert using the principles in Chapter 10?

5. The book describes a progression from manual operations to autonomous systems. Where on that spectrum are your most critical operational procedures? What is the next step on that ladder?

---

## Session 4: Incident Response and Postmortems (Chapters 12-15)

*Chapters: Effective Troubleshooting, Emergency Response, Managing Incidents, Postmortem Culture*

1. Chapter 12 presents a systematic troubleshooting approach. Recall your team's last major incident: did troubleshooting follow a systematic process, or was it more ad-hoc? What would have been different with the structured approach?

2. The book emphasizes defined incident roles (Incident Commander, Operations Lead, Communications Lead). Does your team use defined roles? What happens when roles are ambiguous during a real incident?

3. Google's postmortem culture is explicitly blameless. Describe what "blameless" means in practice. Is there a scenario where naming an individual's action is appropriate in a postmortem? How do you draw that line?

4. The book states that postmortems without follow-through are worse than no postmortems at all. What is your team's track record on completing postmortem action items? What systemic changes would improve completion rates?

5. Design a lightweight incident response protocol your team could adopt next week. What is the minimum viable process that would improve over your current state?

---

## Session 5: Automation and Release Engineering (Chapters 7-8, 16-18)

*Chapters: The Evolution of Automation at Google, Release Engineering, Handling Overload, Software Engineering in SRE, Load Balancing*

1. Chapter 7 describes an automation hierarchy from manual to autonomous. Pick one operational task your team does manually: what would each level of automation look like for that task? Where should you stop and why?

2. Release engineering at Google involves hermetic builds, reproducibility, and clear ownership. How does your release process compare? What is the biggest risk in your current release pipeline?

3. The chapters on overload handling describe strategies like load shedding, graceful degradation, and client-side throttling. Which of these does your system implement? Which is most needed but missing?

4. The book argues that SREs should write software to solve reliability problems, not just scripts and glue. What reliability problem in your environment would benefit from a proper software solution rather than another script?

5. How do you balance the cost of building automation (engineering time) against the cost of continuing to do the work manually (toil)? What framework does your team use to make that decision?

---

## Session 6: Capacity and Overload (Chapters 19-22)

*Chapters: Load Balancing at the Frontend, Handling Overload, Addressing Cascading Failures, Managing Critical State*

1. Chapter 21 describes cascading failure patterns. Have you experienced a cascading failure? Walk through the sequence of events. Which of the mitigation strategies in this chapter would have helped?

2. The book discusses the challenge of managing critical state (configuration, metadata, coordination). What is the most critical piece of state in your system? What happens if it becomes unavailable or corrupted?

3. Load shedding means deliberately dropping requests to protect the system. How would your product team react to this concept? How would you frame it to get buy-in?

4. The book presents specific techniques for preventing cascading failures (health checks, circuit breakers, deadline propagation). Which of these are implemented in your services? Which would provide the most value if added?

---

## Session 7: Organizational Design (Chapters 27-34)

*Chapters: Reliable Product Launches, Accelerating SREs to On-Call, Communication/Collaboration, On-Call, Team Size, Dealing with Interrupts, Operational Overload, Lessons from Other Industries*

1. Chapter 28 describes ramping new SREs to on-call readiness. How does your team onboard new on-call engineers? What would a structured "wheel of misfortune" training look like for your services?

2. The book draws lessons from industries like aviation and healthcare. What reliability practice from another industry would you borrow for your team? What makes it transferable (or not)?

3. The chapter on interrupts distinguishes between "pages" (urgent), "tickets" (important, not urgent), and "ongoing operational responsibilities." How does your team manage the boundary between these categories? Does interrupt-driven work crowd out project work?

4. The book suggests that a team in operational overload should stop taking on new services. How would your organization react to an SRE team saying "no" to a new service engagement? What criteria should gate that decision?

5. Chapter 33 discusses on-call compensation, workload limits, and sustainability. Is your on-call rotation sustainable for the next two years at current growth rates? What changes would be needed?
