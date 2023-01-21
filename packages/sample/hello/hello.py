import os

def main(args):
      print(os.getenv('URL'))
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!!!!"
      print(greeting)
      return {"body": greeting}
  