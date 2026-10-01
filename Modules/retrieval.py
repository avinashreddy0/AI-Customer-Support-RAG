from indexing import indexing_file
from config import TOP_K

def retrieval_file(question):
    vector_database = indexing_file()
    retrieval = vector_database.as_retriever(search_kwargs = {"k":TOP_K})

    result = retrieval.invoke(question)

    documents = []
    for index,data in enumerate(result):
        page_content = data.page_content
        source= data.metadata.get("source")
        page = data.metadata.get("page")

        documents.append({
            'page_content':page_content,
            'source':source,
            'page':page
        })

        return documents