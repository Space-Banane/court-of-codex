---
name: idea-evaluator
description: Evaluate startup ideas, product concepts, MVPs, and business ideas with staged multi-agent debate, market reasoning, competitive analysis, and a final score and verdict. Use when asked whether an idea is worth pursuing, whether there is a real market, what the strongest reasons for and against are, or whether to plan an MVP.
---

# Idea Evaluator

## Purpose

Use this skill to judge whether a user idea is worth building.

Treat the task like a structured decision engine:

- gather opposing viewpoints,
- pressure-test the idea,
- assess market potential,
- and give a clear recommendation.

## Operating Model

Run the evaluation in 3 stages.

Before moving to the next stage, wait until every agent in the current stage has finished its research and returned its output.

### Stage 1: Broad Scan

Launch 5 subagents.

Assign them distinct roles:

- 2 against the idea
- 2 for the idea
- 1 neutral agent that gives 1 strong pro and 1 strong con

Make the roles meaningfully different. Do not let them collapse into the same answer.

Each subagent should focus on:

- market need
- customer pain
- competition
- timing
- feasibility
- evidence where available

### Stage 2: Deep Debate

Launch 2 additional subagents.

Assign them these roles:

- 1 fully pro
- 1 fully against

Ask each one to make the strongest possible case for its side.

They should sharpen the debate, not repeat Stage 1.

### Stage 3: Final Judgment

Read all subagent output and make the final call.

Your final response must:

- give the idea a score from 1 to 10,
- summarize the strongest positive arguments,
- summarize the strongest negative arguments,
- state a clear verdict,
- and ask whether the user wants to plan an MVP next.

## Decision Standards

Use evidence and market logic over vague enthusiasm.

If the market looks weak, crowded, or unproven, say so plainly.

If the idea looks strong, explain why it survives criticism.

Avoid false certainty.

## Final Output Format

Keep the response concise and decision-oriented.

Include:

- score out of 10
- short verdict
- positives
- negatives
- MVP question
