def greet(name: str = 'World'):
    print(f'\nHello, {name}!')
    
def main():
    username = input("What is your name? (optional)\n")
    greet(username)
    
if __name__ == "__main__":
    main()