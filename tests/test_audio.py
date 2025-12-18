
"""
Test script for Audio Steganography
Creates a simple test audio file and performs encode/decode operations.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import wave
import numpy as np
from modules.audio_steg import AudioSteganography

def create_test_audio(filename="test_cover.wav", duration=2, sample_rate=44100):
    """Create a simple test audio file (sine wave)."""
    
    frequency = 440  
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio_data = np.sin(2 * np.pi * frequency * t)
    
    audio_data = (audio_data * 32767).astype(np.int16)
    
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  
        wav_file.setsampwidth(2)  
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())
    
    print(f"[OK] Test audio created: {filename} ({duration}s, {sample_rate}Hz)")
    return filename

def test_audio_steganography():
    """Test audio steganography encoding and decoding."""
    print("\n" + "=" * 60)
    print("AUDIO STEGANOGRAPHY TEST")
    print("=" * 60)
    
    steg = AudioSteganography()
    
    cover_audio = create_test_audio()
    
    secret_message = "Secret audio message with LSB embedding!"
    print(f"\n Secret Message: '{secret_message}'")
    print(f"   Length: {len(secret_message)} characters")
    
    capacity = steg.calculate_capacity(cover_audio)
    print(f"\n Audio Capacity: {capacity} bytes ({capacity} characters)")
    
    print("\n" + "-" * 60)
    print("TEST 1: Sequential Embedding (no key)")
    print("-" * 60)
    
    print("\n Encoding message...")
    stego_audio = "test_stego_sequential.wav"
    success, msg = steg.encode_audio(cover_audio, secret_message, stego_audio)
    
    if success:
        print(f"   [OK] {msg}")
    else:
        print(f"   [FAIL] {msg}")
        return False
    
    print("\n Comparing original and stego audio...")
    comparison = steg.compare_audio(cover_audio, stego_audio)
    print(f"   Max Difference: {comparison['max_difference']} (LSB changes only)")
    print(f"   Mean Difference: {comparison['mean_difference']:.6f}")
    print(f"   Modified Samples: {comparison['modified_samples']} / {comparison['total_samples']}")
    print(f"   Modification: {comparison['modification_percentage']:.4f}%")
    
    print("\n Decoding message...")
    success, decoded_message = steg.decode_audio(stego_audio)
    
    if success:
        print(f"   [OK] Decoded successfully!")
        print(f"    Decoded Message: '{decoded_message}'")
        
        if decoded_message == secret_message:
            print("   [OK] Messages match perfectly!")
        else:
            print("   [FAIL] Messages do not match")
            return False
    else:
        print(f"   [FAIL] Decoding failed: {decoded_message}")
        return False
    
    print("\n" + "-" * 60)
    print("TEST 2: Key-Based Embedding")
    print("-" * 60)
    
    embedding_key = "my_secret_key_123"
    print(f"\n Using key: '{embedding_key}'")
    
    print("\n Encoding message with key...")
    stego_audio_key = "test_stego_keybased.wav"
    success, msg = steg.encode_audio(cover_audio, secret_message, stego_audio_key, key=embedding_key)
    
    if success:
        print(f"   [OK] {msg}")
    else:
        print(f"   [FAIL] {msg}")
        return False
    
    print("\n Decoding with correct key...")
    success, decoded_message = steg.decode_audio(stego_audio_key, key=embedding_key)
    
    if success:
        print(f"   [OK] Decoded successfully!")
        print(f"    Decoded Message: '{decoded_message}'")
        
        if decoded_message == secret_message:
            print("   [OK] Messages match perfectly!")
        else:
            print("   [FAIL] Messages do not match")
            return False
    else:
        print(f"   [FAIL] Decoding failed: {decoded_message}")
        return False
    
    print("\n Decoding with wrong key (should fail)...")
    success, decoded_message = steg.decode_audio(stego_audio_key, key="wrong_key")
    
    if success and decoded_message == secret_message:
        print("   [FAIL] UNEXPECTED: Decoded with wrong key!")
        return False
    else:
        print("   [OK] Correctly failed with wrong key")
    
    return True

if __name__ == "__main__":
    try:
        success = test_audio_steganography()
        print("\n" + "=" * 60)
        if success:
            print("[OK] ALL TESTS PASSED")
        else:
            print("[FAIL] TESTS FAILED")
        print("=" * 60 + "\n")
    except Exception as e:
        print(f"\n[FAIL] ERROR: {str(e)}\n")
        import traceback
        traceback.print_exc()
