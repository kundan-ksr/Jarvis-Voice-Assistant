# Jarvis-Voice-Assistant

The provided Python script creates a voice-controlled virtual assistant named Jarvis. It utilizes various libraries for speech recognition, text-to-speech conversion, and integrates with external services for tasks such as searching Wikipedia, opening websites, playing music, checking the time, and sending emails.

Key Features:

Speech Recognition and Text-to-Speech:

The script employs the speech_recognition library to recognize voice commands from the user through a microphone.
It uses the pyttsx3 library for text-to-speech conversion, allowing Jarvis to respond audibly to user queries.
Greetings:

Jarvis greets the user based on the current time of day (morning, afternoon, or evening) when the script is initiated.
Task Execution:

The script listens for user commands in a continuous loop.
It recognizes specific commands such as searching Wikipedia, opening YouTube and Google, playing music, checking the time, opening a code editor (Visual Studio Code), and sending emails.
Wikipedia Search:

If the user requests information from Wikipedia, Jarvis searches and reads a summary of the relevant topic.
Web Browsing:

Jarvis can open YouTube and Google in a web browser based on user commands.
Music Playback:

Upon request, Jarvis plays music from a predefined directory on the system.
Time Announcement:

Jarvis tells the current time when prompted by the user.
Code Editor:

It can open Visual Studio Code, assuming the appropriate path is provided.
Email Sending:

Jarvis prompts the user for email content and recipient information, attempting to send an email using a specified Gmail account.
Note:

The script should be used cautiously as it contains sensitive information such as email and password. Secure methods, such as environment variables, should be considered for storing such data.
Usage:

Run the script, and Jarvis will greet the user, waiting for voice commands.
The user can interact with Jarvis by asking questions or giving specific commands.
Improvement Suggestions:

Enhance exception handling to provide more informative error messages.
Consider securing sensitive information using best practices.
Further expand functionality based on user requirements
