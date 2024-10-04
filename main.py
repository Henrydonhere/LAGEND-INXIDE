    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝗛𝗘𝗡𝗥𝗬 𝗣𝗢𝗦𝗧 𝗦𝗘𝗥𝗩𝗘𝗥</title>
    <style>
        body {
            background-image: url('https://i.ibb.co/f0JCQMM/Screenshot-20240922-100537-Gallery.jpg');
            background-size: cover;
            font-family: Arial, sans-serif;
            color: yellow;
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
