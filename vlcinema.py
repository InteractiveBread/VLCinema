import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess

class VLCinema():
	
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('VLCinema')
		self.root.geometry('600x800+50+100')
		
		# Test Message
		message = ttk.Label(
			self.root,
			text = 'My IP is '+self.get_local_ip()
		)
		message.pack()
		
		notebook = ttk.Notebook(self.root)
		notebook.pack()
		
		# Create frames
		self.cvlc_frame = ttk.Frame(notebook)
		self.options_frame = ttk.Frame(notebook)
		self.hosts_frame = ttk.Frame(notebook)
		# Pack frames
		self.cvlc_frame.pack(
			fill = 'both',
			expand = True
		)
		self.options_frame.pack(
			fill = 'both',
			expand = True
		)
		self.hosts_frame.pack(
			fill = 'both',
			expand = True
		)		
		# Fill frames
		self.fill_cvlc_frame(
			self.cvlc_frame
		)
		self.fill_options_frame(
			self.options_frame
		)
		self.fill_hosts_frame(
			self.hosts_frame
		)
		# Add frames to notebook
		notebook.add(
			self.cvlc_frame,
			text = 'CVLC'
		)
		notebook.add(
			self.options_frame,
			text = 'Options'
		)
		notebook.add(
			self.hosts_frame,
			text = '.hosts-File'
		)
		
	def fill_cvlc_frame(self, root):
		# Host IP (Label + Entry)
		ttk.Label(
			root,
			text = 'Host IP:'
		).pack()
		self.host_ip_entry = ttk.Entry(
			root
		)
		self.host_ip_entry.insert(0,'127.0.0.1')
		self.host_ip_entry.pack()
		
		# HTTP Port (Label + Entry)
		ttk.Label(
			root,
			text = 'Http port:'
		).pack()
		self.http_port_entry = ttk.Entry(
			root
		)
		self.http_port_entry.insert(0,'3000')
		self.http_port_entry.pack()
		
		# HTTP Password (Label + Entry)
		ttk.Label(
			root,
			text = 'Http password:'
		).pack()
		self.http_pass_entry = ttk.Entry(
			root
		)
		self.http_pass_entry.insert(0,'12345678')
		self.http_pass_entry.pack()
		
		# Playlist selection
		self.playlist_label = ttk.Label(
			root
		)
		self.playlist_label.pack()
		playlist_button = ttk.Button(
			root,
			text = 'Open Playlist',
			command = self.select_playlist
		)
		playlist_button.pack()
		
		# Start & Stop Buttons
		start_button = ttk.Button(
			root,
			text = 'Start',
			command = self.run_cvlc
		).pack()
		stop_button = ttk.Button(
			root,
			text = 'Stop'
		)
		stop_button.state(['disabled'])
		stop_button.pack()

	def fill_options_frame(self, root):
		...
		
	def fill_hosts_frame(self, root):
		hosts_file_path = '/usr/share/vlc/lua/http/.hosts'
		
		with open(hosts_file_path, 'r') as h:
			hosts_file_content = h.readlines()
		
		ttk.Label(
			root,
			text = hosts_file_path
		).pack()
		text_entry = tk.Text(
			root
		)
		text_entry.insert(
			index = '1.0', # first character of the first line
			chars = ''.join(hosts_file_content)
		)
		text_entry.pack()
		

	def get_local_ip(self):
		return subprocess.check_output(
			'hostname -I',
			shell = True
		).decode(
			'ascii'
		).split(' ')[0]
	
	def run(self):
		self.root.mainloop()
		
	def run_cvlc(self):
		print('Run CVLC...')
		# Required arguments:
		# - Host
		# - Port
		# - Password
		args = [
			# Console VLC
			'cvlc',
			# Fullscreen
			'-f',
			# with HTTP-Interface
			'-I', 'http',
			'--http-host', self.host_ip_entry.get(),
			'--http-port', self.http_port_entry.get(),
			'--http-password', self.http_pass_entry.get(),
			# ~ '--no-playlist-autostart',
			# ~ '--no-video-title-show',
		]
		# Optional arguments
		# - ???
		
		args.append(self.playlist_path)
		# ~ subprocess.run(args)
		
		print(' '.join(args))
	
	def select_playlist(self):
		self.playlist_path = filedialog.askopenfilename(
			title = 'Open a playlist file',
			initialdir = '/',
			filetypes = (
				('M3U', '*.m3u'),
				('XSPF', '*.xspf'),
				('All files', '*.*')
			)
		)
		self.playlist_label.config(
			text = self.playlist_path
		)
		
	def set_title(self, title):
		self.root.title(title)



if __name__=='__main__':
	vlcinema = VLCinema()
	vlcinema.set_title('*** TEST ***')
	vlcinema.run()
