import os

def main(args):
      URL=os.getenv('TEST')
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!!!!" + TEST
      print(greeting)
      return {"body": greeting}
  