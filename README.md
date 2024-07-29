# GPT-Auto-Car-Dealer-Negotiator

Automate the process of creating email drafts to start conversations and reply to dealerships, aiming to get the best OTD (Out-The-Door) price using the Gemini LLM.

## Setup

1. **Edit Configuration**
   - Update `settings.ini` with your information and provide your Gemini API key.

2. **Gmail API Setup**
   - Follow the [Gmail API Quickstart Guide for Python](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application).
   - Download `credentials.json` and place it in the root directory of the project.

3. **Run the Script**
   - Execute `main.py`. This script will run in a loop, continuously checking the best OTD price you have received from each dealer and creating draft replies if applicable.

4. **Review and Send Drafts**
   - When convenient, review the drafts created by the LLM model, make any necessary edits, and send the email replies.

---
Happy negotiating! 🚗💼✉
