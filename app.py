from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)
# List of restaurants near my house
food = ["Osmow's", 'Burrito Boyz', "Harvey's", 'Red Chilli', 'Meltwich', "Mary Brown's", "Popeye's", 'Subway', 'BarBurrito']

@app.route('/')
# Home page set to home.html
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
# Result page where users see which restaurant to go to
def result():
    ans1 = request.form['restaurant']

# Logic of website, if the input is not in the list, it will return invalid input else it will remove that entry-
    # -from the list and randomly choose a different restaurant
    if ans1 not in food:
        return render_template('home.html', error='Invalid input, this application is case sensitive and use apostrophes')
    else:
        food_copy = food.copy()
        food_copy.remove(ans1)
        message = choice(food_copy)
# Sends user to result page
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
