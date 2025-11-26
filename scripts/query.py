from src.pipelines.query_pipeline import run_query

if __name__ == "__main__":
    q = input("Enter query: ")
    results = run_query(q, top_k=5)

    for rid, chunk, score in results:
        print("\nID:", rid)
        print("Score:", score)
        print(chunk, "...\n")
