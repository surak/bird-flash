import stackprinter
from dotenv import load_dotenv
import os
import requests

# Stack printer is a better way to print errors
stackprinter.set_excepthook(style="darkbg2") 


input_dir = "/home/strube/birds"
if not os.path.exists(input_dir):
    exception = FileNotFoundError("Input directory not found")

def main():
    load_dotenv()


if __name__ == "__main__":
    main()
