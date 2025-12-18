
"""
Test script for Image Steganography
Creates a simple test image and performs encode/decode operations.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from PIL import Image
import numpy as np
from modules.image_steg import ImageSteganography

def create_test_image(filename="test_cover.png", size=(400, 300)):
    """Create a simple test image."""
    
    img_array = np.zeros((size[1], size[0], 3), dtype=np.uint8)
    
    for i in range(size[1]):
        for j in range(size[0]):
            img_array[i, j] = [
                int(255 * i / size[1]),  
                int(255 * j / size[0]),  
                128  
            ]
    
    img = Image.fromarray(img_array)
    img.save(filename)
    print(f"[OK] Test image created: {filename}")
    return filename

def test_image_steganography():
    """Test image steganography encoding and decoding."""
    print("\n" + "=" * 60)
    print("IMAGE STEGANOGRAPHY TEST")
    print("=" * 60)
    
    steg = ImageSteganography()
    
    cover_image = create_test_image()
    
    secret_message = "This is a secret message hidden in the image using LSB steganography!"
    print(f"\nSecret Message: '{secret_message}'")
    print(f"Length: {len(secret_message)} characters")
    
    capacity = steg.calculate_capacity(cover_image)
    print(f"\nImage Capacity: {capacity} bytes ({capacity} characters)")
    
    print("\nEncoding message...")
    stego_image = "test_stego.png"
    success, msg = steg.encode_image(cover_image, secret_message, stego_image)
    
    if success:
        print(f"[OK] {msg}")
    else:
        print(f"[FAIL] {msg}")
        return False
    
    print("\nComparing original and stego images...")
    comparison = steg.compare_images(cover_image, stego_image)
    print(f"Max Difference: {comparison['max_difference']} (LSB changes only)")
    print(f"Mean Difference: {comparison['mean_difference']:.6f}")
    print(f"Modified Pixels: {comparison['modified_pixels']} / {comparison['total_pixels']}")
    print(f"Modification: {comparison['modification_percentage']:.4f}%")
    
    print("\nDecoding message from stego-image...")
    success, decoded_message = steg.decode_image(stego_image)
    
    if success:
        print(f"[OK] Decoded successfully!")
        print(f"Decoded Message: '{decoded_message}'")
        
        if decoded_message == secret_message:
            print("\n[SUCCESS] Messages match perfectly!")
            return True
        else:
            print("\n[FAIL] Messages do not match")
            print(f"Expected: '{secret_message}'")
            print(f"Got: '{decoded_message}'")
            return False
    else:
        print(f"[FAIL] Decoding failed: {decoded_message}")
        return False

if __name__ == "__main__":
    try:
        success = test_image_steganography()
        print("\n" + "=" * 60)
        if success:
            print("[SUCCESS] ALL TESTS PASSED")
        else:
            print("[FAIL] TESTS FAILED")
        print("=" * 60 + "\n")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}\n")
        import traceback
        traceback.print_exc()
