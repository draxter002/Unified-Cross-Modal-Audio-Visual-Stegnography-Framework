
import os
from typing import Optional
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64

class EncryptionHelper:
   
    def __init__(self):
        self.block_size = AES.block_size
    
    def _derive_key(self, password: str) -> bytes:
        
        return hashlib.sha256(password.encode()).digest()
    
    def encrypt_message(self, message: str, password: str) -> str:
        
        try:
            key = self._derive_key(password)
            cipher = AES.new(key, AES.MODE_CBC)
            
            padded_message = pad(message.encode(), self.block_size)
            
            ciphertext = cipher.encrypt(padded_message)
            
            encrypted_data = cipher.iv + ciphertext
            return base64.b64encode(encrypted_data).decode()
        
        except Exception as e:
            raise Exception(f"Encryption failed: {str(e)}")
    
    def decrypt_message(self, encrypted_message: str, password: str) -> str:
       
        try:
            key = self._derive_key(password)
            
            encrypted_data = base64.b64decode(encrypted_message)
            
            iv = encrypted_data[:self.block_size]
            ciphertext = encrypted_data[self.block_size:]
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            padded_message = cipher.decrypt(ciphertext)
            
            message = unpad(padded_message, self.block_size)
            return message.decode()
        
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}")

class BinaryConverter:
  
    @staticmethod
    def text_to_binary(text: str) -> str:
      
        return ''.join(format(ord(char), '08b') for char in text)
    
    @staticmethod
    def binary_to_text(binary: str) -> str:
     
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                try:
                    text += chr(int(byte, 2))
                except ValueError:
                    pass
        return text
    
    @staticmethod
    def bytes_to_binary(data: bytes) -> str:
      
        return ''.join(format(byte, '08b') for byte in data)
    
    @staticmethod
    def binary_to_bytes(binary: str) -> bytes:
      
        byte_array = bytearray()
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))
        return bytes(byte_array)

class FileHelper:
   
    @staticmethod
    def get_file_size(file_path: str) -> int:
        
        return os.path.getsize(file_path)
    
    @staticmethod
    def get_file_extension(file_path: str) -> str:
       
        return os.path.splitext(file_path)[1].lower()
    
    @staticmethod
    def validate_image_file(file_path: str) -> bool:
      
        valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
        return FileHelper.get_file_extension(file_path) in valid_extensions
    
    @staticmethod
    def validate_audio_file(file_path: str) -> bool:
        
        valid_extensions = ['.wav']
        return FileHelper.get_file_extension(file_path) in valid_extensions
    
    @staticmethod
    def validate_video_file(file_path: str) -> bool:
       
        valid_extensions = ['.mp4', '.avi', '.mov', '.mkv']
        return FileHelper.get_file_extension(file_path) in valid_extensions
    
    @staticmethod
    def format_file_size(size_bytes: int) -> str:
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"

class CapacityCalculator:
    
    @staticmethod
    def image_capacity(width: int, height: int, channels: int = 3) -> int:
        
        
        total_bits = width * height * channels
        return total_bits // 8
    
    @staticmethod
    def audio_capacity(sample_count: int) -> int:
        
        
        return sample_count // 8
    
    @staticmethod
    def video_capacity(frame_count: int, frame_width: int, frame_height: int,
                      audio_samples: int) -> dict:
        
        frame_capacity = CapacityCalculator.image_capacity(frame_width, frame_height)
        total_frame_capacity = frame_capacity * frame_count
        audio_capacity = CapacityCalculator.audio_capacity(audio_samples)
        
        return {
            'frames_capacity_bytes': total_frame_capacity,
            'audio_capacity_bytes': audio_capacity,
            'total_capacity_bytes': total_frame_capacity + audio_capacity,
            'frames_capacity_readable': FileHelper.format_file_size(total_frame_capacity),
            'audio_capacity_readable': FileHelper.format_file_size(audio_capacity),
            'total_capacity_readable': FileHelper.format_file_size(total_frame_capacity + audio_capacity)
        }

def validate_message_size(message: str, capacity: int) -> tuple:
   
    message_size = len(message.encode('utf-8'))
    
    if message_size <= capacity:
        return True, f"Message size: {message_size} bytes, Capacity: {capacity} bytes"
    else:
        return False, f"Message too large! Message: {message_size} bytes, Capacity: {capacity} bytes"

def create_output_filename(input_path: str, prefix: str = "stego_") -> str:
   
    directory = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{prefix}{name}{ext}"
    return os.path.join(directory, output_filename)

encryption_helper = EncryptionHelper()
binary_converter = BinaryConverter()
file_helper = FileHelper()
capacity_calculator = CapacityCalculator()

if __name__ == "__main__":
    print("Steganography Utilities")
    print("=" * 50)
    
    enc = EncryptionHelper()
    encrypted = enc.encrypt_message("Test message", "password123")
    print(f"Encrypted: {encrypted}")
    decrypted = enc.decrypt_message(encrypted, "password123")
    print(f"Decrypted: {decrypted}")
    
    binary = BinaryConverter.text_to_binary("Hello")
    print(f"Binary: {binary}")
    text = BinaryConverter.binary_to_text(binary)
    print(f"Text: {text}")
