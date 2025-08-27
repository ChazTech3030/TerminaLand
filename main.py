import os

learnt_commands = {
	"help": {
		"description ":"Gives an overview of how to play this game or how to utilise a command",
		"linux":"help is used to find out more information about a command",
		"usage":"`help` or `help <command>`"
	},
	"commands": {
		"description ":"Lists all commands available to you",
		"linux":"Not a Linux command",
		"usage":"`commands`"
	}
}
unlearnt_commands = {
	"ls": {
		"description":"Look at what is around you",
		"linux":"ls (LiSt) lists the files and folders in the specified location",
		"usage":"`ls` or `ls <location>`"
	},
	"cd": {
		"description":"Move to the current location",
		"linux":"cd (Change Directory) changes the directory to the specified location",
		"usage":"`cd <location>`"
	},
	"cat": {
		"description":"Inspect an object",
		"linux":"cat (conCATenante) reads one or more files prints the content to the terminal",
		"usage":"`cat <object>`"
	},
	"mkdir": {
		"description":"Make a new location",
		"linux":"mkdir (MaKe DIRectory) makes a new directory with the supplied name",
		"usage":"`mkdir <location>`"
	},
	"touch": {
		"description":"Make a new object",
		"linux":"touch updates an object's meta data. If the object doesn't exist, one will be made",
		"usage":"`touch <object>`"
	},
	"nano": {
		"description":"Edit an object",
		"linux":"nano is a Command Line Interface text editor",
		"usage":"`nano <object>`"
	},
	"rm": {
		"description":"Remove an object",
		"linux":"rm (ReMove) deletes an object",
		"usage":"`rm <object>`"
	}
}
width_and_height = os.get_terminal_size()
screen_width = width_and_height[0]
screen_height = width_and_height[1]
screen_height_mod = 0
working_height = screen_height - 5
working_width = screen_width - 4

def start_up():
	print("\n"*screen_height)

def welcome_screen():
	lines = []
	file = open("splash_screen.txt", encoding="utf8")
	for line in file:
		lines.append(line)
	file.close()
	game_screen(lines,"sc", True)

def print_line_break():
	line_break = "-" * (screen_width - 2)
	print(f"+{line_break}+")

def print_blank_line():
	blank_line = " " * (screen_width - 2)
	print(f"|{blank_line}|")

def print_prompt(root=False):
	if root:
		user_input = input("| # ")
	else:
		user_input = input("| $ ")
	return user_input

def build_a_line(line, alignment="l"):
	if alignment == "l" or alignment == "r":
		filler = " " * (working_width - len(line) - 4)
		if alignment == "l":
			line = f"{line}{filler}"
		else:
			line = f"{filler}{line}"
	elif alignment == "c":
		filler_width = working_width - len(line) - 4
		if filler_width % 2 == 0:
			fill_left = " " * int(filler_width / 2)
			fill_right = fill_left
		else:
			fill_left = " " * int((filler_width -1) / 2)
			fill_right = fill_left + " "
		line = f"{fill_left}{line}{fill_right}"
	return line

def build_commands_data():
	data = []
	data.append("")
	data.append( build_a_line("----===[ COMMAND LIBRARY ]===----", "c") )
	data.append("")
	for command, details in learnt_commands.items():
		data.append(command)
		for title, description in details.items():
			data.append(f" - {title} : {description}")
	for command, details in unlearnt_commands.items():
		data.append("???")
		for title, description in details.items():
			data.append(" - ???")
	game_screen(data,"l")

def line_breaker(data):
	lines = []
	line_length = len(data)
	no_of_lines = int( line_length / working_width )
	start = 0
	end = working_width
	for i in range(0, no_of_lines):
		l = data[start:end]
		lines.append( l )
		start += working_width
		end += working_width
	lines.append(data[start:])
	return lines

def build_help_data():
	data = []
	data.append("")
	data.append( build_a_line("----===[ HELP ]===----","c") )
	data.append("")
	data.append("")
	lines = []
	file = open("help.txt", encoding="utf8")
	for line in file:
		line = line.replace("\n", " ")
		if len(line) > working_width:
			for l in line_breaker(line):
				data.append(l)
		else:
			data.append(line)
	file.close()
	game_screen(data,"l")

def game_screen(data, alignment="l", welcome=False):
	print_line_break()
	print_blank_line()
	global working_height
	global working_width
	printed_line_count = 0
	if alignment == "l" or alignment == "r":
		for line in data:
			line = line.replace("\n"," ")
			filler = " " * (working_width - len(line))
			if alignment == "l":
				print(f"| {line}{filler} |")
			else:
				print(f"| {filler}{line} |")
			printed_line_count += 1
	elif alignment == "c":
		for line in data:
			line = line.replace("\n"," ")
			if (working_width - len(line)) % 2 == 0:
				fill_left = " " * int((working_width - len(line)) / 2)
				fill_right = fill_left
			else:
				fill_left = " " * int(((working_width - len(line)) - 1) / 2)
				fill_right = fill_left + " "
			print(f"| {fill_left}{line}{fill_right} |")
			printed_line_count += 1
	elif alignment == "sc":
		data_line_count = 0
		for line in data:
			data_line_count += 1
		if (working_height - data_line_count) % 2 == 0:
			half_count = int((working_height - data_line_count) / 2)
		else:
			half_count = int((working_height - data_line_count - 1) / 2)
		while printed_line_count < half_count:
			print_blank_line()
			printed_line_count += 1
		for line in data:
			line = line.replace("\n"," ")
			if (working_width - len(line)) % 2 == 0:
				fill_left = " " * int((working_width - len(line)) / 2)
				fill_right = fill_left
			else:
				fill_left = " " * int(((working_width - len(line)) - 1) / 2)
				fill_right = fill_left + " "
			print(f"| {fill_left}{line}{fill_right} |")
			printed_line_count += 1
	if welcome:
		working_height = working_height - 1
	while printed_line_count <= working_height:
		print_blank_line()
		printed_line_count += 1
	if welcome:
		filler = " " * (working_width - 67)
		print(f"| TO BEGIN YOUR ADVENTURE, USE THE COMMAND 'help' IN THE PROMPT BELOW{filler} |" )
	print_line_break()

def game_loop():
	start_up()
	if (screen_width < 97) or (screen_height < 44):
		print(f"THE GAME SCREEN IS TOO SMALL FOR EFFECTIVE DISPLAY. PLEASE RESIZE YOUR TERMINAL TO AT LEAST:\nWidth:97\nHeight:44\nCurrent Width:{screen_width}\nCurrent Height:{screen_height}")
	else:
		welcome_screen()

		while True:
			command = print_prompt()
			command = command.split(" ")
			if command[0] in dict.keys(learnt_commands):
				if command[0] == "commands":
					build_commands_data()
				elif command[0] == "help":
					build_help_data()
			else:
				if command[0] in unlearnt_commands:
					print("You have not learnt that spell yet!")
				else:
					print("I don't know what that is... check your spelling and try again!")

game_loop()