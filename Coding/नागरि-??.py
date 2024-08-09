#ഓരോ മാറ്റവും ഗ്രന്ഥപെട്ടിയിലും നാഗരിപെട്ടിയിലും വെവ്വേറെ ചെയ്യേണ്ടി വരാതിരിക്കാൻ തയ്യാറാക്കിയത്.
# ഓല - file. താളി - folder. പാകുക - coding. അക്ഷരപെട്ടി - keyboard. അരൂപ/അരൂപി - digital.

#ബ്രാഹ്മിഭാഷപാക‍ൽ-ലേക്ക് മാറ്റുക. 

ലിപി_നാമം = input("Enter the script name (without .py extension): ")  # Give the name of the file.
#എൻറ്റെ ഉപയോഗത്തിന് 'സരളഗ്രന്ഥ' അല്ലെങ്കി‍ൽ 'सरळनागरि'


import os
import sys
import importlib.util
from PIL import Image, ImageDraw, ImageFont
import subprocess


sys.path.append(os.getcwd())
ലിപി = __import__(ലിപി_നാമം)
സാധാരണാക്ഷരം = ലിപി.സാധാരണാക്ഷരം
ചില്ലക്ഷരം = ലിപി.ചില്ലക്ഷരം
നുക്താക്ഷരം = ലിപി.നുക്താക്ഷരം
നുക്തം = ലിപി.നുക്തം
വാക്യവിരാമം = ലിപി.വാക്യവിരാമം
ഭാഷപേര് = ലിപി_നാമം

# ഈ  എന്ന താളിയുള്ള പാത നൽകുക.
bundle_പാത = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #ഇത് coding എന്ന താളിയുടെ ഉള്ളി‍ൽ ആയതിനാ‍ൽ
print(".bundleൻറ്റെ സ്ഥാനം:", bundle_പാത) #os.getcwd ക്ക് പകരം
# നിക്ഷേപ & പരിണാമ ഓലകളുടെ പൂർണ്ണ പാത
നിക്ഷേപതാളി = os.path.join(bundle_പാത, 'सरळसंस्कृतं.bundle/Contents/Resources/सरळनागरि.keylayout')
പരിണാമതാളി = os.path.join(bundle_പാത, f'सरळसंस्कृतं.bundle/Contents/Resources/{ഭാഷപേര്}.keylayout')

def അക്ഷരപെട്ടി_പേരുമാഺം(ഉള്ളടക്കം):
    return ഉള്ളടക്കം.replace("सरळनागरि", ഭാഷപേര്)

def ലിപി_മാഺം(വാചകം):
    result = ""
    i = 0
    while i < len(വാചകം):
        # ചില്ലക്ഷരങ്ങളായി മാറുന്ന ദേവനാഗരി അക്ഷരകെട്ടിന് മൂന്നക്ഷരം ഉണ്ട്
        if i < len(വാചകം) - 2 and വാചകം[i:i+3] in ചില്ലക്ഷരം:
            result += ചില്ലക്ഷരം[വാചകം[i:i+3]]
            i += 3
        # ‍നുക്താക്ഷരങ്ങൾ (ജ്സ എന്നിവ) വരുന്നത് രണ്ടക്ഷര ദേവനാഗരി അക്ഷരകെട്ടിന് പകരമാണ്.
        elif i < len(വാചകം) - 1 and വാചകം[i:i+2] in നുക്താക്ഷരം:
            result += നുക്താക്ഷരം[വാചകം[i:i+2]]
            i += 2
        # സാധാരണാക്ഷരങ്ങൾക്ക്
        elif വാചകം[i] in സാധാരണാക്ഷരം:
            result += സാധാരണാക്ഷരം[വാചകം[i]]
            i += 1
        elif വാചകം[i] in വാക്യവിരാമം:
            result += വാക്യവിരാമം[വാചകം[i]]
            i += 1
        # നുക്തത്തിന്
        elif വാചകം[i] in നുക്തം:
            result += നുക്തം[വാചകം[i]]
            i += 1
        # ഒന്നും യോജിക്കുന്നില്ലെങ്കിൽ
        else:
            result += വാചകം[i]
            i += 1
    return result

def ഓല_മാഺം(നിക്ഷേപതാളി, പരിണാമതാളി):
    with open(നിക്ഷേപതാളി, 'r', encoding='utf-8') as f:
        ഉള്ളടക്കം = f.read()
    
    # മാറ്റങ്ങൾക്കു മുൻപായി അക്ഷരപെട്ടിയുടെ പേരുമാറ്റുക
    ഉള്ളടക്കം = അക്ഷരപെട്ടി_പേരുമാഺം(ഉള്ളടക്കം)
    
    # ദേവനാഗരിയെ മലയാളത്തിലേക്ക് മാറ്റൽ
    മാറ്റിയ_എഴുത്ത് = ലിപി_മാഺം(ഉള്ളടക്കം)
    
    #എല്ലാ മാറ്റങ്ങളും കഴിഞ്ഞതിന് ശേഷം വാക്യ വിരാമം (।) എന്നത് ശരിയായിടം വരുത്തിക്കാൻ. പൂർണമായും മാറില്ല, എന്തെന്നാ‍ൽ '.' കണ്ട് പിടിച്ച് മാറ്റുക എന്നത് ബുദ്ധിമുട്ടാണ്. തിരിച്ച് ചെയ്യാൻ എ‍ളുപ്പവും ആണ്.
    for key, value in വാക്യവിരാമം.items():
        മാറ്റിയ_എഴുത്ത് = മാറ്റിയ_എഴുത്ത്.replace(f'<key code="43" output="{value}"/>', f'<key code="43" output="{key}"/>')
    
    #ഇത് കൂടാതെ ടിപ്പണി കൊടുത്തത് മലയാളത്തി‍ൽ നിന്ന് തന്നത്താൻ ഹിന്ദിയിലേക്ക് മാറ്റാൻ വകുപ്പുണ്ടെങ്കി‍ൽ (Google Translate API) എനിക്ക് ബുദ്ധിമുട്ടി ടിപ്പണി മുറി-സംസ്കൃതത്തി‍ൽ എഴുതേണ്ടി വരില്ല.

    with open(പരിണാമതാളി, 'w', encoding='utf-8') as f:
        f.write(മാറ്റിയ_എഴുത്ത്)




    # Check for duplicate lines within blocks and remove them
    അനുകരണമാഺൽ(പരിണാമതാളി)

def അനുകരണമാഺൽ(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    block_lines = set()
    within_action_or_terminators_block = False
    within_keymap_block = False

    for line in lines:
        if '<action' in line or '<terminators' in line:
            within_action_or_terminators_block = True
            block_lines.clear()
        elif '<keyMap' in line:
            within_keymap_block = True
            block_lines.clear()

        if within_action_or_terminators_block:
            if '<when state="' in line:
                # Extract the value of `X`
                state_start = line.find('<when state="') + len('<when state="')
                state_end = line.find('"', state_start)
                state = line[state_start:state_end]

                if state not in block_lines:
                    new_lines.append(line)
                    block_lines.add(state)
            else:
                new_lines.append(line)
        elif within_keymap_block:
            if line not in block_lines:
                new_lines.append(line)
                block_lines.add(line)
        else:
            new_lines.append(line)

        if '</action>' in line or '</terminators>' in line:
            within_action_or_terminators_block = False
        elif '</keyMap>' in line:
            within_keymap_block = False

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

print(f'{പരിണാമതാളി}ലെ അനുകരണങ്ങൾ കളഞ്ഞു.')


def സുന്ദര_പ്രതീകം(അക്ഷരം, വലുപ്പം, output_path):
    # Create an image with transparent background
    image = Image.new('RGBA', (വലുപ്പം, വലുപ്പം), (255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(image)

    # Define initial font വലുപ്പം and color
    തുടക്കത്തിലെ_പ്രതീക_വലുപ്പം = വലുപ്പം // 2  # Start with a large font വലുപ്പം
    green_color = (0, 255, 0, 255)  # Green text color with full opacity
    
    # Load a TTF font file that supports Unicode characters
    try:
        font_path = "/Library/Fonts/Arial Unicode.ttf"  # Adjust to a font path that exists on your system
        font = ImageFont.truetype(font_path, തുടക്കത്തിലെ_പ്രതീക_വലുപ്പം)
    except IOError:
        font = ImageFont.load_default()
    
    # Increase the font വലുപ്പം until the text fits the canvas
    പ്രതീക_വലുപ്പം = തുടക്കത്തിലെ_പ്രതീക_വലുപ്പം
    while True:
        font = ImageFont.truetype(font_path, പ്രതീക_വലുപ്പം)
        bbox = draw.textbbox((0, 0), അക്ഷരം, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        if text_width >= വലുപ്പം * 0.8 or text_height >= വലുപ്പം * 0.8:  # Leave some margin
            break
        പ്രതീക_വലുപ്പം += 10

    # Calculate the position to center the text
    text_x = (വലുപ്പം - text_width) / 2
    # To fix the bottom center issue, adjust the y position using bbox top value
    text_y = (വലുപ്പം - text_height) / 2 - bbox[1]

    # Draw text on the image
    draw.text((text_x, text_y), അക്ഷരം, fill=green_color, font=font)
    
    # Save the image
    image.save(output_path)
    #print(f'Image saved as {output_path}')

def പ്രതീകം_ഉണ്ടാക്കൽ(script_name):
    # Load the script module dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, f"{script_name}.py")
    
    spec = importlib.util.spec_from_file_location(script_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Fetch the value for the key 'आ'
    അക്ഷരം = module.സാധാരണാക്ഷരം['आ']
    
    # Define വലുപ്പംങൾ for the iconset
    വലുപ്പങൾ = [16, 32, 64, 128, 256, 512, 1024]
    iconset_dir = os.path.join(script_dir, 'അക്ഷരം.iconset')

    # Create iconset directory
    if not os.path.exists(iconset_dir):
        os.makedirs(iconset_dir)
    
    # Generate images for each വലുപ്പം and save them in the iconset directory
    for വലുപ്പം in വലുപ്പങൾ:
        output_path = os.path.join(iconset_dir, f'icon_{വലുപ്പം}x{വലുപ്പം}.png')
        സുന്ദര_പ്രതീകം(അക്ഷരം, വലുപ്പം, output_path)
        if വലുപ്പം != 1024:  # For @2x വലുപ്പങൾ
            output_path_2x = os.path.join(iconset_dir, f'icon_{വലുപ്പം}x{വലുപ്പം}@2x.png')
            സുന്ദര_പ്രതീകം(അക്ഷരം, വലുപ്പം * 2, output_path_2x)

    # Convert the iconset to ICNS using iconutil
    icns_path = os.path.join(os.path.dirname(പരിണാമതാളി), f'{script_name}.icns')
    subprocess.run(['iconutil', '-c', 'icns', iconset_dir, '-o', icns_path])

    # Clean up the iconset directory
    subprocess.run(['rm', '-rf', iconset_dir])

    print(f'ICNS file created at {icns_path}')




# Call the main function
ഓല_മാഺം(നിക്ഷേപതാളി, പരിണാമതാളി)
print(f'ഓലമാഺം പൂർത്തിയായി. പരിണാമം {പരിണാമതാളി} ൽ സംരക്ഷിച്ചു.')

# Generate the ICNS file
പ്രതീകം_ഉണ്ടാക്കൽ(ലിപി_നാമം)