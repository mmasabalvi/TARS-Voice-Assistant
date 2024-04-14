import openai

# Set your OpenAI API key
openai.api_key = 

def generate_resignation_email():
    prompt = """I am done with my boss please write a resignation letter for me"""

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "You are resigning from your position."}, {"role": "user", "content": prompt}],
      temperature=0.5,
      max_tokens=150
    )

    return response#.choices[0].message['content']

if __name__ == "__main__":
    resignation_email = generate_resignation_email()
    print(resignation_email)
