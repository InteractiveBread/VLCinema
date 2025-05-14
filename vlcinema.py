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
		
		# Host IP (Label + Entry)
		ttk.Label(
			self.root,
			text = 'Host IP:'
		).pack()
		self.host_ip_entry = ttk.Entry(
			self.root
		)
		self.host_ip_entry.insert(0,'127.0.0.1')
		self.host_ip_entry.pack()
		
		# HTTP Port (Label + Entry)
		ttk.Label(
			self.root,
			text = 'Http port:'
		).pack()
		self.http_port_entry = ttk.Entry(
			self.root
		)
		self.http_port_entry.insert(0,'3000')
		self.http_port_entry.pack()
		
		# HTTP Password (Label + Entry)
		ttk.Label(
			self.root,
			text = 'Http password:'
		).pack()
		self.http_pass_entry = ttk.Entry(
			self.root
		)
		self.http_pass_entry.insert(0,'12345678')
		self.http_pass_entry.pack()
		
		# Playlist selection
		self.playlist_label = ttk.Label(
			self.root
		)
		self.playlist_label.pack()
		playlist_button = ttk.Button(
			self.root,
			text = 'Open Playlist',
			command = self.select_playlist
		)
		playlist_button.pack()
		
		# Start & Stop Buttons
		start_button = ttk.Button(
			self.root,
			text = 'Start',
			command = self.run_cvlc
		).pack()
		stop_button = ttk.Button(
			self.root,
			text = 'Stop'
		)
		stop_button.state(['disabled'])
		stop_button.pack()

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
