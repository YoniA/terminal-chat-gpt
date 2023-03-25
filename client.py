#!/usr/bin/python3

import openai
import os
import sys

openai.api_key = os.environ.get("OPENAI_API_KEY")


def run_query(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=3000,
        n=2,
        stop=None,
        temperature=0.7
    )

    message = completions.choices[0].text
    new_history = prompt + message
    return message.strip(), new_history


def main():
    os.system('clear')
    history = ""
    while True:
        query = input("You: ")
        if not query:
            print("\033[31m{}\033[0m".format("Please enter a query"))
            print("\n")
            continue
        prompt = history + query + "\n\n" 
        answer, history = run_query(prompt)
        print("\033[32m{}\033[0m".format(answer))
        print("\n")


if __name__ == "__main__":
    main()



# https://beta.openai.com/docs/models/codex
