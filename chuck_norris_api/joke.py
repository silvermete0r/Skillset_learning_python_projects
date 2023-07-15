import requests
import json

def generate_joke():
    api_url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(api_url)
    data = response.json()
    joke = {
        'id': data['id'],
        'text': data['value']
    }
    return joke

def save_ratings():
    global jokes_base
    
    with open('jokes_base.json', 'w') as file:
        json.dump(jokes_base, file)

def continue_check():
    choice = input('Do you want to continue? yes/no: ')
    if choice.lower() == 'yes':
        pass
    elif choice.lower() == 'no':
        save_ratings()
        exit()
    else:
        print('You entered incorrect value, ok let\'s continue:)')

def add_rating(joke, rating):
    global jokes_base
    
    if joke['id'] in jokes_base:
        jokes_base[joke['id']]['rating'].append(rating)
    else:
        jokes_base[joke['id']] = {
            'rating': [rating],
            'text': joke['text']
        }

    print(f'Success, this joke\'s average rating is: {round(sum(jokes_base[joke["id"]]["rating"]) / len(jokes_base[joke["id"]]["rating"]), 2)}')
    print('-----')


if __name__ == '__main__':
    try:
        with open('jokes_base.json', 'r') as file:
            jokes_base = json.load(file)
    except FileNotFoundError:
        print('Jokes Base does not exist!')
        exit()

    print('Joke Rating App')
    print('-----')

    while True:
        joke = generate_joke()

        print(f'🤠 Joke: {joke["text"]}', end='\n\n')
        print('1 - 😠 | 2 - 😐 | 3 - 🙂 | 4 - 😂 | 5 - 🤣')
        try:
            rating = int(input('Enter your rating for this joke: '))
            add_rating(joke, rating)
            
        except ValueError:
            print('Please enter a valid number 😠')

        continue_check()