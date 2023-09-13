from modules.util import join_prompts


fooocus_expansion = "Fooocus V2"
default_styles = ["Default (Slightly Cinematic)"]

# https://github.com/twri/sdxl_prompt_styler/blob/main/sdxl_styles.json

styles = [
    {
        "name": "Default (Slightly Cinematic)",
        "prompt": "cinematic still {prompt} . emotional, harmonious, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "sai-3d-model",
        "prompt": "professional 3d model {prompt} . octane render, highly detailed, volumetric, dramatic lighting",
        "negative_prompt": "ugly, deformed, noisy, low poly, blurry, painting"
    },
    {
        "name": "sai-analog film",
        "prompt": "analog film photo {prompt} . faded film, desaturated, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "sai-anime",
        "prompt": "anime artwork {prompt} . anime style, key visual, vibrant, studio anime,  highly detailed",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast"
    },
    {
        "name": "sai-cinematic",
        "prompt": "cinematic film still {prompt} . shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "sai-comic book",
        "prompt": "comic {prompt} . graphic illustration, comic art, graphic novel art, vibrant, highly detailed",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo"
    },
    {
        "name": "sai-craft clay",
        "prompt": "play-doh style {prompt} . sculpture, clay art, centered composition, Claymation",
        "negative_prompt": "sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "sai-digital art",
        "prompt": "concept art {prompt} . digital artwork, illustrative, painterly, matte painting, highly detailed",
        "negative_prompt": "photo, photorealistic, realism, ugly"
    },
    {
        "name": "sai-enhance",
        "prompt": "breathtaking {prompt} . award-winning, professional, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy"
    },
    {
        "name": "sai-fantasy art",
        "prompt": "ethereal fantasy concept art of  {prompt} . magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy",
        "negative_prompt": "photographic, realistic, realism, 35mm film, dslr, cropped, frame, text, deformed, glitch, noise, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, sloppy, duplicate, mutated, black and white"
    },
    {
        "name": "sai-isometric",
        "prompt": "isometric style {prompt} . vibrant, beautiful, crisp, detailed, ultra detailed, intricate",
        "negative_prompt": "deformed, mutated, ugly, disfigured, blur, blurry, noise, noisy, realistic, photographic"
    },
    {
        "name": "sai-line art",
        "prompt": "line art drawing {prompt} . professional, sleek, modern, minimalist, graphic, line art, vector graphics",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, mutated, realism, realistic, impressionism, expressionism, oil, acrylic"
    },
    {
        "name": "sai-lowpoly",
        "prompt": "low-poly style {prompt} . low-poly game art, polygon mesh, jagged, blocky, wireframe edges, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "sai-neonpunk",
        "prompt": "neonpunk style {prompt} . cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "sai-origami",
        "prompt": "origami style {prompt} . paper art, pleated paper, folded, origami art, pleats, cut and fold, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "sai-photographic",
        "prompt": "cinematic photo {prompt} . 35mm photograph, film, bokeh, professional, 4k, highly detailed",
        "negative_prompt": "drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly"
    },
    {
        "name": "sai-pixel art",
        "prompt": "pixel-art {prompt} . low-res, blocky, pixel art style, 8-bit graphics",
        "negative_prompt": "sloppy, messy, blurry, noisy, highly detailed, ultra textured, photo, realistic"
    },
    {
        "name": "sai-texture",
        "prompt": "texture {prompt} top down close-up",
        "negative_prompt": "ugly, deformed, noisy, blurry"
    },
    {
        "name": "ads-advertising",
        "prompt": "Advertising poster style {prompt} . Professional, modern, product-focused, commercial, eye-catching, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "ads-automotive",
        "prompt": "Automotive advertisement style {prompt} . Sleek, dynamic, professional, commercial, vehicle-focused, high-resolution, highly detailed",
        "negative_prompt": "noisy, blurry, unattractive, sloppy, unprofessional"
    },
    {
        "name": "ads-corporate",
        "prompt": "Corporate branding style {prompt} . Professional, clean, modern, sleek, minimalist, business-oriented, highly detailed",
        "negative_prompt": "noisy, blurry, grungy, sloppy, cluttered, disorganized"
    },
    {
        "name": "ads-fashion editorial",
        "prompt": "Fashion editorial style {prompt} . High fashion, trendy, stylish, editorial, magazine style, professional, highly detailed",
        "negative_prompt": "outdated, blurry, noisy, unattractive, sloppy"
    },
    {
        "name": "ads-food photography",
        "prompt": "Food photography style {prompt} . Appetizing, professional, culinary, high-resolution, commercial, highly detailed",
        "negative_prompt": "unappetizing, sloppy, unprofessional, noisy, blurry"
    },
    {
        "name": "ads-luxury",
        "prompt": "Luxury product style {prompt} . Elegant, sophisticated, high-end, luxurious, professional, highly detailed",
        "negative_prompt": "cheap, noisy, blurry, unattractive, amateurish"
    },
    {
        "name": "ads-real estate",
        "prompt": "Real estate photography style {prompt} . Professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed",
        "negative_prompt": "dark, blurry, unappealing, noisy, unprofessional"
    },
    {
        "name": "ads-retail",
        "prompt": "Retail packaging style {prompt} . Vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "artstyle-abstract",
        "prompt": "abstract style {prompt} . non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
        "negative_prompt": "realistic, photographic, figurative, concrete"
    },
    {
        "name": "artstyle-abstract expressionism",
        "prompt": "abstract expressionist painting {prompt} . energetic brushwork, bold colors, abstract forms, expressive, emotional",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, monochrome"
    },
    {
        "name": "artstyle-art deco",
        "prompt": "Art Deco style {prompt} . geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "artstyle-art nouveau",
        "prompt": "Art Nouveau style {prompt} . elegant, decorative, curvilinear forms, nature-inspired, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "artstyle-constructivist",
        "prompt": "constructivist style {prompt} . geometric shapes, bold colors, dynamic composition, propaganda art style",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, abstract expressionism"
    },
    {
        "name": "artstyle-cubist",
        "prompt": "cubist artwork {prompt} . geometric shapes, abstract, innovative, revolutionary",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "artstyle-expressionist",
        "prompt": "expressionist {prompt} . raw, emotional, dynamic, distortion for emotional effect, vibrant, use of unusual colors, detailed",
        "negative_prompt": "realism, symmetry, quiet, calm, photo"
    },
    {
        "name": "artstyle-graffiti",
        "prompt": "graffiti style {prompt} . street art, vibrant, urban, detailed, tag, mural",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "artstyle-hyperrealism",
        "prompt": "hyperrealistic art {prompt} . extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike",
        "negative_prompt": "simplified, abstract, unrealistic, impressionistic, low resolution"
    },
    {
        "name": "artstyle-impressionist",
        "prompt": "impressionist painting {prompt} . loose brushwork, vibrant color, light and shadow play, captures feeling over form",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "artstyle-pointillism",
        "prompt": "pointillism style {prompt} . composed entirely of small, distinct dots of color, vibrant, highly detailed",
        "negative_prompt": "line drawing, smooth shading, large color fields, simplistic"
    },
    {
        "name": "artstyle-pop art",
        "prompt": "Pop Art style {prompt} . bright colors, bold outlines, popular culture themes, ironic or kitsch",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, minimalist"
    },
    {
        "name": "artstyle-psychedelic",
        "prompt": "psychedelic style {prompt} . vibrant colors, swirling patterns, abstract forms, surreal, trippy",
        "negative_prompt": "monochrome, black and white, low contrast, realistic, photorealistic, plain, simple"
    },
    {
        "name": "artstyle-renaissance",
        "prompt": "Renaissance style {prompt} . realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract"
    },
    {
        "name": "artstyle-steampunk",
        "prompt": "steampunk style {prompt} . antique, mechanical, brass and copper tones, gears, intricate, detailed",
        "negative_prompt": "deformed, glitch, noisy, low contrast, anime, photorealistic"
    },
    {
        "name": "artstyle-surrealist",
        "prompt": "surrealist art {prompt} . dreamlike, mysterious, provocative, symbolic, intricate, detailed",
        "negative_prompt": "anime, photorealistic, realistic, deformed, glitch, noisy, low contrast"
    },
    {
        "name": "artstyle-typography",
        "prompt": "typographic art {prompt} . stylized, intricate, detailed, artistic, text-based",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "artstyle-watercolor",
        "prompt": "watercolor painting {prompt} . vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "futuristic-biomechanical",
        "prompt": "biomechanical style {prompt} . blend of organic and mechanical elements, futuristic, cybernetic, detailed, intricate",
        "negative_prompt": "natural, rustic, primitive, organic, simplistic"
    },
    {
        "name": "futuristic-biomechanical cyberpunk",
        "prompt": "biomechanical cyberpunk {prompt} . cybernetics, human-machine fusion, dystopian, organic meets artificial, dark, intricate, highly detailed",
        "negative_prompt": "natural, colorful, deformed, sketch, low contrast, watercolor"
    },
    {
        "name": "futuristic-cybernetic",
        "prompt": "cybernetic style {prompt} . futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "futuristic-cybernetic robot",
        "prompt": "cybernetic robot {prompt} . android, AI, machine, metal, wires, tech, futuristic, highly detailed",
        "negative_prompt": "organic, natural, human, sketch, watercolor, low contrast"
    },
    {
        "name": "futuristic-cyberpunk cityscape",
        "prompt": "cyberpunk cityscape {prompt} . neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed",
        "negative_prompt": "natural, rural, deformed, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "futuristic-futuristic",
        "prompt": "futuristic style {prompt} . sleek, modern, ultramodern, high tech, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vintage, antique"
    },
    {
        "name": "futuristic-retro cyberpunk",
        "prompt": "retro cyberpunk {prompt} . 80's inspired, synthwave, neon, vibrant, detailed, retro futurism",
        "negative_prompt": "modern, desaturated, black and white, realism, low contrast"
    },
    {
        "name": "futuristic-retro futurism",
        "prompt": "retro-futuristic {prompt} . vintage sci-fi, 50s and 60s style, atomic age, vibrant, highly detailed",
        "negative_prompt": "contemporary, realistic, rustic, primitive"
    },
    {
        "name": "futuristic-sci-fi",
        "prompt": "sci-fi style {prompt} . futuristic, technological, alien worlds, space themes, advanced civilizations",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "futuristic-vaporwave",
        "prompt": "vaporwave style {prompt} . retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed",
        "negative_prompt": "monochrome, muted colors, realism, rustic, minimalist, dark"
    },
    {
        "name": "game-bubble bobble",
        "prompt": "Bubble Bobble style {prompt} . 8-bit, cute, pixelated, fantasy, vibrant, reminiscent of Bubble Bobble game",
        "negative_prompt": "realistic, modern, photorealistic, violent, horror"
    },
    {
        "name": "game-cyberpunk game",
        "prompt": "cyberpunk game style {prompt} . neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre video games",
        "negative_prompt": "historical, natural, rustic, low detailed"
    },
    {
        "name": "game-fighting game",
        "prompt": "fighting game style {prompt} . dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games",
        "negative_prompt": "peaceful, calm, minimalist, photorealistic"
    },
    {
        "name": "game-gta",
        "prompt": "GTA-style artwork {prompt} . satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed",
        "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed"
    },
    {
        "name": "game-mario",
        "prompt": "Super Mario style {prompt} . vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "game-minecraft",
        "prompt": "Minecraft style {prompt} . blocky, pixelated, vibrant colors, recognizable characters and objects, game assets",
        "negative_prompt": "smooth, realistic, detailed, photorealistic, noise, blurry, deformed"
    },
    {
        "name": "game-pokemon",
        "prompt": "Pokémon style {prompt} . vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "game-retro arcade",
        "prompt": "retro arcade style {prompt} . 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games",
        "negative_prompt": "modern, ultra-high resolution, photorealistic, 3D"
    },
    {
        "name": "game-retro game",
        "prompt": "retro game art {prompt} . 16-bit, vibrant colors, pixelated, nostalgic, charming, fun",
        "negative_prompt": "realistic, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "game-rpg fantasy game",
        "prompt": "role-playing game (RPG) style fantasy {prompt} . detailed, vibrant, immersive, reminiscent of high fantasy RPG games",
        "negative_prompt": "sci-fi, modern, urban, futuristic, low detailed"
    },
    {
        "name": "game-strategy game",
        "prompt": "strategy game style {prompt} . overhead view, detailed map, units, reminiscent of real-time strategy video games",
        "negative_prompt": "first-person view, modern, photorealistic"
    },
    {
        "name": "game-streetfighter",
        "prompt": "Street Fighter style {prompt} . vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series",
        "negative_prompt": "3D, realistic, modern, photorealistic, turn-based strategy"
    },
    {
        "name": "game-zelda",
        "prompt": "Legend of Zelda style {prompt} . vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
        "negative_prompt": "sci-fi, modern, realistic, horror"
    },
    {
        "name": "misc-architectural",
        "prompt": "architectural style {prompt} . clean lines, geometric shapes, minimalist, modern, architectural drawing, highly detailed",
        "negative_prompt": "curved lines, ornate, baroque, abstract, grunge"
    },
    {
        "name": "misc-disco",
        "prompt": "disco-themed {prompt} . vibrant, groovy, retro 70s style, shiny disco balls, neon lights, dance floor, highly detailed",
        "negative_prompt": "minimalist, rustic, monochrome, contemporary, simplistic"
    },
    {
        "name": "misc-dreamscape",
        "prompt": "dreamscape {prompt} . surreal, ethereal, dreamy, mysterious, fantasy, highly detailed",
        "negative_prompt": "realistic, concrete, ordinary, mundane"
    },
    {
        "name": "misc-dystopian",
        "prompt": "dystopian style {prompt} . bleak, post-apocalyptic, somber, dramatic, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, cheerful, optimistic, vibrant, colorful"
    },
    {
        "name": "misc-fairy tale",
        "prompt": "fairy tale {prompt} . magical, fantastical, enchanting, storybook style, highly detailed",
        "negative_prompt": "realistic, modern, ordinary, mundane"
    },
    {
        "name": "misc-gothic",
        "prompt": "gothic style {prompt} . dark, mysterious, haunting, dramatic, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, cheerful, optimistic"
    },
    {
        "name": "misc-grunge",
        "prompt": "grunge style {prompt} . textured, distressed, vintage, edgy, punk rock vibe, dirty, noisy",
        "negative_prompt": "smooth, clean, minimalist, sleek, modern, photorealistic"
    },
    {
        "name": "misc-horror",
        "prompt": "horror-themed {prompt} . eerie, unsettling, dark, spooky, suspenseful, grim, highly detailed",
        "negative_prompt": "cheerful, bright, vibrant, light-hearted, cute"
    },
    {
        "name": "misc-kawaii",
        "prompt": "kawaii style {prompt} . cute, adorable, brightly colored, cheerful, anime influence, highly detailed",
        "negative_prompt": "dark, scary, realistic, monochrome, abstract"
    },
    {
        "name": "misc-lovecraftian",
        "prompt": "lovecraftian horror {prompt} . eldritch, cosmic horror, unknown, mysterious, surreal, highly detailed",
        "negative_prompt": "light-hearted, mundane, familiar, simplistic, realistic"
    },
    {
        "name": "misc-macabre",
        "prompt": "macabre style {prompt} . dark, gothic, grim, haunting, highly detailed",
        "negative_prompt": "bright, cheerful, light-hearted, cartoonish, cute"
    },
    {
        "name": "misc-manga",
        "prompt": "manga style {prompt} . vibrant, high-energy, detailed, iconic, Japanese comic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style"
    },
    {
        "name": "misc-metropolis",
        "prompt": "metropolis-themed {prompt} . urban, cityscape, skyscrapers, modern, futuristic, highly detailed",
        "negative_prompt": "rural, natural, rustic, historical, simple"
    },
    {
        "name": "misc-minimalist",
        "prompt": "minimalist style {prompt} . simple, clean, uncluttered, modern, elegant",
        "negative_prompt": "ornate, complicated, highly detailed, cluttered, disordered, messy, noisy"
    },
    {
        "name": "misc-monochrome",
        "prompt": "monochrome {prompt} . black and white, contrast, tone, texture, detailed",
        "negative_prompt": "colorful, vibrant, noisy, blurry, deformed"
    },
    {
        "name": "misc-nautical",
        "prompt": "nautical-themed {prompt} . sea, ocean, ships, maritime, beach, marine life, highly detailed",
        "negative_prompt": "landlocked, desert, mountains, urban, rustic"
    },
    {
        "name": "misc-space",
        "prompt": "space-themed {prompt} . cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed",
        "negative_prompt": "earthly, mundane, ground-based, realism"
    },
    {
        "name": "misc-stained glass",
        "prompt": "stained glass style {prompt} . vibrant, beautiful, translucent, intricate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "misc-techwear fashion",
        "prompt": "techwear fashion {prompt} . futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed",
        "negative_prompt": "vintage, rural, colorful, low contrast, realism, sketch, watercolor"
    },
    {
        "name": "misc-tribal",
        "prompt": "tribal style {prompt} . indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed",
        "negative_prompt": "modern, futuristic, minimalist, pastel"
    },
    {
        "name": "misc-zentangle",
        "prompt": "zentangle {prompt} . intricate, abstract, monochrome, patterns, meditative, highly detailed",
        "negative_prompt": "colorful, representative, simplistic, large fields of color"
    },
    {
        "name": "papercraft-collage",
        "prompt": "collage style {prompt} . mixed media, layered, textural, detailed, artistic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "papercraft-flat papercut",
        "prompt": "flat papercut style {prompt} . silhouette, clean cuts, paper, sharp edges, minimalist, color block",
        "negative_prompt": "3D, high detail, noise, grainy, blurry, painting, drawing, photo, disfigured"
    },
    {
        "name": "papercraft-kirigami",
        "prompt": "kirigami representation of {prompt} . 3D, paper folding, paper cutting, Japanese, intricate, symmetrical, precision, clean lines",
        "negative_prompt": "painting, drawing, 2D, noisy, blurry, deformed"
    },
    {
        "name": "papercraft-paper mache",
        "prompt": "paper mache representation of {prompt} . 3D, sculptural, textured, handmade, vibrant, fun",
        "negative_prompt": "2D, flat, photo, sketch, digital art, deformed, noisy, blurry"
    },
    {
        "name": "papercraft-paper quilling",
        "prompt": "paper quilling art of {prompt} . intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental",
        "negative_prompt": "photo, painting, drawing, 2D, flat, deformed, noisy, blurry"
    },
    {
        "name": "papercraft-papercut collage",
        "prompt": "papercut collage of {prompt} . mixed media, textured paper, overlapping, asymmetrical, abstract, vibrant",
        "negative_prompt": "photo, 3D, realistic, drawing, painting, high detail, disfigured"
    },
    {
        "name": "papercraft-papercut shadow box",
        "prompt": "3D papercut shadow box of {prompt} . layered, dimensional, depth, silhouette, shadow, papercut, handmade, high contrast",
        "negative_prompt": "painting, drawing, photo, 2D, flat, high detail, blurry, noisy, disfigured"
    },
    {
        "name": "papercraft-stacked papercut",
        "prompt": "stacked papercut art of {prompt} . 3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast",
        "negative_prompt": "2D, flat, noisy, blurry, painting, drawing, photo, deformed"
    },
    {
        "name": "papercraft-thick layered papercut",
        "prompt": "thick layered papercut art of {prompt} . deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers",
        "negative_prompt": "2D, flat, thin paper, low stack, smooth texture, painting, drawing, photo, deformed"
    },
    {
        "name": "photo-alien",
        "prompt": "alien-themed {prompt} . extraterrestrial, cosmic, otherworldly, mysterious, sci-fi, highly detailed",
        "negative_prompt": "earthly, mundane, common, realistic, simple"
    },
    {
        "name": "photo-film noir",
        "prompt": "film noir style {prompt} . monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vibrant, colorful"
    },
    {
        "name": "photo-hdr",
        "prompt": "HDR photo of {prompt} . High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed",
        "negative_prompt": "flat, low contrast, oversaturated, underexposed, overexposed, blurred, noisy"
    },
    {
        "name": "photo-long exposure",
        "prompt": "long exposure photo of {prompt} . Blurred motion, streaks of light, surreal, dreamy, ghosting effect, highly detailed",
        "negative_prompt": "static, noisy, deformed, shaky, abrupt, flat, low contrast"
    },
    {
        "name": "photo-neon noir",
        "prompt": "neon noir {prompt} . cyberpunk, dark, rainy streets, neon signs, high contrast, low light, vibrant, highly detailed",
        "negative_prompt": "bright, sunny, daytime, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "photo-silhouette",
        "prompt": "silhouette style {prompt} . high contrast, minimalistic, black and white, stark, dramatic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, color, realism, photorealistic"
    },
    {
        "name": "photo-tilt-shift",
        "prompt": "tilt-shift photo of {prompt} . Selective focus, miniature effect, blurred background, highly detailed, vibrant, perspective control",
        "negative_prompt": "blurry, noisy, deformed, flat, low contrast, unrealistic, oversaturated, underexposed"
    },
    {
        "name": "cinematic-diva",
        "prompt": "UHD, 8K, ultra detailed, a cinematic photograph of {prompt}, beautiful lighting, great composition",
        "negative_prompt": "ugly, deformed, noisy, blurry, NSFW"
    },
    {
        "name": "Abstract Expressionism",
        "prompt": "Abstract Expressionism Art, {prompt}, High contrast, minimalistic, colorful, stark, dramatic, expressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Academia",
        "prompt": "Academia, {prompt}, preppy Ivy League style, stark, dramatic, chic boarding school, academia",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, grunge, sloppy, unkempt"
    },
    {
        "name": "Action Figure",
        "prompt": "Action Figure, {prompt}, plastic collectable action figure, collectable toy action figure",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Adorable 3D Character",
        "prompt": "Adorable 3D Character, {prompt}, 3D render, adorable character, 3D art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, grunge, sloppy, unkempt, photograph, photo, realistic"
    },
    {
        "name": "Adorable Kawaii",
        "prompt": "Adorable Kawaii, {prompt}, pretty, cute, adorable, kawaii",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, gothic, dark, moody, monochromatic"
    },
    {
        "name": "Art Deco",
        "prompt": "Art Deco, {prompt}, sleek, geometric forms, art deco style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Art Nouveau",
        "prompt": "Art Nouveau, beautiful art, {prompt}, sleek, organic forms, long, sinuous, art nouveau style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, industrial, mechanical"
    },
    {
        "name": "Astral Aura",
        "prompt": "Astral Aura, {prompt}, astral, colorful aura, vibrant energy",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Avant-garde",
        "prompt": "Avant-garde, {prompt}, unusual, experimental, avant-garde art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Baroque",
        "prompt": "Baroque, {prompt}, dramatic, exuberant, grandeur, baroque art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Bauhaus-Style Poster",
        "prompt": "Bauhaus-Style Poster, {prompt}, simple geometric shapes, clean lines, primary colors, Bauhaus-Style Poster",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Blueprint Schematic Drawing",
        "prompt": "Blueprint Schematic Drawing, {prompt}, technical drawing, blueprint, schematic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Caricature",
        "prompt": "Caricature, {prompt}, exaggerated, comical, caricature",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Cel Shaded Art",
        "prompt": "Cel Shaded Art, {prompt}, 2D, flat color, toon shading, cel shaded style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Character Design Sheet",
        "prompt": "Character Design Sheet, {prompt}, character reference sheet, character turn around",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Classicism Art",
        "prompt": "Classicism Art, {prompt}, inspired by Roman and Greek culture, clarity, harmonious, classicism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Color Field Painting",
        "prompt": "Color Field Painting, {prompt}, abstract, simple, geometic, color field painting style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Colored Pencil Art",
        "prompt": "Colored Pencil Art, {prompt}, colored pencil strokes, light color, visible paper texture, colored pencil art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Conceptual Art",
        "prompt": "Conceptual Art, {prompt}, concept art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Constructivism",
        "prompt": "Constructivism Art, {prompt}, minimalistic, geometric forms, constructivism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Cubism",
        "prompt": "Cubism Art, {prompt}, flat geometric forms, cubism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dadaism",
        "prompt": "Dadaism Art, {prompt}, satirical, nonsensical, dadaism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dark Fantasy",
        "prompt": "Dark Fantasy Art, {prompt}, dark, moody, dark fantasy style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, bright, sunny"
    },
    {
        "name": "Dark Moody Atmosphere",
        "prompt": "Dark Moody Atmosphere, {prompt}, dramatic, mysterious, dark moody atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, vibrant, colorful, bright"
    },
    {
        "name": "DMT Art Style",
        "prompt": "DMT Art Style, {prompt}, bright colors, surreal visuals, swirling patterns, DMT art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Doodle Art",
        "prompt": "Doodle Art Style, {prompt}, drawing, freeform, swirling patterns, doodle art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Double Exposure",
        "prompt": "Double Exposure Style, {prompt}, double image ghost effect, image combination, double exposure style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dripping Paint Splatter Art",
        "prompt": "Dripping Paint Splatter Art, {prompt}, dramatic, paint drips, splatters, dripping paint",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Expressionism",
        "prompt": "Expressionism Art Style, {prompt}, movement, contrast, emotional, exaggerated forms, expressionism art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Faded Polaroid Photo",
        "prompt": "Faded Polaroid Photo, {prompt}, analog, old faded photo, old polaroid",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, vibrant, colorful"
    },
    {
        "name": "Fauvism",
        "prompt": "Fauvism Art, {prompt}, painterly, bold colors, textured brushwork, fauvism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Flat 2D Art",
        "prompt": "Flat 2D Art, {prompt}, simple flat color, 2-dimensional, Flat 2D Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "Fortnite Art Style",
        "prompt": "Fortnite Art Style, {prompt}, 3D cartoon, colorful, Fortnite Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "Futurism",
        "prompt": "Futurism Art Style, {prompt}, dynamic, dramatic, Futurism Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Glitchcore",
        "prompt": "Glitchcore Art Style, {prompt}, dynamic, dramatic, distorted, vibrant colors, glitchcore art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Glo-fi",
        "prompt": "Glo-fi Art Style, {prompt}, dynamic, dramatic, vibrant colors, glo-fi art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Googie Art Style",
        "prompt": "Googie Art Style, {prompt}, dynamic, dramatic, 1950's futurism, bold boomerang angles, Googie art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Graffiti Art",
        "prompt": "Graffiti Art Style, {prompt}, dynamic, dramatic, vibrant colors, graffiti art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Harlem Renaissance Art",
        "prompt": "Harlem Renaissance Art Style, {prompt}, dynamic, dramatic, 1920s African American culture, Harlem Renaissance art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "High Fashion",
        "prompt": "High Fashion, {prompt}, dynamic, dramatic, haute couture, elegant, ornate clothing, High Fashion",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Idyllic",
        "prompt": "Idyllic, {prompt}, peaceful, happy, pleasant, happy, harmonious, picturesque, charming",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Impressionism",
        "prompt": "Impressionism, {prompt}, painterly, small brushstrokes, visible brushstrokes, impressionistic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Infographic Drawing",
        "prompt": "Infographic Drawing, {prompt}, diagram, infographic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Ink Dripping Drawing",
        "prompt": "Ink Dripping Drawing, {prompt}, ink drawing, dripping ink",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "Japanese Ink Drawing",
        "prompt": "Japanese Ink Drawing, {prompt}, ink drawing, inkwash, Japanese Ink Drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "Knolling Photography",
        "prompt": "Knolling Photography, {prompt}, flat lay photography, object arrangment, knolling photography",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Light Cheery Atmosphere",
        "prompt": "Light Cheery Atmosphere, {prompt}, happy, joyful, cheerful, carefree, gleeful, lighthearted, pleasant atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, monochromatic, dark, moody"
    },
    {
        "name": "Logo Design",
        "prompt": "Logo Design, {prompt}, dynamic graphic art, vector art, minimalist, professional logo design",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Luxurious Elegance",
        "prompt": "Luxurious Elegance, {prompt}, extravagant, ornate, designer, opulent, picturesque, lavish",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Macro Photography",
        "prompt": "Macro Photography, {prompt}, close-up, macro 100mm, macro photography",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Mandola Art",
        "prompt": "Mandola art style, {prompt}, complex, circular design, mandola",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Marker Drawing",
        "prompt": "Marker Drawing, {prompt}, bold marker lines, visibile paper texture, marker drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "Medievalism",
        "prompt": "Medievalism, {prompt}, inspired by The Middle Ages, medieval art, elaborate patterns and decoration, Medievalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Minimalism",
        "prompt": "Minimalism, {prompt}, abstract, simple geometic shapes, hard edges, sleek contours, Minimalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Baroque",
        "prompt": "Neo-Baroque, {prompt}, ornate and elaborate, dynaimc, Neo-Baroque",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Byzantine",
        "prompt": "Neo-Byzantine, {prompt}, grand decorative religious style, Orthodox Christian inspired, Neo-Byzantine",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Futurism",
        "prompt": "Neo-Futurism, {prompt}, high-tech, curves, spirals, flowing lines, idealistic future, Neo-Futurism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Impressionism",
        "prompt": "Neo-Impressionism, {prompt}, tiny dabs of color, Pointillism, painterly, Neo-Impressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "Neo-Rococo",
        "prompt": "Neo-Rococo, {prompt}, curved forms, naturalistic ornamentation, elaborate, decorative, gaudy, Neo-Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neoclassicism",
        "prompt": "Neoclassicism, {prompt}, ancient Rome and Greece inspired, idealic, sober colors, Neoclassicism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Op Art",
        "prompt": "Op Art, {prompt}, optical illusion, abstract, geometric pattern, impression of movement, Op Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Ornate and Intricate",
        "prompt": "Ornate and Intricate, {prompt}, decorative, highly detailed, elaborate, ornate, intricate",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Pencil Sketch Drawing",
        "prompt": "Pencil Sketch Drawing, {prompt}, black and white drawing, graphite drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Pop Art 2",
        "prompt": "Pop Art, {prompt}, vivid colors, flat color, 2D, strong lines, Pop Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "Rococo",
        "prompt": "Rococo, {prompt}, flamboyant, pastel colors, curved lines, elaborate detail, Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Silhouette Art",
        "prompt": "Silhouette Art, {prompt}, high contrast, well defined, Silhouette Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Simple Vector Art",
        "prompt": "Simple Vector Art, {prompt}, 2D flat, simple shapes, minimalistic, professional graphic, flat color, high contrast, Simple Vector Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "Sketchup",
        "prompt": "Sketchup, {prompt}, CAD, professional design, Sketchup",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, photograph"
    },
    {
        "name": "Steampunk 2",
        "prompt": "Steampunk, {prompt}, retrofuturistic science fantasy, steam-powered tech, vintage industry, gears, neo-victorian, steampunk",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Surrealism",
        "prompt": "Surrealism, {prompt}, expressive, dramatic, organic lines and forms, dreamlike and mysterious, Surrealism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Suprematism",
        "prompt": "Suprematism, {prompt}, abstract, limited color palette, geometric forms, Suprematism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Terragen",
        "prompt": "Terragen, {prompt}, beautiful massive landscape, epic scenery, Terragen",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Tranquil Relaxing Atmosphere",
        "prompt": "Tranquil Relaxing Atmosphere, {prompt}, calming style, soothing colors, peaceful, idealic, Tranquil Relaxing Atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, oversaturated"
    },
    {
        "name": "Sticker Designs",
        "prompt": "Vector Art Stickers, {prompt}, professional vector design, sticker designs, Sticker Sheet",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Vibrant Rim Light",
        "prompt": "Vibrant Rim Light, {prompt}, bright rim light, high contrast, bold edge light",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Volumetric Lighting",
        "prompt": "Volumetric Lighting, {prompt}, light depth, dramatic atmospheric lighting, Volumetric Lighting",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Watercolor 2",
        "prompt": "Watercolor style painting, {prompt}, visible paper texture, colorwash, watercolor",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "Whimsical and Playful",
        "prompt": "Whimsical and Playful, {prompt}, imaginative, fantastical, bight colors, stylized, happy, Whimsical and Playful",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, drab, boring, moody"
    }
]


def normalize_key(k):
    k = k.replace('-', ' ')
    words = k.split(' ')
    words = [w[:1].upper() + w[1:].lower() for w in words]
    k = ' '.join(words)
    k = k.replace('3d', '3D')
    k = k.replace('Sai', 'SAI')
    k = k.replace('(s', '(S')
    return k


default_styles = [normalize_key(x) for x in default_styles]
styles = {normalize_key(k['name']): (k['prompt'], k['negative_prompt']) for k in styles}
style_keys = list(styles.keys())

SD_XL_BASE_RATIOS = {
    "0.5": (704, 1408),
    "0.52": (704, 1344),
    "0.57": (768, 1344),
    "0.6": (768, 1280),
    "0.68": (832, 1216),
    "0.72": (832, 1152),
    "0.78": (896, 1152),
    "0.82": (896, 1088),
    "0.88": (960, 1088),
    "0.94": (960, 1024),
    "1.0": (1024, 1024),
    "1.07": (1024, 960),
    "1.13": (1088, 960),
    "1.21": (1088, 896),
    "1.29": (1152, 896),
    "1.38": (1152, 832),
    "1.46": (1216, 832),
    "1.67": (1280, 768),
    "1.75": (1344, 768),
    "1.91": (1344, 704),
    "2.0": (1408, 704),
    "2.09": (1472, 704),
    "2.4": (1536, 640),
    "2.5": (1600, 640),
    "2.89": (1664, 576),
    "3.0": (1728, 576),
}

aspect_ratios = {str(v[0]) + '×' + str(v[1]): v for k, v in SD_XL_BASE_RATIOS.items()}


def apply_style(style, positive):
    p, n = styles[style]
    return p.replace('{prompt}', positive), n
