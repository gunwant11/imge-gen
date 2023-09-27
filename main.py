from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(input_image_path, brand_name, service_name, output_image_path):
    input_image = Image.open(input_image_path)
    print(input_image.width)
    if input_image.width > 3000 or input_image.height > 3000:
     input_image = input_image.resize((int(input_image.width / 3), int(input_image.height / 3)))

    top_spacing = 100
    left_spacing = 150

    new_width = input_image.width + left_spacing
    new_height = input_image.height + top_spacing + 400 

    new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))

    new_image.paste(input_image, (left_spacing, top_spacing))

    draw = ImageDraw.Draw(new_image)

    font = ImageFont.truetype("poppins.ttf", 52)
    font2 = ImageFont.truetype("poppins.ttf", 98)

   
    brand_text_size = draw.textlength(brand_name, font=font)
    service_text_size = draw.textlength(service_name, font=font)

    brand_x = brand_text_size 
    service_x = (new_width - service_text_size) / 2
    text_y = top_spacing + input_image.height  


    black_box = ImageDraw.Draw(new_image)
    black_box.rectangle([(0, text_y ), (new_width, text_y + 150)], fill=(0, 0, 0))

    pink_box = ImageDraw.Draw(new_image)
    pink_box.rectangle([(0, text_y), (brand_text_size+100, text_y + 150)], fill=(255, 192, 203))
    draw.text((50, text_y + 40), brand_name, fill=(255,255,255), font=font)

    draw.text((service_x, text_y + 200), service_name, fill=(0,0,0), font=font2)

    new_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "input.jpg" 
    brand_name = "Oops Upside YO Head"
    service_name = "Hairstyling In Houston"
    output_image_path = "output_image.jpg"  

    create_image_with_text(input_image_path, brand_name, service_name, output_image_path)
