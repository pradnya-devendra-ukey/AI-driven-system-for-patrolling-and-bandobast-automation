from transformers import pipeline
from rag.knowledge_base import KnowledgeBase

class PatrolRAG:

    def __init__(self):

        self.kb = KnowledgeBase()

        self.generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )

        docs = [
            "Large crowds often lead to pickpocketing incidents.",
            "Unattended bags in crowded areas may indicate security risk.",
            "Heavy vehicle congestion increases accident risk."
        ]

        self.kb.add_documents(docs)

    def generate_summary(self, event):

        context = self.kb.retrieve(event)

        prompt = f"""
        Context: {context}

        Current Event: {event}

        Generate a patrol intelligence report with:
        - risk indicators
        - recommendations
        """

        result = self.generator(prompt, max_length=120)

        return result[0]["generated_text"]
