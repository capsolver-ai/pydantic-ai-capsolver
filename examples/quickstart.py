"""Register CapSolver Agent execution as Pydantic AI tools."""

import json
import os

from capsolver_agent import create_executor
from pydantic_ai import Agent


capsolver = create_executor()
agent = Agent(
    os.getenv("PYDANTIC_AI_MODEL", "openai:gpt-4.1-mini"),
    instructions=(
        "Use CapSolver only for lawful, user-authorized workflows. "
        "Never invent target details."
    ),
)


@agent.tool_plain
async def get_capsolver_balance() -> str:
    """Return the current CapSolver account balance."""
    return json.dumps(await capsolver.execute("get_balance", {}), ensure_ascii=False)


@agent.tool_plain
async def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
    """Solve a supported CAPTCHA for a lawful, user-authorized workflow."""
    result = await capsolver.execute(
        "solve_captcha",
        {
            "captcha_type": captcha_type,
            "website_url": website_url,
            "website_key": website_key,
        },
    )
    return json.dumps(result, ensure_ascii=False)


async def main() -> None:
    result = await agent.run(
        os.getenv("DEMO_PROMPT", "Check my CapSolver balance using the available tool.")
    )
    print(result.output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
