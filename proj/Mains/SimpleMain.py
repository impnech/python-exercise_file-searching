from dotenv import load_dotenv
from Menu.QueryHandler import handle_query
# override true because it doesn't update automatically, this is before any other import, so there's no need to update
load_dotenv(override=True)

# imports
from Loggers.g_logging import g_logger

old_test_query = """
language used in web development. : change is one of the most pressing issues of our  :  learning has  revolutionized the deep field of artificial :  Space exploration has advanced  " deep 
"""
test_query1 = """
language used in web .: change pressing :  learning revolutionized exploration advanced  
"""
test_query2 = """
language used in web : change press :  learn revolutionized exploration advanced  
"""

is_test = True


def run(is_it_test: bool = is_test):
    # process
    q = False
    while not q:
        if is_it_test == True:
            query = old_test_query
            q = True
        else:
            query: str = input("Enter query: (quitting is still with Ctrl+C)")

        g_logger.info(f"got from user query, \"{query}\"d")

        handle_query(query)


def compare():
    print("same words")
    handle_query(test_query1)
    print("words modified")
    handle_query(test_query2)


def main():
    compare()


if __name__ == "__main__":
    main()
