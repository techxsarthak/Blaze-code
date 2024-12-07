#Please install micropip module from ide then enter code as follows
# import micropip
# micropip.install("wikipedia")
import wikipedia

def get_wikipedia_article(title):
    try:
        # Set the language (optional)
        wikipedia.set_lang("en")
        
        # Fetch the article content
        article_content = wikipedia.page(title).content
        return article_content
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError:
        return "Article not found."

# Example usage
article_title = "Python (programming language)"  # Change this to any Wikipedia article title
article_content = get_wikipedia_article(article_title)
print(article_content)
