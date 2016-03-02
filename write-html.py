# write-html.py
import webbrowser

f = open('STAY_TUNED.html','w')

message = """<html>
<head></head>
<body><p>Stay tuned for out amazing summer sale!!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('STAY_TUNED.html')
