from transformers import pipeline

def document_code(code):
    documenter_pipeline = pipeline("text-generation", model="huggingface/CodeGPT-small-py")
    prompt = f"Genera documentación para el siguiente código:\n{code}"
    documentation = documenter_pipeline(prompt, max_length=500)
    return documentation[0]['generated_text']
