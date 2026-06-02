# Intent

## Purpose

This skill helps an agent evaluate whether a user idea, MVP, product concept, or startup concept is worth pursuing.

The skill should behave like a structured decision engine:

- gather opposing viewpoints,
- pressure-test the idea,
- judge market potential,
- and give the user a clear recommendation.

## What It Should Do

When the user presents an idea, the skill should:

- research and reason through the idea from multiple angles,
- split the analysis into pro, con, and neutral positions,
- use subagents to avoid one-sided thinking,
- identify market signals, risks, and opportunity size,
- and produce a final score plus a decision summary.

## Core Question

The skill exists to answer:

- Is this a good idea?
- Is there a market for it?
- What are the strongest reasons to build it?
- What are the strongest reasons not to build it?
- Is it worth planning an MVP?

## Operating Model

The evaluation must happen in 3 stages.

### Stage 1: Broad Scan

Launch 5 subagents.

Assign them different roles so the idea is explored from multiple directions.

Required split:

- 2 subagents against the idea
- 2 subagents for the idea
- 1 neutral subagent that gives 1 strong pro and 1 strong con

Stage 1 should feel exploratory and independent. The subagents should not all say the same thing.

### Stage 2: Deep Debate

Launch 2 additional subagents.

Required split:

- 1 fully pro
- 1 fully against

These subagents should make the strongest possible case for their side using:

- market logic,
- customer pain,
- competition,
- timing,
- feasibility,
- and evidence where possible.

Stage 2 should sharpen the argument on both sides, not repeat Stage 1.

### Stage 3: Final Judgment

The main agent reads all subagent output and makes the final call.

The final response must:

- give the idea a score from 1 to 10,
- summarize the strongest positive arguments,
- summarize the strongest negative arguments,
- state a clear verdict,
- and ask whether the user wants to plan an MVP next.

## Output Format

The final response should be concise and decision-oriented.

It should include:

- score out of 10,
- short verdict,
- positives,
- negatives,
- and an MVP question.

## Behavioral Rules

- Keep pro and con agents meaningfully different.
- Treat the neutral agent as a real balancing role, not filler.
- Prefer evidence and market reasoning over vague enthusiasm.
- If the market looks weak, crowded, or unproven, say so plainly.
- If the idea looks strong, explain why it survives criticism.
- Avoid giving the user a false sense of certainty.

## Success Criteria

The skill is successful if it can:

- expose weak ideas quickly,
- support strong ideas with real reasoning,
- surface useful market and execution risks,
- and help the user decide whether the idea deserves an MVP.

