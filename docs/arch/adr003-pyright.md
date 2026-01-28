# ADR003: Implementing Static Type Checking


## Context
In languages like Java (which I've used in other CS classes), the compiler catches type errors before the code runs. Python doesn't do this by default, which means a simple typo can crash our app at runtime. We need a "guardrail" to catch these type mismatches early.

## Forces
* **Developer Velocity:** I want immediate feedback in VSCode with red squiggly lines when I pass the wrong type to a function.
* **Integration:** The tool needs to work well with the Python extensions we already have in our Dev Container.

## Decision
I am choosing **Pyright**.

While `mypy` is the original standard, Pyright is maintained by Microsoft and is the engine that powers VSCode's internal type checking (Pylance). It's significantly faster and provides a better experience within the IDE, which will help me code faster without waiting for a slow check to finish.

## Consequences
* **Positive:** We get "Java-like" safety in a dynamic language. 
* **Negative:** I have to be more disciplined about adding type hints (like `name: str`) to my functions.