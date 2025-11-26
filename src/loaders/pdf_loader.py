from unstructured.partition.pdf import partition_pdf

def load_pdf(path):
    elements = partition_pdf(path, 
                             strategy="auto", 
                             languages=["en"])
    return "\n".join([el.text for el in elements if hasattr(el, "text")])
