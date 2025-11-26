from unstructured.partition.text import partition_text

def load_txt(path):
    elements = partition_text(path)
    return "\n".join([el.text for el, _ in enumerate(elements) if hasattr(el, "text")])
