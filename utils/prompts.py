""" 
Custom Langchain prompt templates
"""

from langchain.prompts import PromptTemplate


def create_qa_prompt() -> PromptTemplate:
    """
    Prompt for retrieval QA chain
    """

    template = """\n\nHuman: Use the following pieces of context to answer the question at the end.

{context}

Question: {question}

\n\nAssistant:
Answer:"""

    return PromptTemplate(template=template, input_variables=["context", "question"])


def create_agent_prompt() -> PromptTemplate:
    """
    Prompt for the agent
    """

    prefix = """\n\nHuman: Answer the following questions as best you can. You have access to the following tools:"""

    format_instructions = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""

    suffix = """Begin!
Question: {input}
\n\nAssistant:
Thought: {agent_scratchpad}
"""

    return prefix, format_instructions, suffix
