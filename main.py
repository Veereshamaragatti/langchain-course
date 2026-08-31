from dotenv import load_dotenv
# import os
# from langchain_openai import AzureChatOpenAI

load_dotenv()

# llm = AzureChatOpenAI(
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#     azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
#     api_version=os.getenv("AZURE_OPENAI_API_VERSION")
# )

# response = llm.invoke("What is Generative AI?")
# print(response.content)

def main():
    print("Helo World")

if __name__ == "__main__":
    main()