from PIL import Image

def compress_image(input_image_path, output_image_path, scale_factor):
    with Image.open(input_image_path) as image:
        # Get the original dimensions
        original_width, original_height = image.size
        
        # Calculate new dimensions
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        
        # Resize the image
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the compressed image
        resized_image.save(output_image_path)

def main():
    input_image_path = input("Enter the path to the input image: ")
    output_image_path = input("Enter the path to save the compressed image: ")
    scale_factor = float(input("Enter the scale factor (e.g., 0.5 for 50%): "))
    
    compress_image(input_image_path, output_image_path, scale_factor)
    print(f"Image saved at {output_image_path}")

if __name__ == "__main__":
    main()

    """
    Compresses an image by resizing it to a given scale factor.

    * param input_image_path: Path to the input image file without the colons
    * param output_image_path: Path to save the compressed image with the name you want to give to the new image 
    file without the colons
    * param scale_factor: The ratio by which to scale the image

    Here's how you can interpret the scale factor for different compression requirements:

    * Scale Factor 1 (1:1 Ratio): No compression. The image dimensions remain the same.
    * Scale Factor 0.5 (2:2 Ratio): The image dimensions are halved. This reduces the width and height by 50%,  
      resulting in an image that is 25% of the original size.
    * Scale Factor 0.25 (4:4 Ratio): The image dimensions are reduced to a quarter of the original size. This 
      reduces the width and height by 75%, resulting in an image that is 6.25% of the original size.
    """