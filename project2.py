import json
import ollama
from qdrant_client import QdrantClient

# Qdrant
client = QdrantClient(url="http://localhost:6333")

def get_context_from_qdrant(question, limit=2):
    vect = ollama.embeddings(model='nomic-embed-text', prompt=question)
    search_result = client.query_points(
        collection_name="working_collection",
        query=vect["embedding"],
        with_payload=True,
        limit=limit
    ).points

    context = ""
    for res in search_result:
        context += res.payload["content"] + "\n\n"
    return context.strip()

 
def is_labview_related(text: str) -> bool:

    keywords = ["labview", "ni", "virtual instrument", "block diagram"]
    text_lower = text.lower()
    return any(kw in text_lower for kw in keywords)


def main_logic(data):
    history = data["History"]
    user_input = data["content"]

    # формируем историю для Ollama
    history_with_context = history.copy()  # копируем историю

    if is_labview_related(user_input):
        context = get_context_from_qdrant(user_input)
        history_with_context.insert(0, {  # вставляем system в начало
            "role": "system",
            "content": f"Use the following context to answer:\n\n{context}"
        })

    history_with_context.append({"role": "user", "content": user_input})
    history.append({"role": "user", "content": user_input})


    try:
        response = ollama.chat(
            model='mistral',
            messages=history_with_context
        )
        assistant_response = response['message']['content']
    except Exception as e:
        assistant_response = f"Error communicating with Ollama: {str(e)}"

    # добавляем ответ ассистента в историю
    history.append({"role": "assistant", "content": assistant_response})

    return json.dumps({"History": history}, ensure_ascii=False)


def Run_chat(input_json_string):
    data = json.loads(input_json_string)
    return main_logic(data)


if __name__ == "__main__":
    input_json = input()
    print(Run_chat(input_json))