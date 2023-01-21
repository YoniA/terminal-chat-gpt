import openai
import os
import sys


def run_query(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


def main():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    query = sys.argv[1].strip()
    answer = run_query(query) if query else "no query"
    print(answer)
    exit


if __name__ == "__main__":
    main()
