from transformers import pipeline

def optimize_code(code):
    optimizer_pipeline = pipeline("text-generation", model="huggingface/CodeGPT-small-py")
    prompt = f"Optimiza el siguiente código para mejorar su rendimiento:\n{code}"
    optimized_code = optimizer_pipeline(prompt, max_length=500)
    return optimized_code[0]['generated_text']
