import settings
import time
from langchain_community.agent_toolkits import GmailToolkit
from langchain.agents import AgentType, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import gmail

wait_time = 120

def ask_yes_no_question(question):
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Please answer 'yes' or 'no'.")

def build_agent_with_gmail_tools():
    toolkit = GmailToolkit()
    api_key = settings.get_api_key()
    # Initialize the language model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key=api_key,
    )
    agent = initialize_agent(tools=toolkit.get_tools(), llm=llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent


agent = build_agent_with_gmail_tools()

config = settings.get_personal_setting()

question = "Is this your first time running script? Want to send emails to start conversation with car dealers?"
response = ask_yes_no_question(question)

if response == 'yes':
    for dealer_email in config['dealer_emails']:
        invoke_input = dict(config)
        invoke_input['dealer_email'] = dealer_email
        gmail.start_convo(agent, invoke_input)
        time.sleep(wait_time)
    time.sleep(wait_time)


while True:
    dealers_offer_infos = []
    for dealer_email in config['dealer_emails']:
        invoke_input = dict(config)
        invoke_input['dealer_email'] = dealer_email
        offer_status_info = gmail.query_status(agent, invoke_input)
        time.sleep(wait_time)
        if offer_status_info == "no info":
            continue
        dealers_offer_info = f" For {dealer_email}, {offer_status_info}"
        dealers_offer_infos.append(dealers_offer_info)
    
    # dealers_offer_infos_str = dealers_offer_infos.join("|")
    dealers_offer_infos_str = "|".join(dealers_offer_infos)
    for dealer_email in config['dealer_emails']:
        invoke_input = dict(config)
        invoke_input['dealer_email'] = dealer_email
        if gmail.check_reply_status(agent, invoke_input) == 'yes':
            time.sleep(wait_time)
            invoke_input['dealers_offer_info'] = dealers_offer_infos_str
            gmail.create_reply_draft(agent, invoke_input)
        time.sleep(wait_time)

