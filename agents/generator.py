from transformers import pipeline

def generate_code(instruction):
    generator_pipeline = pipeline("text-generation", model="huggingface/CodeGPT-small-py")
    prompt = f"Genera el siguiente código basado en esta instrucción:\n{instruction}"
    code = generator_pipeline(prompt, max_length=500)
    return code[0]['generated_text']
