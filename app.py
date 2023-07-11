import random
from flask import Flask, request, jsonify

app = Flask(__name__)

jokes = [
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "What has four wheels and flies? A garbage truck!",
    "Did you hear the one about the bossy man at the bar? He ordered everyone around!",
    "But before we get started, we're curious to know if you've ever had a bad sausage - If you have, then probably "
    "know that they're the wurst!",
    "Why did the pony ask for a glass of water? Because it was a little horse!",
    "Is there anything worse than when it's raining cats and dogs? Yes, hailing taxis!",
    "How many apples can you grow on a tree? All of them!",
    "My manager told me to have a good day. So I didn't go into work!",
    "What did the girl say to her fingers? I'm counting on you!",
    "What do kids play when they have nothing else to do? Bored games!"
]

@app.route('/joke', methods=['GET'])
def get_joke():
    num_joke = int(request.args.get('num', 1))
    if num_joke <= 0:
        return jsonify({'error': 'Please provide number of jokes'})

    random_joke = random.sample(jokes, num_joke)
    response = jsonify({'joke': random_joke})
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
