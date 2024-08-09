# Devanagari to Tamil mapping

സാധാരണാക്ഷരം = { #சாதாரணாக்ஷரம்
    # Numbers
    '०': '௦', '१': '௧', '२': '௨', '३': '௩', '४': '௪', '५': '௫', '६': '௬', '७': '௭', '८': '௮', '९': '௯', 

    # Vowels
    'अ': 'அ', 'आ': 'ஆ', 'इ': 'இ', 'ई': 'ஈ', 'उ': 'உ', 'ऊ': 'ஊ',
    'ऋ': 'ர்', 'ॠ': 'ற்', 'ऌ': '', 'ॡ': '', 
    'ऎ': 'எ', 'ए': 'ஏ', 'ऐ': 'ஐ', 
    'ऒ': 'ஒ', 'ओ': 'ஓ', 'औ': 'ஔ',
    'अं': 'அஂ', 'अः': 'அஃ',

    # Consonants

    'क': 'க',           # Basic ka
    'ख': 'ஃக',         # Second letter: ஃ + ka
    'ग': '\u200Bக',     # Third letter: ka + zero-width-space
    'घ': '\u200Bஃக',    # Fourth letter: ஃ + ka + zero-width-space
    'ङ': 'ங',

    'च': 'ச',           # Basic ca
    'छ': 'ஃச',         # Second letter: ஃ + ca
    'ज': 'ஜ',       # Third letter: ja 
    'झ': 'ஃஜ',      # Fourth letter: ஃ + ja
    'ञ': 'ஞ',

    'ट': 'ட',           # Basic ட
    'ठ': 'ஃட',         # Second letter: ஃ + ட
    'ड': '\u200Bட',     # Third letter: ட + zero-width-space
    'ढ': '\u200Bஃட',    # Fourth letter: ஃ + ட + zero-width-space
    'ण': 'ண',
    
    'ट़': 'ഺ',        #Placeholder letter. This is a Malayalam letter which is alveolar த/ட, usually written in Malayalam as റ്റ.Like the t in English word "Wet".
    'ऩ': 'ன',

    'त': 'த',           # Basic த
    'थ': 'ஃத',         # Second letter: ஃ + த
    'द': '\u200Bத',     # Third letter: த + zero-width-space
    'ध': '\u200Bஃத',    # Fourth letter: ஃ + த + zero-width-space
    'न': 'ந',

    'प': 'ப',           # Basic pa
    'फ': 'ஃப',         # Second letter: ஃ + pa
    'ब': '\u200Bப',     # Third letter: pa + zero-width-space
    'भ': '\u200Bஃப',    # Fourth letter: ஃ + pa + zero-width-space
    'म': 'ம',

    #FYI, whole of Bharat uses scripts that are derived out of Brahmi. Brahmi itself came from Sindhu script. Script is always adapted depending on the need such as Sindhu script for pottery (pictures to survive) to Brahmi for stone edifice (short lines to sculpt). Then, as the geography of North and South varies slightly, we took either Nagari for birch bark writing (North of India has this tree plenty) or Grantha for plam leaf writing (South of India has this tree plenty) This is why South Indian scripts are rounded lest palm leaf gets cut. Exception is Odia (Odisha is in the middle), which developed separate script from both, but still from Brahmi. Brahmi script was an innovation for the whole world as this was basis the innovation that Panini bought to the language. He structured letters basis the source of sound, which is why Indian language scripts are arranged from க-ச-ட-த-ப. Languages in India (except Tamizh) further innovated it and added more symbols for all sounds in each class of consonants.  
    #In the case of TamizhNad, it is even more important to not lose any more phonetic sound. Not having full set of letters as invented by Panini and others might be making it difficult to learn and pronounce other Indian languages (I am from Palakkad). This is simply the choice of the ruler kings in Tamizh Nad who would have prioritized quick learning for the script.  The main difference between Tamizh and Malayalam is that Malayalam retains full pronunication of words due to having full script. Tamizh is continuing to lose the letters, even the special characters which are exclusive to Tamizh (and Malayalam) with native speakers not using it, such as ழ, though Tamizh itself contains it (தமிழ்). 
    # Sadly due to not having unity, we are now using English, which has none of this innovation. We identify our language with our script, although both are independent of each other. Script is independent from the language (Most of the scripts are only few centuries old while languages are millenias old) and we always improved the script for the times. We need to adopt a common script lest we lose our language and common heritage to English.
    
    'य': 'ய', 'र': 'ர', 'ल': 'ல', 'व': 'வ',
    'श': 'ஶ', 'ष': 'ஷ', 'स': 'ஸ', 'ह': 'ஹ',
    'ळ': 'ள', 'ऱ': 'ற', 'ऴ': 'ழ',

    # Vowel signs
    'ा': 'ா', 'ि': 'ி', 'ी': 'ீ', 'ु': 'ு', 'ू': 'ூ', 'ृ': '',
    'ॆ': 'ெ', 'े': 'ே', 'ै': 'ை', 'ॊ': 'ொ', 'ो': 'ோ', 'ौ': 'ௌ',
    'ं': 'ஂ', 'ः': 'ஃ',
    'ऽ': '஽',

    '्': '்', # Virama
    'ँ': '஁', # Chandrabindu
}

വാക്യവിരാമം = { #வாக்கியவிராம்
    '।': '.' # வாக்கியவிராம்
}

ചില്ലക്ഷരം = { #சில்லக்ஷரம்
    'ऩ्': 'ந்', 'ण़्': 'ண்',
    'ळ्': 'ள்', 'ल़्': 'ல்',
    'ल्': 'ல்', 'ऴ्': 'ழ்',

    'म़्': 'ஂ', 'क़्': 'க்', 'य़्': 'ய்', 'ऴ़्': 'ழ்',
    'र्': 'ர்',
    'र्य': 'ர்ய',
    'ऱ्': 'ர்', 'ऱ़्': 'ர்',
    'ऱ्र्': 'ற்ற', 'ऱ्र': 'ற்ற', 'ऱ्ऱ्': 'ற்ற'
}

നുക്താക്ഷരം = { #நுக்தாக்ஷரம்
    'व़': 'ஃவ', # Special usage for Tamil
    'ज़': 'ஃஜ', # Special usage for Tamil
    'फ़': 'ஃப', # Special usage for Tamil
    'य़': 'ஃய', # Special usage for Tamil
}

നുക്തം = { #நுக்தம்
    '़': '​'  # Placeholder for Nukta
}
