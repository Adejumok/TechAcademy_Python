
import openai
openai.api_key = "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"

context = "Albert Einstein was a German-born theoretical physicist who developed the theory of relativity."
question = "Where was Albert Einstein born?"
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
  max_tokens=50
)

answer = response.choices[0].text.strip()
print(answer)

