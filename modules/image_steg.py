

from PIL import Image
import numpy as np
from typing import Tuple, Optional

class ImageSteganography:
   
    
    def __init__(self):
        self.delimiter = "<<<END>>>"  
    
    def calculate_capacity(self, image_path: str) -> int:
       
    
        img = Image.open(image_path)
        width, height = img.size
        
        capacity = (width * height * 3) // 8
        delimiter_bytes = len(self.delimiter)
        return capacity - delimiter_bytes - 10  
    
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
    
    def encode_image(self, cover_image_path: str, secret_message: str, 
                     output_path: str) -> Tuple[bool, str]:
       
        try:
            
            img = Image.open(cover_image_path)
            img = img.convert('RGB')  
            width, height = img.size
            img_array = np.array(img)
            
            max_capacity = self.calculate_capacity(cover_image_path)
            message_with_delimiter = secret_message + self.delimiter
            
            if len(message_with_delimiter) > max_capacity:
                return False, f"Message too long! Max capacity: {max_capacity} bytes, Message: {len(message_with_delimiter)} bytes"
            
            binary_message = self._text_to_binary(message_with_delimiter)
            message_length = len(binary_message)
            
            data_index = 0
            for i in range(height):
                for j in range(width):
                    if data_index >= message_length:
                        break
                    
                    pixel = img_array[i, j]
                    
                    for k in range(3):  
                        if data_index < message_length:
                            
                            pixel[k] = (pixel[k] & 0xFE) | int(binary_message[data_index])
                            data_index += 1
                    
                    img_array[i, j] = pixel
                
                if data_index >= message_length:
                    break
            
            stego_img = Image.fromarray(img_array)
            stego_img.save(output_path, 'PNG')
            
            return True, f"Message encoded successfully! Stego-image saved to {output_path}"
        
        except Exception as e:
            return False, f"Error encoding image: {str(e)}"
    
    def decode_image(self, stego_image_path: str) -> Tuple[bool, str]:
       
        try:
            
            img = Image.open(stego_image_path)
            img = img.convert('RGB')
            width, height = img.size
            img_array = np.array(img)
            
            binary_data = ""
            
            for i in range(height):
                for j in range(width):
                    pixel = img_array[i, j]
                    
                    for k in range(3):  
                        binary_data += str(pixel[k] & 1)
            
            extracted_text = self._binary_to_text(binary_data)
            
            if self.delimiter in extracted_text:
                message = extracted_text.split(self.delimiter)[0]
                return True, message
            else:
                return False, "No hidden message found or delimiter missing"
        
        except Exception as e:
            return False, f"Error decoding image: {str(e)}"
    
    def compare_images(self, original_path: str, stego_path: str) -> dict:
       
        try:
            img1 = np.array(Image.open(original_path).convert('RGB'))
            img2 = np.array(Image.open(stego_path).convert('RGB'))
            
            diff = np.abs(img1.astype(int) - img2.astype(int))
            max_diff = np.max(diff)
            mean_diff = np.mean(diff)
            
            modified_pixels = np.count_nonzero(diff)
            total_pixels = img1.shape[0] * img1.shape[1] * 3
            
            return {
                'max_difference': int(max_diff),
                'mean_difference': float(mean_diff),
                'modified_pixels': int(modified_pixels),
                'total_pixels': int(total_pixels),
                'modification_percentage': float(modified_pixels / total_pixels * 100)
            }
        
        except Exception as e:
            return {'error': str(e)}

def encode_image(cover_image_path: str, secret_message: str, 
                 output_path: str) -> Tuple[bool, str]:
    
    steg = ImageSteganography()
    return steg.encode_image(cover_image_path, secret_message, output_path)

def decode_image(stego_image_path: str) -> Tuple[bool, str]:
  
    steg = ImageSteganography()
    return steg.decode_image(stego_image_path)

def get_image_capacity(image_path: str) -> int:
    
    steg = ImageSteganography()
    return steg.calculate_capacity(image_path)

if __name__ == "__main__":
    
    print("Image Steganography Module")
    print("=" * 50)
    