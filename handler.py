# handler.py
 
from requests_html import HTMLSession
import numpy as np


def main(event, context):
    a = np.arange(15).reshape(3, 5)
    s = HTMLSession()
    r = s.get('https://ebartan.dev')

    print("Your numpy array:")
    print(a)
    print(r)


if __name__ == "__main__":
    main('', '')