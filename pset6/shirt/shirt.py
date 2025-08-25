import os
import sys
from PIL import Image, ImageOps

#reusable function:

#Validate args
def validate_args():
    #exactly 2 args: input and output files
    #img extensionmust be .jpg, .jpeg, .png
    #input and output must be same extension
    #input file must exist
    #returns: input and outfile filenames

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command_line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = (".jpg", ".jpeg", ".png") #create tuple of valid extensions

    #get input file ext.
    input_ext = os.path.splitext(input_file)[1].lower()  #splitext returns a tuple(file name, ext)
    output_ext = os.path.splitext(output_file)[1].lower() #[1] gets the ext index 0: file name

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(input_file): #if input filde doesnt exist
        sys.exit("Input does not exist")

    return input_file, output_file #return valid input and putout names if all is well and valid

#process image
def open_img(path):

    #open input img using Pillow
    #args: path(str) to image file
    #return: img object
    try:
        shirt = Image.open(path) #attempt to open input file and return img object
        return shirt
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except OSError:
        sys.exit("Invalid input")

#resize and crop img
def resize_crop(img, target_size=(600, 600)):
    #resize and crop
    #args:
        #Image - Pil img object
        #size - tuple(width, height)
    #return: resized and cropped img object

    #ImageOps.fit resizes and crops to exactly match target_size
    # Keeps aspect ratio and centers image

    return ImageOps.fit(img, target_size) #return resized img with 600x600 as automatic sizing

#Overlay shrt img onto input img
def overlay_shirt(photo, shirt):
    #overlay shirt into photo
    #args:
        #photo - Pil img object
        #shirt - Pil img object
    #return: combined img object

    #second shirt "arg" is an overlay using alpha channel as mask
    photo.paste(shirt, shirt) #paste shirt at 0,0 using alpha channel as mask
    return photo

#save new combined img
def save_img(img, path):
    #save img to path
    #args:
        #img - Pil img object
        #path - str path to save img
    #return none

    img.save(path)

def main():

    #validate args and get input and output file names
    input_file, output_file = validate_args()

    #open input and shirt img
    photo = open_img(input_file)
    shirt = open_img("shirt.png") #should be in same dir/folder as shirt.py

    #resize and crop photo to match shirt dimensions
    photo_resized = resize_crop(photo, shirt.size) #shirt.size gets the size tuple of shirt img

    #overlay shirt into photo
    combined_img = overlay_shirt(photo_resized, shirt)

    #save new combo img
    save_img(combined_img, output_file)

    print(f"{output_file} saved successfully.")

if __name__ == "__main__":
    main()




