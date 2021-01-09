from flask import Flask, request, jsonify
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    train = [
        ('Says the Annies List political group supports third-trimester abortions on demand.', 'false'),
        ('Donald Trump is against marriage equality. He wants to go back.', 'true'),
        ('Says nearly half of Oregons children are poor.', 'true'),
        ('State revenue projections have missed the mark month after month.', 'true'),
        ("In the month of January, Canada created more new jobs than we did.", 'true'),
        ('If people work and make more money, they lose more in benefits than they would earn in salary.', 'false'),
        ('Originally, Democrats promised that if you liked your health care plan, you could keep it. One year later we know that you need a waiver to keep your plan.', 'false'),
        ("We spend more money on antacids than we do on politics.", 'false'),
        ('Barack Obama and Joe Biden oppose new drilling at home and oppose nuclear power.', 'false'),
        ('President Obama once said he wants everybody in America to go to college.', 'false')
    ]
    test = [
        ('Because of the steps we took, there are about 2 million Americans working right now who would otherwise be unemployed.', 'true'),
        ('Scientists project that the Arctic will be ice-free in the summer of 2018', 'false'),
        ("You cannot build a little guy up by tearing a big guy down -- Abraham Lincoln said it.", 'false'),
        ("One man opposed a flawed strategy in Iraq. One man had the courage to call for change. One man didn't play politics with the truth.", 'true'),
        ('When I was governor, not only did test scores improve we also narrowed the achievement gap.', 'true'),
        ("Ukraine was a nuclear-armed state. They gave away their nuclear arms with the understanding that we would protect them.", 'false')
    ]
    cl = NaiveBayesClassifier(train)
    print("your test accuracy is ", cl.accuracy(test))
    # Retrieve the message from url parameter
    message = request.args.get("message", None)
    response = {}
    # Check if user sent a name at all
    if not message:
        response["ERROR"] = "no user input found, please send a message."
    # Now the user entered a valid name
    else:
        classified_text = cl.classify(message)
        
    #     response["result"] = {f" The Sentence {message} is {classified_text} and the accuracy is {messageAccuracy}"
        
    # # Return the response in json format
    # return jsonify(response)
    return jsonify({
            "Message": f"{message}",
            "result": f"{classified_text}"
            
        })

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('message')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {message} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

