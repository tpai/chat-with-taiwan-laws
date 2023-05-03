# Chat with Taiwan Laws

This tool extracts content from the PDF files of the Civil Code, Criminal Code, Code of Criminal Procedure, Labor Standards Act, Labor Pension Act, and Occupational Safety and Health Facility Regulations found in the National Regulations Database. This tool is for research and learning purposes only. Please consult a professional lawyer for any legal needs.

## Development Components

- LangChain
- FAISS
- OpenAI
- Streamlit

## Usage

```sh
docker run -d -p 8501:8501 -e OPENAI_API_KEY=$OPENAI_API_KEY tonypai/chat-with-taiwan-laws
```

## Demo

![demo](./demo.png)