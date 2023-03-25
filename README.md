# ChatGPT client for Linux terminal


## How to use

- Install openai package: `pip install openai`
- Get API key from your openai account
- Add your API key to your `.bashrc`/`.zshrc`: `export OPENAI_API_KEY=<your key>`
- Add execute permission to the script: `chmod +x client.py`
- Run `./client.py`


## Demo

![demo](demo.PNG)


## Known Issues

The textual engines are limited to maximum context length. When this limit is exceeded, the program will crash,
throwing the following error:

```python
InvalidRequestError: This model's maximum context length
```
