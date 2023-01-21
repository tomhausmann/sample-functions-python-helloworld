import os
import time

TEST=os.getenv("TEST")

def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!!!!" + TEST + " " + time.localtime()
      print(greeting)
      return {"body": greeting}