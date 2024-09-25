# from PIL import Image

# # ASCII characters used to build outputs
# ASCII_CHARS = ["@", "#", "8", "&", "o", ":", "*", ".", " "]

# # Resize the input image while maintaining the aspect ratio
# def resize_image(image, new_width=150, scaling_factor=0.7):
#     width, height = image.size
#     aspect_ratio = height / width
#     new_height = int(new_width / aspect_ratio * scaling_factor)
#     resized_image = image.resize((new_width, new_height))
#     return resized_image

# # Convert each pixel to grayscale
# def grayify(image):
#     grayscale_image = image.convert("L")
#     return grayscale_image

# # Convert pixels to ASCII with lighter mapping
# def pixels_to_ascii(image):
#     pixels = image.getdata()

#     # Normalize pixel values to the range [0, 255]
#     normalized_pixels = [pixel / 255 for pixel in pixels]

#     # Map normalized pixel values to ASCII characters with a higher divisor
#     characters = "".join([ASCII_CHARS[int(value * (len(ASCII_CHARS) - 1) / 2)] for value in normalized_pixels])
#     return characters

# # To open an image by user input
# def main(new_width=150, scaling_factor=0.7):  # Adjust new_width and scaling_factor as needed
#     path = input("Enter a valid pathname to an image:\n")
#     image = None
#     try:
#         image = Image.open(path)  # Use 'Image' from the imported PIL module
#     except Exception as e:
#         print(f"{path} is not a valid pathname to an image. Error: {e}")
#         return

#     # Convert img to ASCII with adjusted width and height
#     new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width, scaling_factor)))

#     # To format
#     pixel_count = len(new_image_data)
#     ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

#     # Print result
#     print(ascii_image)

#     # Save result to "ascii_image.txt"
#     with open("ascii_image.txt", "w") as f:
#         f.write(ascii_image)

# main()


# try



from PIL import Image

#ASCII characters used to build out outputs
ASCII_CHARS = ["#", "&","%", "+", "-", ";", ",", ".", " "]


#resize the input image
def resize_image (image, new_width=100):
    width, height = image.size
    ratio = height/width/1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

#covert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#covert pixels to ascii
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

#to open an image by user input
def main(new_width=100):
    path = input("Enter a valid pathname to an image:\n")
    image = None
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"{path}is not a valid pathname to an image. Error: {e}")
        return

    #convert img to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    #to format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    #print result
    print(ascii_image)

    #save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()