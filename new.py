import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
	message = input("Enter your message to the bot: ")
	if message == "quit":
		exit()
	elif message == "save":
		kernel.saveBrain("bot_brain.brn")
	else:
		bot_response = kernel.respond(message)
		print(bot_response)