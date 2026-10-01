from langchain_core.prompts import ChatPromptTemplate

def prompt_template(question,documents):

    context = "\n\n".join(document['page_content'] for document in documents )
    prompt = ChatPromptTemplate.from_template(
        """
Act as RAG assistant.

Give from the only above context.

Rules
- If the answer is not in the context ,say 
"Answer is the not available in the provided context".
- Do not make up the Answer.
- Give answer concise.
- Do not give outside the information.
- Give clear answer structure.
- Do not repeat thE  Answer.
- GIve only final Answer.
- do not give Assistant.

context:
{context}

Question:
{question}

Answer

"""
    )

    final_prompt = prompt.invoke({
        "context":context,
        "question":question
    })

    return final_prompt
