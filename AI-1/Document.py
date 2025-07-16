# import re
# documents = [
#  "The new iPhone 15 has been released.",
#  "Galaxy S23 Ultra is the latest model.",
#  "Nokia was a top brand in the 2000s.",
#  "Pixel phones are known for their cameras."
#  ]
# pattern = r"\b(iPhone|Galaxy)\b"
# matched_docs = [doc for doc in documents if re.search(pattern, doc, re.IGNORECASE)]
# for doc in matched_docs:
#  print("Matched:", doc)

import re
documents = [
    "Apple just launched the new iPhone 16 Pro Max.",
    "Samsung unveiled the Galaxy Z Fold5 last week.",
    "Motorola dominated the mobile market in the early 2000s.",
    "Google Pixel 8 excels in AI photography features."
]
pattern = r"\b(iPhone|Galaxy)\b"
matched_docs = [doc for doc in documents if re.search(pattern, doc, re.IGNORECASE)]
for doc in matched_docs:
    print("Matched:", doc)