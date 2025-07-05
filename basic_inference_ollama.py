from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

# List available models
models = client.models.list()

# Select the first LLM
llm = next(m for m in models if m.model_type == "llm")
model_id = llm.identifier

print("Model:", model_id)

response = client.inference.chat_completion(
    model_id=model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Artificial Intelligence ? Give me a detailed answer?"},
    ],
)
print(response.completion_message.content)
