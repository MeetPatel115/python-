# # print("hello worl")

# import pandas

# print("pandas has been installed ")


# for i in range(11):
#     print(f"5  X  {i} = {5*i}")
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this")
engine.runAndWait()

print("task completed")