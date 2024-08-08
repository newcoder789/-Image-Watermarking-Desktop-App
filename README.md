**Watermark Image Using Pillow in Python**
Overview
This project provides a Python script to add various types of watermarks to images using the Pillow library. The script includes options to add text, image watermarks, lines, or apply a blur effect to the image.

Features
Text Watermarking: Add customizable text as a watermark with options to adjust the font, size, and position.
Image Watermarking: Overlay a watermark image on the main image with adjustable size and position.
Blurring: Apply a blur effect to the image before adding a watermark.
Custom Lines: Draw diagonal lines across the image as a watermark.

Parameters
original_path: Path to the input image.
blur_density: Blur density for the watermark_blur task.
font_size: Font size for text watermark.
font_text: Text content for the watermark_text task.
task: Type of watermarking task ("watermark_blur", "watermark_text", "watermark_img", "watermark_lines").
num_lines: Number of lines for the watermark_lines task.
watermark_img_path: Path to the watermark image for the watermark_img task.
