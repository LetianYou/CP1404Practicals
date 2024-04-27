import wikipedia


def get_wikipedia_page():
    """Interactively with Wikipedia"""
    continue_search = True

    while continue_search:
        query = input("Enter a Wikipedia search term (or leave blank to exit): ")
        if not query:
            continue_search = False
        else:
            try:
                page = wikipedia.page(query, auto_suggest=False)
                print("\nTitle:", page.title)
                print("Summary:", page.summary)
                print("URL:", page.url)
            except wikipedia.DisambiguationError as e:
                print(f"Disambiguation error: {e.options}")
            except wikipedia.PageError:
                print("Error: Page not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

            print("\n")


get_wikipedia_page()
