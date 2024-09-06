from transformers import pipeline

def review_code(diff):
    review_pipeline = pipeline("text-generation", model="huggingface/CodeGPT-small-py")
    prompt = f"Revisa los siguientes cambios de código y proporciona feedback:\n{diff}"
    review = review_pipeline(prompt, max_length=500)
    return review[0]['generated_text']
