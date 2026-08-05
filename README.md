# Pydantic AI + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/pydantic-ai-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/pydantic-ai-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable Pydantic AI examples powered directly by the official [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent) executor.

> Examples only: no additional SDK, PyPI package, or independent release lifecycle.

## Repository scope

Pydantic AI generates typed tool schemas from ordinary functions. The demo keeps those functions thin and delegates CapSolver behavior to the shared agent library.

## Quick start

```bash
git clone https://github.com/capsolver-ai/pydantic-ai-capsolver.git
cd pydantic-ai-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Export [`.env.example`](.env.example) values and run `python examples/quickstart.py`.

## Key integration code

```python
from capsolver_agent import create_executor
from pydantic_ai import Agent

capsolver = create_executor()
agent = Agent("openai:gpt-4.1-mini")

@agent.tool_plain
async def get_capsolver_balance() -> str:
    return str(await capsolver.execute("get_balance", {}))
```

See [`examples/quickstart.py`](examples/quickstart.py) for balance and solving tools.

## Project layout

```text
examples/quickstart.py   Pydantic AI Agent and typed tools
requirements.txt         Shared SDK repositories plus Pydantic AI
tests/test_demo.py        Offline validation
.github/workflows/ci.yml  Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver for AI agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [Pydantic AI function tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/)

## Responsible use

Use the example only for lawful, user-authorized workflows that respect target-site terms. Never commit secrets or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

Pydantic AI is a third-party project. This repository is maintained by CapSolver and is not affiliated with or endorsed by Pydantic.
