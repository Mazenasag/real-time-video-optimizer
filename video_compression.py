# video_compression.py
import os
import subprocess
import cv2
from config import *

class VideoCompressor:
    def __init__(self, codec='h264', crf=23, preset='medium', resolution=(1920, 1080)):
        self.codec = codec
        self.crf = crf
        self.preset = preset
        self.resolution = resolution

    def set_parameters_by_bandwidth(self, bandwidth):
        """Set compression parameters based on predicted bandwidth"""
        if bandwidth < 10:  # Low bandwidth
            self.codec = 'libx264'
            self.crf = 28
            self.resolution = (640, 360)
        elif bandwidth < 20:
            self.codec = 'libx264'
            self.crf = 25
            self.resolution = (854, 480)
        else:  # High bandwidth
            self.codec = 'libx265'
            self.crf = 23
            self.resolution = (1280, 720)

    def compress_video(self, input_path=INPUT_VIDEO_PATH, 
                       output_path=COMPRESSED_VIDEO_PATH):
        """Compress video using FFmpeg with current settings"""
        cmd = [
            'ffmpeg', '-i', input_path,
            '-vf', f'scale={self.resolution[0]}:{self.resolution[1]}',
            '-c:v', self.codec, '-crf', str(self.crf),
            '-preset', self.preset, output_path
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"Video compressed: {output_path}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Compression failed: {e.stderr.decode()}")
            return False