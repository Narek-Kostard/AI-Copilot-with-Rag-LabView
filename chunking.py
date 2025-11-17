chunk_size = 20 
with open("#Documentation", "r", encoding="utf-8") as f:
    lines = f.readlines()

chunks = []
for i in range(0, len(lines), chunk_size):
    chunk_text = "".join(lines[i:i + chunk_size]).strip()
    if chunk_text:
        chunks.append({
            "id": i // chunk_size,
            "content": chunk_text
        })


import json
with open("chunk-name.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

