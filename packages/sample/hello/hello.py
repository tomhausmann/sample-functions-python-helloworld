import os

TEST=os.getenv("TEST")

def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!!!!" + TEST
      print(greeting)
      return {"body": greeting}