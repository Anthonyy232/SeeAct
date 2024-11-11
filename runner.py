import asyncio
import os

from seeact_package.seeact.agent import SeeActAgent

filename = "key.env"


def get_api(name):
    with open(name) as f:
        return f.read().strip()


os.environ["GEMINI_API_KEY"] = get_api(filename)


async def run_agent():
    agent = SeeActAgent(
        model="gemini-1.5-flash",
        default_task="Register an account with both username and password as test. Then login and then change my password to test2.",
        default_website="http://localhost/",
        rate_limit=15
    )
    await agent.start()
    while not agent.complete_flag:
        prediction_dict = await agent.predict()
        await agent.execute(prediction_dict)
    await agent.stop()


if __name__ == "__main__":
    asyncio.run(run_agent())
