# ?? Project overview ù AI Customer Support RAG

One-page brief for demos, GitHub, and portfolio.

## Thumbnail

![Project thumbnail](assets/thumbnail.jpg)

## Problem

Customer support teams answer the same policy questions every day. Staff and chatbots often **guess** refund, warranty, or payment rules. Wrong answers create tickets, chargebacks, and distrust.

## Solution

A local **RAG chatbot** that:

- Reads the company PDFs in `Data/`
- Retrieves the closest policy chunks
- Answers only from that text
- Says the answer is unavailable when the documents do not contain it

## Demo (real run)

![App output](assets/app-output.png)

- **Payment policy** ? not in the retrieved chunk ? honest refusal  
- **Refund policy** ? answered from `customer_policies.pdf` (5 business days after inspection)

## Stack snapshot

| Layer | Choice |
| --- | --- |
| UI | Streamlit chat + sidebar sources |
| Retrieval | Chroma + MiniLM embeddings |
| Generation | Qwen2.5-3B-Instruct (local) |
| Knowledge | Policies, FAQ, product guide, warranty PDFs |

## How to run

```bash
pip install -r requirements.txt
streamlit run Modules/app.py
```

## Outcome

A working, grounded support assistant you can show in a portfolio: **documents in ? cited-style chunks in the sidebar ? policy-safe answers in chat.**
