import time
from langchain_core.prompts import ChatPromptTemplate

identity = (
            "system",
            "You are an expert in negotiating with car dealers to get the best deals, using the car information and competitive offers from other dealerships",
        )

customer_info = ("human", "My name is {name}, My zipcode is {zipcode}, and I want to buy a new car {car_model}")


start_convo_prompt = ChatPromptTemplate.from_messages(
    [
        identity,
        ("human", "Search if I have email history with {dealer_email}."),
        ("human", "if I have not sent an email to them, write a draft to dealership {dealer_email} to ask for the best OTD price it offer"),
        customer_info,
        ("human", "Don't ask me further question"),
    ]
)

query_status_prompt = ChatPromptTemplate.from_messages(
    [
        identity,
        customer_info,
        ("human", "Search and Read the emails between me and {dealer_email}, provide me the latest summary of the best OTD and other important information."),
        ("human", "if there is no information, give no info"),
        ("human", "Don't ask me further question"),
    ]
)

check_reply_prompt = ChatPromptTemplate.from_messages(
    [
        identity,
        ("human", "Search between me and {dealer_email}. Return yes only if there is no draft email to {dealer_email} and there is unread emails from {dealer_email}"),
    ]
)

create_reply_draft_prompt = ChatPromptTemplate.from_messages(
    [
        identity,
        ("human", "Read all emails between me and {dealer_email}"),
        ("human", "Create draft reply to {dealer_email} to continue conversation to get the best OTD price on the original thread"),
        customer_info,
        ("human", "So far those are the offers I got for dealers: {dealers_offer_info}"),
        ("human", "Don't ask me further question"),
    ]
)

def start_convo(agent, invoke_input):
    agent_with_prom = start_convo_prompt | agent
    result = agent_with_prom.invoke(
        invoke_input,
    )
    print("finish start_convo")
    return result['output']

def query_status(agent, invoke_input):
    agent_with_prom = query_status_prompt | agent
    result = agent_with_prom.invoke(
        invoke_input,
    )
    print("finish query_status")
    return result['output']

def check_reply_status(agent, invoke_input):
    agent_with_prom = check_reply_prompt | agent
    result = agent_with_prom.invoke(
        invoke_input,
    )
    print("finish check_reply_status")
    return result['output']

def create_reply_draft(agent, invoke_input):
    agent_with_prom = create_reply_draft_prompt | agent
    result = agent_with_prom.invoke(
        invoke_input,
    )
    print("finish create_reply_draft")
    return result['output']
