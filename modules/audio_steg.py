

import wave
import numpy as np
from typing import Tuple, Optional
import hashlib

class AudioSteganography:
   
    
    def __init__(self):
        self.delimiter = "<<<END>>>"
    
    def calculate_capacity(self, audio_path: str) -> int:
       
        try:
            with wave.open(audio_path, 'rb') as audio:
                n_frames = audio.getnframes()
                n_channels = audio.getnchannels()
                
                total_samples = n_frames * n_channels
                
                capacity = total_samples // 8
                delimiter_bytes = len(self.delimiter)
                return capacity - delimiter_bytes - 10  
        except Exception as e:
            return 0
    
    def _text_to_binary(self, text: str) -> str:
        
        binary = ''.join(format(ord(char), '08b') for char in text)
        return binary
    
    def _binary_to_text(self, binary: str) -> str:
       
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                text += chr(int(byte, 2))
        return text
    
    def _generate_positions(self, key: str, total_samples: int, message_length: int) -> list:
        
        
        seed = int(hashlib.sha256(key.encode()).hexdigest(), 16) % (2**32)
        np.random.seed(seed)
        
        positions = np.random.choice(total_samples, size=message_length, replace=False)
        return positions.tolist()
    
    def encode_audio(self, cover_audio_path: str, secret_message: str,
                     output_path: str, key: Optional[str] = None) -> Tuple[bool, str]:
        
        try:
            
            with wave.open(cover_audio_path, 'rb') as audio:
                params = audio.getparams()
                n_frames = params.nframes
                n_channels = params.nchannels
                sampwidth = params.sampwidth
                framerate = params.framerate
                
                frames = audio.readframes(n_frames)
            
            audio_data = np.frombuffer(frames, dtype=np.int16)
            
            max_capacity = self.calculate_capacity(cover_audio_path)
            message_with_delimiter = secret_message + self.delimiter
            
            if len(message_with_delimiter) > max_capacity:
                return False, f"Message too long! Max capacity: {max_capacity} bytes, Message: {len(message_with_delimiter)} bytes"
            
            binary_message = self._text_to_binary(message_with_delimiter)
            message_length = len(binary_message)
            
            if key:
                positions = self._generate_positions(key, len(audio_data), message_length)
            else:
                positions = list(range(message_length))  
            
            modified_audio = audio_data.copy()
            for i, pos in enumerate(positions):
                if i >= message_length:
                    break
                
                sample = int(modified_audio[pos])
                
                modified_audio[pos] = (sample & ~1) | int(binary_message[i])
            
            with wave.open(output_path, 'wb') as stego_audio:
                stego_audio.setparams(params)
                stego_audio.writeframes(modified_audio.tobytes())
            
            return True, f"Message encoded successfully! Stego-audio saved to {output_path}"
        
        except Exception as e:
            return False, f"Error encoding audio: {str(e)}"
    
    def decode_audio(self, stego_audio_path: str, key: Optional[str] = None) -> Tuple[bool, str]:
      
        try:
            
            with wave.open(stego_audio_path, 'rb') as audio:
                params = audio.getparams()
                n_frames = params.nframes
                frames = audio.readframes(n_frames)
            
            audio_data = np.frombuffer(frames, dtype=np.int16)
            
            max_bits = len(audio_data)
            
            initial_extract_size = min(max_bits, 10000 * 8)  
            
            if key:
                
                positions = self._generate_positions(key, len(audio_data), initial_extract_size)
            else:
                
                positions = list(range(initial_extract_size))
            
            binary_data = ""
            for pos in positions:
                binary_data += str(int(audio_data[pos]) & 1)
            
            extracted_text = self._binary_to_text(binary_data)
            
            if self.delimiter in extracted_text:
                message = extracted_text.split(self.delimiter)[0]
                return True, message
            else:
                return False, "No hidden message found or delimiter missing (key might be incorrect)"
        
        except Exception as e:
            return False, f"Error decoding audio: {str(e)}"
    
    def compare_audio(self, original_path: str, stego_path: str) -> dict:
        
        try:
            
            with wave.open(original_path, 'rb') as audio:
                frames1 = audio.readframes(audio.getnframes())
            audio_data1 = np.frombuffer(frames1, dtype=np.int16)
            
            with wave.open(stego_path, 'rb') as audio:
                frames2 = audio.readframes(audio.getnframes())
            audio_data2 = np.frombuffer(frames2, dtype=np.int16)
            
            diff = np.abs(audio_data1.astype(int) - audio_data2.astype(int))
            max_diff = np.max(diff)
            mean_diff = np.mean(diff)
            
            modified_samples = np.count_nonzero(diff)
            total_samples = len(audio_data1)
            
            return {
                'max_difference': int(max_diff),
                'mean_difference': float(mean_diff),
                'modified_samples': int(modified_samples),
                'total_samples': int(total_samples),
                'modification_percentage': float(modified_samples / total_samples * 100)
            }
        
        except Exception as e:
            return {'error': str(e)}
    
    def get_audio_info(self, audio_path: str) -> dict:
      
        try:
            with wave.open(audio_path, 'rb') as audio:
                params = audio.getparams()
                return {
                    'channels': params.nchannels,
                    'sample_width': params.sampwidth,
                    'framerate': params.framerate,
                    'n_frames': params.nframes,
                    'duration_seconds': params.nframes / params.framerate
                }
        except Exception as e:
            return {'error': str(e)}

def encode_audio(cover_audio_path: str, secret_message: str,
                 output_path: str, key: Optional[str] = None) -> Tuple[bool, str]:
    
    steg = AudioSteganography()
    return steg.encode_audio(cover_audio_path, secret_message, output_path, key)

def decode_audio(stego_audio_path: str, key: Optional[str] = None) -> Tuple[bool, str]:
   
    steg = AudioSteganography()
    return steg.decode_audio(stego_audio_path, key)

def get_audio_capacity(audio_path: str) -> int:
    
    steg = AudioSteganography()
    return steg.calculate_capacity(audio_path)

if __name__ == "__main__":
    
    print("Audio Steganography Module")
    print("=" * 50)
