
from alith import Agent, LazAIClient
 
# 1. Join the iDAO, register user wallet on LazAI and deposit fees (Only Once)
LAZAI_IDAO_ADDRESS = "0x3e186f0b9568bf5415854577D042843A9f1C2266" # Replace with your own address
client = LazAIClient()
# Add by the inference node admin
 
client.deposit_inference(LAZAI_IDAO_ADDRESS, 1000000)
 
try:
    client.get_user(client.wallet.address)
    print("User already exists")
except Exception:
    print("User does not exist, adding user")
    client.add_user(10000000)
 
# 2. Request the inference server with the settlement headers and DAT file id
file_id = 10  # Use the File ID you received from the Data Contribution step
url = client.get_inference_node(LAZAI_IDAO_ADDRESS)[1]
print("url", url)
agent = Agent(
    # Note: replace with your model here
    model="deepseek/deepseek-r1-0528",
    # OpenAI-compatible inference server URL
    base_url=f"{url}/v1",
    # Extra headers for settlement and DAT file anchoring
    extra_headers=client.get_request_headers(LAZAI_IDAO_ADDRESS, file_id=file_id),
)
print(agent.prompt("summmarize it"))