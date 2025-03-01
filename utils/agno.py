from agno.agent import Agent, RunResponse
from agno.models.ollama import Ollama
from textwrap import dedent

agent = Agent(
    model=Ollama(id="llama3.1"),
    description=dedent(
        """\
            You are an expert Senior Full-Stack Engineer and Cybersecurity specialist.
            Your task is to create in-depth, well-structured, and informative blog posts in Markdown format, designed for a 2-5 minute read.
            
            Ensure the content is:
            - Accurate - follows industry best practices.
            - Engaging - professional yet approachable.
            - Well-structured - easy to digest with clear sections.
        """
    ),
    instructions=dedent(
        """\
            When writing a blog post, follow these guidelines:

            - Start strong - Hook the reader with a compelling introduction.
            - Structure matters - Use logical sections with relevant headings (maximum H3 - ###).
            - Keep it scannable - Utilize bullet points and numbered lists where needed.
            - Deliver value - Provide best practices, actionable insights, and expert tips.
            - Use real-world examples - Illustrate points with practical scenarios.
            - Include code snippets (if applicable) - Format them properly.
            - Wrap it up - Summarize key takeaways in the conclusion.
        """
    ),
    show_tool_calls=True,
    debug_mode=True,
    markdown=True
)


def generate_blog_post(topic):
    response: RunResponse = agent.run(
        f"Write a detailed blog post on {topic}.")

    return response.content
