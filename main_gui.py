import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.image_steg import ImageSteganography
from modules.audio_steg import AudioSteganography
from utils.helpers import FileHelper, EncryptionHelper

class SteganographyGUI:
    
    
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Analyzer")
        self.root.geometry("900x700")
        
        self.image_steg = ImageSteganography()
        self.audio_steg = AudioSteganography()
        self.encryption = EncryptionHelper()
        self.file_helper = FileHelper()
        
        self.cover_file = None
        self.stego_file = None
        self.use_encryption = tk.BooleanVar(value=False)
        
        self.create_menu()
        self.create_notebook()
        
        self.status_var = tk.StringVar(value="Ready")
        self.create_status_bar()
    
    def create_menu(self):
        """Create menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Usage Guide", command=self.show_usage)
    
    def create_notebook(self):
        """Create tabbed interface."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.image_tab = ttk.Frame(self.notebook)
        self.audio_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.image_tab, text="Image Steganography")
        self.notebook.add(self.audio_tab, text="Audio Steganography")
        
        self.build_image_tab()
        self.build_audio_tab()
    
    def create_status_bar(self):
        """Create status bar at bottom."""
        status_frame = ttk.Frame(self.root)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        ttk.Label(status_frame, textvariable=self.status_var, relief=tk.SUNKEN).pack(
            side=tk.LEFT, fill=tk.X, expand=True
        )
    
    def build_image_tab(self):
        """Build image steganography tab."""
        
        file_frame = ttk.LabelFrame(self.image_tab, text="File Selection", padding=10)
        file_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(file_frame, text="Select Cover Image (PNG)", 
                  command=lambda: self.select_file("image", "cover")).pack(side=tk.LEFT, padx=5)
        self.image_cover_label = ttk.Label(file_frame, text="No file selected")
        self.image_cover_label.pack(side=tk.LEFT, padx=5)
        
        msg_frame = ttk.LabelFrame(self.image_tab, text="Secret Message", padding=10)
        msg_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.image_message_text = scrolledtext.ScrolledText(msg_frame, height=8)
        self.image_message_text.pack(fill=tk.BOTH, expand=True)
        
        ttk.Checkbutton(msg_frame, text="Encrypt message (optional)", 
                       variable=self.use_encryption).pack(anchor=tk.W, pady=5)
        
        ttk.Label(msg_frame, text="Password (if encryption enabled):").pack(anchor=tk.W)
        self.image_password_entry = ttk.Entry(msg_frame, show="*", width=30)
        self.image_password_entry.pack(anchor=tk.W, pady=2)
        
        self.image_capacity_label = ttk.Label(msg_frame, text="Capacity: Select an image first")
        self.image_capacity_label.pack(anchor=tk.W, pady=5)
        
        btn_frame = ttk.Frame(self.image_tab)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Encode Message", 
                  command=self.encode_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Decode Message", 
                  command=self.decode_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear", 
                  command=self.clear_image_tab).pack(side=tk.LEFT, padx=5)
        
        output_frame = ttk.LabelFrame(self.image_tab, text="Output", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.image_output_text = scrolledtext.ScrolledText(output_frame, height=6)
        self.image_output_text.pack(fill=tk.BOTH, expand=True)
    
    def build_audio_tab(self):
        """Build audio steganography tab."""
        
        file_frame = ttk.LabelFrame(self.audio_tab, text="File Selection", padding=10)
        file_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(file_frame, text="Select Audio File (WAV)", 
                  command=lambda: self.select_file("audio", "cover")).pack(side=tk.LEFT, padx=5)
        self.audio_cover_label = ttk.Label(file_frame, text="No file selected")
        self.audio_cover_label.pack(side=tk.LEFT, padx=5)
        
        msg_frame = ttk.LabelFrame(self.audio_tab, text="Secret Message", padding=10)
        msg_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.audio_message_text = scrolledtext.ScrolledText(msg_frame, height=8)
        self.audio_message_text.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(msg_frame, text="Embedding Key (optional - for position randomization):").pack(anchor=tk.W, pady=5)
        self.audio_key_entry = ttk.Entry(msg_frame, width=30)
        self.audio_key_entry.pack(anchor=tk.W, pady=2)
        
        self.audio_capacity_label = ttk.Label(msg_frame, text="Capacity: Select an audio file first")
        self.audio_capacity_label.pack(anchor=tk.W, pady=5)
        
        btn_frame = ttk.Frame(self.audio_tab)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Encode Message", 
                  command=self.encode_audio).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Decode Message", 
                  command=self.decode_audio).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear", 
                  command=self.clear_audio_tab).pack(side=tk.LEFT, padx=5)
        
        output_frame = ttk.LabelFrame(self.audio_tab, text="Output", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.audio_output_text = scrolledtext.ScrolledText(output_frame, height=6)
        self.audio_output_text.pack(fill=tk.BOTH, expand=True)
    
    def select_file(self, file_type, mode):
        """Select file dialog."""
        filetypes = {
            "image": [("PNG files", "*.png"), ("All files", "*.*")],
            "audio": [("WAV files", "*.wav"), ("All files", "*.*")]
        }
        
        filename = filedialog.askopenfilename(
            title=f"Select {file_type} file",
            filetypes=filetypes.get(file_type, [("All files", "*.*")])
        )
        
        if filename:
            self.cover_file = filename
            
            if file_type == "image":
                self.image_cover_label.config(text=os.path.basename(filename))
                capacity = self.image_steg.calculate_capacity(filename)
                self.image_capacity_label.config(text=f"Capacity: {capacity} bytes ({capacity} characters)")
            elif file_type == "audio":
                self.audio_cover_label.config(text=os.path.basename(filename))
                capacity = self.audio_steg.calculate_capacity(filename)
                self.audio_capacity_label.config(text=f"Capacity: {capacity} bytes ({capacity} characters)")
    
    def encode_image(self):
        """Encode message in image."""
        if not self.cover_file:
            messagebox.showerror("Error", "Please select a cover image first")
            return
        
        message = self.image_message_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Error", "Please enter a message to hide")
            return
        
        if self.use_encryption.get():
            password = self.image_password_entry.get()
            if not password:
                messagebox.showerror("Error", "Please enter a password for encryption")
                return
            try:
                message = self.encryption.encrypt_message(message, password)
                self.image_output_text.insert(tk.END, "[INFO] Message encrypted before embedding\n")
            except Exception as e:
                messagebox.showerror("Error", f"Encryption failed: {str(e)}")
                return
        
        output_file = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if not output_file:
            return
        
        self.update_status("Encoding image...")
        self.image_output_text.delete("1.0", tk.END)
        
        threading.Thread(target=self._encode_image_thread, args=(message, output_file), daemon=True).start()
    
    def _encode_image_thread(self, message, output_file):
        """Thread function for encoding image."""
        success, result = self.image_steg.encode_image(self.cover_file, message, output_file)
        
        def update_ui():
            self.image_output_text.insert(tk.END, result + "\n")
            if success:
                messagebox.showinfo("Success", "Image encoded successfully!")
            else:
                messagebox.showerror("Error", result)
            self.update_status("Ready")
        
        self.root.after(0, update_ui)
    
    def decode_image(self):
        """Decode message from image."""
        filename = filedialog.askopenfilename(
            title="Select stego-image",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        self.update_status("Decoding image...")
        self.image_output_text.delete("1.0", tk.END)
        
        success, message = self.image_steg.decode_image(filename)
        
        if success:
            
            if self.use_encryption.get():
                password = self.image_password_entry.get()
                if password:
                    try:
                        message = self.encryption.decrypt_message(message, password)
                        self.image_output_text.insert(tk.END, "[INFO] Message decrypted\n\n")
                    except Exception as e:
                        self.image_output_text.insert(tk.END, f"[WARNING] Decryption failed: {str(e)}\n")
                        self.image_output_text.insert(tk.END, "Showing encrypted message:\n\n")
            
            self.image_output_text.insert(tk.END, f"Decoded Message:\n{message}\n")
            messagebox.showinfo("Success", "Message decoded successfully!")
        else:
            self.image_output_text.insert(tk.END, f"Error: {message}\n")
            messagebox.showerror("Error", message)
        
        self.update_status("Ready")
    
    def encode_audio(self):
        """Encode message in audio."""
        if not self.cover_file:
            messagebox.showerror("Error", "Please select a cover audio file first")
            return
        
        message = self.audio_message_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Error", "Please enter a message to hide")
            return
        
        key = self.audio_key_entry.get() or None
        
        output_file = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
        )
        
        if not output_file:
            return
        
        self.update_status("Encoding audio...")
        self.audio_output_text.delete("1.0", tk.END)
        
        threading.Thread(target=self._encode_audio_thread, args=(message, output_file, key), daemon=True).start()
    
    def _encode_audio_thread(self, message, output_file, key):
        """Thread function for encoding audio."""
        success, result = self.audio_steg.encode_audio(self.cover_file, message, output_file, key)
        
        def update_ui():
            self.audio_output_text.insert(tk.END, result + "\n")
            if success:
                messagebox.showinfo("Success", "Audio encoded successfully!")
            else:
                messagebox.showerror("Error", result)
            self.update_status("Ready")
        
        self.root.after(0, update_ui)
    
    def decode_audio(self):
        """Decode message from audio."""
        filename = filedialog.askopenfilename(
            title="Select stego-audio",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        key = self.audio_key_entry.get() or None
        
        self.update_status("Decoding audio...")
        self.audio_output_text.delete("1.0", tk.END)
        
        success, message = self.audio_steg.decode_audio(filename, key)
        
        if success:
            self.audio_output_text.insert(tk.END, f"Decoded Message:\n{message}\n")
            messagebox.showinfo("Success", "Message decoded successfully!")
        else:
            self.audio_output_text.insert(tk.END, f"Error: {message}\n")
            messagebox.showerror("Error", message)
        
        self.update_status("Ready")
    
    def clear_image_tab(self):
        """Clear image tab fields."""
        self.image_message_text.delete("1.0", tk.END)
        self.image_output_text.delete("1.0", tk.END)
        self.image_password_entry.delete(0, tk.END)
        self.cover_file = None
        self.image_cover_label.config(text="No file selected")
        self.image_capacity_label.config(text="Capacity: Select an image first")
    
    def clear_audio_tab(self):
        """Clear audio tab fields."""
        self.audio_message_text.delete("1.0", tk.END)
        self.audio_output_text.delete("1.0", tk.END)
        self.audio_key_entry.delete(0, tk.END)
        self.cover_file = None
        self.audio_cover_label.config(text="No file selected")
        self.audio_capacity_label.config(text="Capacity: Select an audio file first")
    
    def update_status(self, message):
        """Update status bar."""
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def show_about(self):
        """Show about dialog."""
        messagebox.showinfo(
            "About",
            "Steganography Analyzer v1.0\n\n"
            "A comprehensive steganography application for hiding messages in:\n"
            "• Images (PNG) using LSB substitution\n"
            "• Audio files (WAV) using LSB with optional key-based embedding\n\n"
            "Created as a demonstration of LSB steganography techniques."
        )
    
    def show_usage(self):
        """Show usage guide."""
        usage_text = """
USAGE GUIDE

IMAGE STEGANOGRAPHY:
1. Select a PNG cover image
2. Enter your secret message
3. Optionally enable encryption with a password
4. Click 'Encode Message' and save the stego-image
5. To decode: Click 'Decode Message' and select a stego-image

AUDIO STEGANOGRAPHY:
1. Select a WAV audio file
2. Enter your secret message
3. Optionally enter an embedding key for position randomization
4. Click 'Encode Message' and save the stego-audio
5. To decode: Use the same key if one was used during encoding

TIPS:
• PNG is recommended for images (lossless)
• Larger files have more capacity
• Encryption adds security but increases message size
        """
        
        top = tk.Toplevel(self.root)
        top.title("Usage Guide")
        top.geometry("600x500")
        
        text = scrolledtext.ScrolledText(top, wrap=tk.WORD)
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text.insert("1.0", usage_text)
        text.config(state=tk.DISABLED)
        
        ttk.Button(top, text="Close", command=top.destroy).pack(pady=5)

def main():
    """Main entry point."""
    root = tk.Tk()
    app = SteganographyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
