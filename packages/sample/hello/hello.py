import os

def main(args):
      URL=os.environ.get("URL")
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!!!!" + URL
      print(greeting)
      return {"body": greeting}
  