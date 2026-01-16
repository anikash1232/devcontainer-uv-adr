Title
Adopting uv for Fast Environment Setup and CI/CD

Context
We are building a microservice that needs to be deployed quickly using Docker. In this project, speed and efficiency are our top priorities. We are constantly rebuilding our environments and running tests in GitHub Actions, so we need a tool that doesn't make us wait minutes just to install a few things.

Decision
We will use uv as our primary tool for managing dependencies and environments. We will use it to generate our virtual environments and lock our dependencies into a uv.lock file.

Considered Options
Poetry: We rejected Poetry because it feels too "heavy" for a simple service, and its installation times would slow down our automated testing significantly.

Conda: We decided against Conda because it is overkill for a standard Python web project and is often much slower than uv.

Consequences
Benefits: Installation is nearly instantaneous because uv is written in Rust. It also handles installing Python itself, which means we don't have to worry about what version is on our laptops.

Costs: uv is a newer tool, so if we run into a weird bug, there might be fewer StackOverflow answers compared to older tools.

Risks: Because uv is moving so fast, we need to make sure we don't accidentally use a feature that changes in a week.