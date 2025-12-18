"""
FastAPI Web Application for Steganography Framework
Provides REST API endpoints for image and audio steganography operations.
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import os
import tempfile
import uuid
from pathlib import Path

from modules.image_steg import ImageSteganography
from modules.audio_steg import AudioSteganography
from utils.helpers import EncryptionHelper

# Initialize FastAPI app
app = FastAPI(
    title="Steganography API",
    description="API for hiding and extracting secret messages in images and audio files",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Initialize steganography modules
image_steg = ImageSteganography()
audio_steg = AudioSteganography()
encryption_helper = EncryptionHelper()

# Create temp directory for processing files
TEMP_DIR = Path(tempfile.gettempdir()) / "steg_uploads"
TEMP_DIR.mkdir(exist_ok=True)


class CapacityResponse(BaseModel):
    """Response model for capacity calculation"""
    capacity_bytes: int
    capacity_chars: int
    file_type: str


class MessageResponse(BaseModel):
    """Response model for decode operations"""
    success: bool
    message: str
    decrypted: bool = False


@app.get("/")
async def root():
    """Root endpoint - serves the web interface"""
    return FileResponse("static/index.html")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "steganography-api"}


@app.post("/api/image/capacity")
async def calculate_image_capacity(file: UploadFile = File(...)):
    """Calculate the message capacity of an image file"""
    try:
        # Save uploaded file temporarily
        file_id = str(uuid.uuid4())
        temp_path = TEMP_DIR / f"{file_id}_{file.filename}"
        
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Calculate capacity
        capacity = image_steg.calculate_capacity(str(temp_path))
        
        # Clean up
        os.remove(temp_path)
        
        return CapacityResponse(
            capacity_bytes=capacity,
            capacity_chars=capacity,
            file_type="image"
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error calculating capacity: {str(e)}")


@app.post("/api/audio/capacity")
async def calculate_audio_capacity(file: UploadFile = File(...)):
    """Calculate the message capacity of an audio file"""
    try:
        # Save uploaded file temporarily
        file_id = str(uuid.uuid4())
        temp_path = TEMP_DIR / f"{file_id}_{file.filename}"
        
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Calculate capacity
        capacity = audio_steg.calculate_capacity(str(temp_path))
        
        # Clean up
        os.remove(temp_path)
        
        return CapacityResponse(
            capacity_bytes=capacity,
            capacity_chars=capacity,
            file_type="audio"
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error calculating capacity: {str(e)}")


@app.post("/api/image/encode")
async def encode_image(
    file: UploadFile = File(...),
    message: str = Form(...),
    password: Optional[str] = Form(None),
    use_encryption: bool = Form(False)
):
    """Encode a secret message into an image"""
    try:
        # Validate file type
        if not file.filename.lower().endswith(('.png', '.bmp')):
            raise HTTPException(status_code=400, detail="Only PNG and BMP images are supported")
        
        # Save uploaded file
        file_id = str(uuid.uuid4())
        input_path = TEMP_DIR / f"{file_id}_input_{file.filename}"
        output_path = TEMP_DIR / f"{file_id}_output.png"
        
        with open(input_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Encrypt message if requested
        final_message = message
        if use_encryption:
            if not password:
                raise HTTPException(status_code=400, detail="Password required for encryption")
            final_message = encryption_helper.encrypt_message(message, password)
        
        # Encode message
        success, result_msg = image_steg.encode_image(
            str(input_path),
            final_message,
            str(output_path)
        )
        
        # Clean up input file
        os.remove(input_path)
        
        if not success:
            if os.path.exists(output_path):
                os.remove(output_path)
            raise HTTPException(status_code=400, detail=result_msg)
        
        # Return the stego image
        return FileResponse(
            output_path,
            media_type="image/png",
            filename=f"stego_{file.filename}",
            background=None  # Keep file until download completes
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error encoding image: {str(e)}")


@app.post("/api/image/decode")
async def decode_image(
    file: UploadFile = File(...),
    password: Optional[str] = Form(None),
    use_decryption: bool = Form(False)
):
    """Decode a secret message from an image"""
    try:
        # Save uploaded file
        file_id = str(uuid.uuid4())
        temp_path = TEMP_DIR / f"{file_id}_{file.filename}"
        
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Decode message
        success, extracted_msg = image_steg.decode_image(str(temp_path))
        
        # Clean up
        os.remove(temp_path)
        
        if not success:
            raise HTTPException(status_code=400, detail=extracted_msg)
        
        # Decrypt if requested
        decrypted = False
        if use_decryption:
            if not password:
                raise HTTPException(status_code=400, detail="Password required for decryption")
            try:
                extracted_msg = encryption_helper.decrypt_message(extracted_msg, password)
                decrypted = True
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Decryption failed: {str(e)}")
        
        return MessageResponse(
            success=True,
            message=extracted_msg,
            decrypted=decrypted
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding image: {str(e)}")


@app.post("/api/audio/encode")
async def encode_audio(
    file: UploadFile = File(...),
    message: str = Form(...),
    password: Optional[str] = Form(None),
    use_encryption: bool = Form(False),
    steg_key: Optional[str] = Form(None)
):
    """Encode a secret message into an audio file"""
    try:
        # Validate file type
        if not file.filename.lower().endswith('.wav'):
            raise HTTPException(status_code=400, detail="Only WAV audio files are supported")
        
        # Save uploaded file
        file_id = str(uuid.uuid4())
        input_path = TEMP_DIR / f"{file_id}_input_{file.filename}"
        output_path = TEMP_DIR / f"{file_id}_output.wav"
        
        with open(input_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Encrypt message if requested
        final_message = message
        if use_encryption:
            if not password:
                raise HTTPException(status_code=400, detail="Password required for encryption")
            final_message = encryption_helper.encrypt_message(message, password)
        
        # Encode message
        success, result_msg = audio_steg.encode_audio(
            str(input_path),
            final_message,
            str(output_path),
            key=steg_key
        )
        
        # Clean up input file
        os.remove(input_path)
        
        if not success:
            if os.path.exists(output_path):
                os.remove(output_path)
            raise HTTPException(status_code=400, detail=result_msg)
        
        # Return the stego audio
        return FileResponse(
            output_path,
            media_type="audio/wav",
            filename=f"stego_{file.filename}",
            background=None
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error encoding audio: {str(e)}")


@app.post("/api/audio/decode")
async def decode_audio(
    file: UploadFile = File(...),
    password: Optional[str] = Form(None),
    use_decryption: bool = Form(False),
    steg_key: Optional[str] = Form(None)
):
    """Decode a secret message from an audio file"""
    try:
        # Save uploaded file
        file_id = str(uuid.uuid4())
        temp_path = TEMP_DIR / f"{file_id}_{file.filename}"
        
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Decode message
        success, extracted_msg = audio_steg.decode_audio(str(temp_path), key=steg_key)
        
        # Clean up
        os.remove(temp_path)
        
        if not success:
            raise HTTPException(status_code=400, detail=extracted_msg)
        
        # Decrypt if requested
        decrypted = False
        if use_decryption:
            if not password:
                raise HTTPException(status_code=400, detail="Password required for decryption")
            try:
                extracted_msg = encryption_helper.decrypt_message(extracted_msg, password)
                decrypted = True
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Decryption failed: {str(e)}")
        
        return MessageResponse(
            success=True,
            message=extracted_msg,
            decrypted=decrypted
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding audio: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
