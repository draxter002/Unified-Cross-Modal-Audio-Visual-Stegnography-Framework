
"""
Test utilities and helper functions.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.helpers import (
    EncryptionHelper,
    BinaryConverter,
    FileHelper,
    CapacityCalculator
)

def test_encryption():
    """Test encryption and decryption."""
    print("\n" + "=" * 60)
    print("ENCRYPTION TEST")
    print("=" * 60)
    
    enc = EncryptionHelper()
    
    message = "This is a secret message!"
    password = "my_secure_password"
    
    print(f"\n Original Message: '{message}'")
    print(f" Password: '{password}'")
    
    print("\n Encrypting...")
    encrypted = enc.encrypt_message(message, password)
    print(f"   Encrypted: {encrypted}")
    
    print("\n Decrypting with correct password...")
    decrypted = enc.decrypt_message(encrypted, password)
    print(f"   Decrypted: '{decrypted}'")
    
    if decrypted == message:
        print("   [OK] Encryption/Decryption successful!")
    else:
        print("   [FAIL] Messages do not match")
        return False
    
    print("\n Decrypting with wrong password (should fail)...")
    try:
        wrong_decrypted = enc.decrypt_message(encrypted, "wrong_password")
        print(f"   [FAIL] UNEXPECTED: Decrypted with wrong password: '{wrong_decrypted}'")
        return False
    except Exception as e:
        print(f"   [OK] Correctly failed: {str(e)}")
    
    return True

def test_binary_conversion():
    """Test binary conversion functions."""
    print("\n" + "=" * 60)
    print("BINARY CONVERSION TEST")
    print("=" * 60)
    
    conv = BinaryConverter()
    
    text = "Hello, World!"
    print(f"\n Original Text: '{text}'")
    
    binary = conv.text_to_binary(text)
    print(f" Binary: {binary[:50]}... ({len(binary)} bits)")
    
    converted_back = conv.binary_to_text(binary)
    print(f" Converted Back: '{converted_back}'")
    
    if converted_back == text:
        print("   [OK] Binary conversion successful!")
    else:
        print("   [FAIL] Conversion failed")
        return False
    
    return True

def test_capacity_calculator():
    """Test capacity calculation functions."""
    print("\n" + "=" * 60)
    print("CAPACITY CALCULATOR TEST")
    print("=" * 60)
    
    calc = CapacityCalculator()
    
    width, height = 1920, 1080
    image_cap = calc.image_capacity(width, height)
    print(f"\n Image ({width}x{height} RGB):")
    print(f"   Capacity: {image_cap} bytes ({image_cap // 1024} KB)")
    
    sample_rate = 44100
    duration = 60  
    samples = sample_rate * duration
    audio_cap = calc.audio_capacity(samples)
    print(f"\n Audio ({sample_rate}Hz, {duration}s):")
    print(f"   Samples: {samples}")
    print(f"   Capacity: {audio_cap} bytes ({audio_cap // 1024} KB)")
    
    fps = 30
    frame_count = fps * duration
    video_cap = calc.video_capacity(frame_count, width, height, samples)
    print(f"\n Video ({width}x{height}, {fps}fps, {duration}s):")
    print(f"   Frames: {frame_count}")
    print(f"   Frame Capacity: {video_cap['frames_capacity_readable']}")
    print(f"   Audio Capacity: {video_cap['audio_capacity_readable']}")
    print(f"   Total Capacity: {video_cap['total_capacity_readable']}")
    
    return True

def test_file_helper():
    """Test file helper functions."""
    print("\n" + "=" * 60)
    print("FILE HELPER TEST")
    print("=" * 60)
    
    helper = FileHelper()
    
    test_cases = [
        ("image.png", "image", True),
        ("photo.jpg", "image", True),
        ("audio.wav", "audio", True),
        ("video.mp4", "video", True),
        ("document.pdf", "image", False),
        ("music.mp3", "audio", False),
    ]
    
    print("\n File Validation Tests:")
    all_passed = True
    
    for filename, file_type, expected in test_cases:
        if file_type == "image":
            result = helper.validate_image_file(filename)
        elif file_type == "audio":
            result = helper.validate_audio_file(filename)
        elif file_type == "video":
            result = helper.validate_video_file(filename)
        
        status = "[OK]" if result == expected else "[FAIL]"
        print(f"   {status} {filename} as {file_type}: {result} (expected {expected})")
        
        if result != expected:
            all_passed = False
    
    print("\\n File Size Formatting:")
    sizes = [100, 1024, 1024*1024, 1024*1024*1024]
    for size in sizes:
        formatted = helper.format_file_size(size)
        print(f"   {size} bytes = {formatted}")
    
    return all_passed

def run_all_tests():
    """Run all utility tests."""
    print("\n" + "=" * 60)
    print("RUNNING ALL UTILITY TESTS")
    print("=" * 60)
    
    tests = [
        ("Encryption", test_encryption),
        ("Binary Conversion", test_binary_conversion),
        ("Capacity Calculator", test_capacity_calculator),
        ("File Helper", test_file_helper),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"\n[FAIL] ERROR in {test_name}: {str(e)}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "[OK] PASSED" if passed else "[FAIL] FAILED"
        print(f"{status}: {test_name}")
    
    all_passed = all(passed for _, passed in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("[OK] ALL TESTS PASSED")
    else:
        print("[FAIL] SOME TESTS FAILED")
    print("=" * 60 + "\n")
    
    return all_passed

if __name__ == "__main__":
    run_all_tests()
