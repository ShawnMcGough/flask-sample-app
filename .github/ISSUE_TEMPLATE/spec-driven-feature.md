---
name: Spec-Driven Feature / Change
about: Create a clear, testable specification that drives implementation
title: "[Feature/Change] Short descriptive title"
labels: ["spec", "triage"]
assignees: ""

---

<!-- 
Spec-Driven Development (SDD) Issue Instructions
------------------------------------------------
Goal: This issue becomes the **living specification** and acceptance criteria.
The spec should be detailed enough that:
• A developer (or AI agent) can implement it correctly
• Tests can be written directly from it
• We can verify completion without mind-reading

Fill sections in order. Delete any you don't need.
Use [NEEDS CLARIFICATION] for anything ambiguous.
-->

## 1. Problem / User Need (Why)

<!--
One paragraph max. Describe the user pain, business goal, or opportunity.
Avoid solution language here — focus on the **problem**.
-->

## 2. Goal / Success Criteria

<!--
What does "done" look like from the user's/business perspective?
Prefer outcome-oriented statements.
Examples:
- User can reset password in < 30 seconds without support
- API returns 95th percentile latency < 200ms under 1000 rps
-->

## 3. Concrete Specification

<!--
This is the heart of SDD — make it precise and testable.

Use Gherkin-style (Given/When/Then), numbered acceptance criteria, API contract examples, UI flows, edge cases, etc.

Feel free to use multiple formats:
- Gherkin scenarios
- API request/response examples
- UI component states
- Data invariants / business rules
-->

**Feature:** [short name]

**Scenario:** [happy path name]
Given [initial context]
When [action]
Then [expected outcome]

**Scenario:** [important edge case]
...

**Acceptance Criteria Checklist**
- [ ] Criterion 1 – very specific and verifiable
- [ ] Criterion 2
- [ ] Handles offline / slow network gracefully
- [ ] Input validation prevents X
- [ ] Security: prevents Y attack vector
- [ ] Performance: does Z within N seconds/ms
- [ ] Accessibility: meets WCAG AA for this feature (if UI)
- [ ] Internationalization: strings are externalized (if applicable)
- [ ] Logging & observability hooks are present

## 4. Out of Scope (explicitly)

<!--
Very important — prevents scope creep.
List things people might assume are included.
-->

## 5. Open Questions / Needs Clarification

<!--
Use this format so it's easy to search later:
[NEEDS CLARIFICATION] What is the exact retry policy for failed payments?
[NEEDS CLARIFICATION] Should we support dark mode v1 or defer to v2?
-->

## 6. Technical Notes / Constraints (optional)

<!--
Only add if already known — otherwise this belongs in a separate PLAN.md or follow-up issue.
Examples: must use existing library X, cannot change database schema yet, target mobile-only, etc.
-->

## 7. Related / Parent Issues

- #123 (parent epic)
- #456 (blocked by)
- #789 (blocks)

---
**Definition of Ready Checklist** (for assignees / implementers)
- [ ] Spec is unambiguous (no open [NEEDS CLARIFICATION] items)
- [ ] Acceptance criteria are testable
- [ ] Out-of-scope is explicit
- [ ] Size feels reasonable (can be split if > ~3-5 days work)