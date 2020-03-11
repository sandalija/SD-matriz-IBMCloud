def main(args):
    name = args.get("name", "pom")
    greeting = "Hello " + name + "!"
    print(greeting)
    return {"greeting": greeting}