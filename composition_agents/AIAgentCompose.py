# phi4_client_example.py

import requests
import json
from composition_agent import CompositionAgent

PHI4_URL = "http://localhost:8001/v1/chat/completions"
PHI4_MODEL = "gpt-oss:20b"  # Adjust if your model id is different


def llm_generate(prompt: str) -> str:
    """
    Minimal client for Phi-4.
    Adjust this to match your actual FastAPI / server contract.
    """
    payload = {
        "model": PHI4_MODEL,
        "messages": [
            {"role": "system", "content": "You are a careful JSON-producing assistant."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 1024,
        "temperature": 0.2,
    }

    resp = requests.post(PHI4_URL, json=payload, timeout=200)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# -------------------------------------------------------------------------
# Example usages
# -------------------------------------------------------------------------
if __name__ == "__main__":
    agent = CompositionAgent(llm_generate=llm_generate)

    # 1) JSON / dict input mode
    json_input = {
  "customers": [
    {
      "CUSTOMER_ID": "CUST001",
      "NAME": "Jane Smith",
      "ACCOUNT_NUMBER": "987654321",
      "STATEMENT_PERIOD": "2025-10-01 to 2025-10-31",
      "ADDRESS": "12 Garden Way, Tampa, FL 33614",
      "OPENING_BALANCE": 2500.45,
      "CLOSING_BALANCE": 3410.22,
      "TRANSACTIONS": [
        {"DATE": "2025-10-02", "DESCRIPTION": "PAYROLL DEPOSIT", "AMOUNT": 1850.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-03", "DESCRIPTION": "STARBUCKS", "AMOUNT": -6.45, "TYPE": "DEBIT"},
        {"DATE": "2025-10-05", "DESCRIPTION": "CHEQUE HOLD RELEASE", "AMOUNT": 500.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-06", "DESCRIPTION": "AMZN MKTPLACE", "AMOUNT": -85.90, "TYPE": "DEBIT"},
        {"DATE": "2025-10-07", "DESCRIPTION": "UTILITY BILL", "AMOUNT": -110.30, "TYPE": "DEBIT"},
        {"DATE": "2025-10-09", "DESCRIPTION": "ATM WITHDRAWAL", "AMOUNT": -200.00, "TYPE": "DEBIT"}
      ],
      "SUMMARY": "Customer reports repeated cheque hold delays.",
      "RECOMMENDATION": "Implement ICP batch automation to reduce hold time."
    },
    {
      "CUSTOMER_ID": "CUST002",
      "NAME": "Michael Johnson",
      "ACCOUNT_NUMBER": "445122001",
      "STATEMENT_PERIOD": "2025-10-01 to 2025-10-31",
      "ADDRESS": "822 Ridgeview Dr, Orlando, FL 32835",
      "OPENING_BALANCE": 420.00,
      "CLOSING_BALANCE": 190.35,
      "TRANSACTIONS": [
        {"DATE": "2025-10-01", "DESCRIPTION": "GROCERY", "AMOUNT": -72.34, "TYPE": "DEBIT"},
        {"DATE": "2025-10-03", "DESCRIPTION": "ATM FEE REVERSAL", "AMOUNT": 3.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-04", "DESCRIPTION": "PETRO CANADA", "AMOUNT": -45.20, "TYPE": "DEBIT"},
        {"DATE": "2025-10-05", "DESCRIPTION": "SALARY PART-TIME", "AMOUNT": 350.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-10", "DESCRIPTION": "SUBSCRIPTION", "AMOUNT": -15.00, "TYPE": "DEBIT"},
        {"DATE": "2025-10-11", "DESCRIPTION": "WALMART", "AMOUNT": -150.11, "TYPE": "DEBIT"}
      ],
      "SUMMARY": "Customer disputes unauthorized subscription charges.",
      "RECOMMENDATION": "Investigate recurring merchant authorization trail."
    },
    {
      "CUSTOMER_ID": "CUST003",
      "NAME": "Priya Patel",
      "ACCOUNT_NUMBER": "110022334",
      "STATEMENT_PERIOD": "2025-10-01 to 2025-10-31",
      "ADDRESS": "50 Crosslake Blvd, Miami, FL 33177",
      "OPENING_BALANCE": 8900.12,
      "CLOSING_BALANCE": 9122.67,
      "TRANSACTIONS": [
        {"DATE": "2025-10-02", "DESCRIPTION": "WIRE INCOMING", "AMOUNT": 2500.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-04", "DESCRIPTION": "TARGET", "AMOUNT": -122.49, "TYPE": "DEBIT"},
        {"DATE": "2025-10-05", "DESCRIPTION": "ACH PAYMENT", "AMOUNT": -350.00, "TYPE": "DEBIT"},
        {"DATE": "2025-10-09", "DESCRIPTION": "RENT", "AMOUNT": -2000.00, "TYPE": "DEBIT"},
        {"DATE": "2025-10-12", "DESCRIPTION": "REFUND", "AMOUNT": 94.25, "TYPE": "CREDIT"}
      ],
      "SUMMARY": "Customer requests explanation of large rent payment processing time.",
      "RECOMMENDATION": "Provide ACH batch timing documentation."
    },
    {
      "CUSTOMER_ID": "CUST004",
      "NAME": "Carlos Mendes",
      "ACCOUNT_NUMBER": "558877221",
      "STATEMENT_PERIOD": "2025-10-01 to 2025-10-31",
      "ADDRESS": "663 Harbor View, Fort Lauderdale, FL 33312",
      "OPENING_BALANCE": 1550.00,
      "CLOSING_BALANCE": 1620.40,
      "TRANSACTIONS": [
        {"DATE": "2025-10-02", "DESCRIPTION": "CHEQUE DEPOSIT", "AMOUNT": 750.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-05", "DESCRIPTION": "RESTAURANT", "AMOUNT": -45.00, "TYPE": "DEBIT"},
        {"DATE": "2025-10-06", "DESCRIPTION": "CAR WASH", "AMOUNT": -18.00, "TYPE": "DEBIT"},
        {"DATE": "2025-10-07", "DESCRIPTION": "EBAY", "AMOUNT": -150.00, "TYPE": "DEBIT"},
        {"DATE": "2025-10-09", "DESCRIPTION": "REFUND", "AMOUNT": 33.40, "TYPE": "CREDIT"}
      ],
      "SUMMARY": "Customer questions cheque deposit hold duration.",
      "RECOMMENDATION": "Provide hold policy document to customer."
    },
    {
      "CUSTOMER_ID": "CUST005",
      "NAME": "Akhil Sharma",
      "ACCOUNT_NUMBER": "889900112",
      "STATEMENT_PERIOD": "2025-10-01 to 2025-10-31",
      "ADDRESS": "21 Lakeshore Ave, Jacksonville, FL 32224",
      "OPENING_BALANCE": 120.00,
      "CLOSING_BALANCE": 305.60,
      "TRANSACTIONS": [
        {"DATE": "2025-10-03", "DESCRIPTION": "UPWORK PAYMENT", "AMOUNT": 225.00, "TYPE": "CREDIT"},
        {"DATE": "2025-10-06", "DESCRIPTION": "UBER", "AMOUNT": -23.55, "TYPE": "DEBIT"},
        {"DATE": "2025-10-08", "DESCRIPTION": "NETFLIX", "AMOUNT": -16.99, "TYPE": "DEBIT"},
        {"DATE": "2025-10-10", "DESCRIPTION": "AT&T", "AMOUNT": -72.30, "TYPE": "DEBIT"},
        {"DATE": "2025-10-11", "DESCRIPTION": "REFUND", "AMOUNT": 22.44, "TYPE": "CREDIT"}
      ],
      "SUMMARY": "Customer wants explanation of repeated subscription charges.",
      "RECOMMENDATION": "Review subscription cycle and alert options."
    }
  ]
}


    mapping = agent.compose_many(
        template_path= r"C:\Users\balum\OneDrive\Documents\Balu career\AI\Local GPT OSS 20b\Agents\templates\complaint_template.docx",
        input_data=json_input,
        output_path=r"C:\Users\balum\OneDrive\Documents\Balu career\AI\Local GPT OSS 20b\Agents\templates\complaint_filled_from_json.docx",
    )
    print("Saved doc with mapping:", mapping)

    # 2) Human text input mode (Phi-4 will fill fields)
    human_text = """
Customer: Jane Smith
Account: 987654321
Situation: Customer is unhappy about repeated holds on deposited cheques,
delaying access to funds. She wants clarity on policy and a firm timeline
when this will stop.

We want the letter to be empathetic, clearly describe TD's policy,
and outline the operational fixes we are planning, including potential
ICP automation and batch control enhancements.
"""

    mapping2 = agent.compose(
        template_path=r"C:\Users\balum\OneDrive\Documents\Balu career\AI\Local GPT OSS 20b\Agents\templates\complaint_template.docx",
        input_data=human_text,
        output_path=r"C:\Users\balum\OneDrive\Documents\Balu career\AI\Local GPT OSS 20b\Agents\templates\complaint_filled_from_json.docx",
    )
    print("Saved doc with mapping:", mapping2)
