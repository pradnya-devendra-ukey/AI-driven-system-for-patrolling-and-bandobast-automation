from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def generate_summary(event):

    prompt = f"""
    Police AI assistant.

    Event: {event}

    Generate patrol intelligence summary and recommendation.
    """

    result = generator(prompt, max_length=120)

    return result[0]["generated_text"]
