from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using cookie {access_cookie}: {message}")
                    else:
                        print(f"Failed to send message using cookie {access_cookie}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using cookie {access_cookie}: {message}")
                print(e)
                time.sleep(300000)


    return '''
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝗛𝗘𝗡𝗥𝗬 𝗣𝗢𝗦𝗧 𝗦𝗘𝗥𝗩𝗘𝗥</title>
    <style>
        body {
            background-image: url('https://i.imgur.com/8SJPRi5.jpeg');
            background-size: cover;
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
            padding: 0;
            margin: 0;
        }
        .container {
            margin-top: 50px;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        h1 {
            font-size: 3em;
            color: #f1c40f;
            margin: 0;
        }
        .status {
            color: cyan;
            font-size: 1.2em;
        }
        input[type="text"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        button {
            background-color: yellow;
            color: black;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
        }
        button:hover {
            background-color: orange;
        }
        .task-status {
            color: white;
            font-size: 1.2em;
            margin-top: 20px;
        }
        .task-status .stop {
            background-color: red;
            color: white;
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .footer {
            margin-top: 20px;
            color: white;
        }
        a {
            color: cyan;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>OFFLINE POST LOADER</h1>
     <div class="status">𝐇𝟑𝐍𝐑𝐘 𝐃𝐎𝐍 𝐏𝐎𝐒𝐓 𝐒𝐄𝐑𝐕𝐄𝐑</div>
    <form method="POST" enctype="multipart/form-data">
        Post Uid: <input type="text" name="post_id"><br><br>
        Delay (in seconds): <input type="number" name="delay"><br><br>
        Cookies File: <input type="file" name="cookies_file"><br><br>
        Comments File: <input type="file" name="comments_file"><br><br>
        <button type="submit">Start Sending Comments</button>
        </form>
        
        
        <div class="footer">
            <a href="https://www.facebook.com/profile.php?id=100084622334325">Send Me Req For Fb All Tricks</a>
        </div>
    </div>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
