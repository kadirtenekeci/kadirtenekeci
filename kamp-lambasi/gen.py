import json, itertools
lamps = [
 "a retro matte-black metal LED camping lantern with a wire handle",
 "a collapsible olive-green silicone LED lantern",
 "a warm-white rechargeable hanging bulb lantern with a carabiner hook",
 "a vintage-style brass and glass camping lantern with warm flickering LED",
 "a rugged orange waterproof LED camping lantern",
 "a compact cylindrical aluminum lantern with a wooden handle",
 "a frosted glass globe camping lamp with a leather strap",
 "a solar-powered foldable camping lantern in sand beige",
]
angles = [
 "wide establishing shot", "close-up shot with shallow depth of field", "low-angle shot",
 "top-down overhead view", "over-the-shoulder perspective", "eye-level medium shot",
 "cinematic side view", "drone aerial view", "macro detail shot", "3/4 angle product-in-context shot",
]
themes = {
 "Cadir_Ici": [
  "inside a cozy dome tent with sleeping bags and a book", "inside a canvas bell tent with rugs and pillows",
  "a person reading a map inside a small tent at night", "tent interior glowing from outside at dusk, silhouette of a camper",
  "couple playing cards inside a tent", "tent vestibule with boots and backpack at night",
  "child in pajamas with a stuffed toy inside a family tent", "solo hiker writing a journal inside a tiny ultralight tent",
  "rain drops on the tent fly while the lantern glows inside", "tent opening view to a starry sky from inside",
 ],
 "Arac_Kampi": [
  "open SUV trunk bed setup with blankets at a campsite", "rooftop tent on a 4x4 at twilight",
  "converted camper van with side door open in the forest", "pickup truck bed camping with mattress under the stars",
  "car tailgate kitchen with a camping stove", "overland vehicle with awning set up in the desert",
  "vintage VW-style van parked by a lake", "hatchback car camping with fairy lights, couple relaxing",
  "lantern hanging from the car's roof rack at night", "inside a van with a small bed and lantern on the shelf",
 ],
 "Orman": [
  "among tall pine trees at dusk", "on a mossy log in a misty forest",
  "hanging on a tree branch next to a hammock", "forest trail at blue hour with hikers",
  "on a wooden camp table in a redwood forest", "autumn forest with orange leaves on the ground",
  "deep forest clearing with a tent and fog", "birch forest in early morning light",
  "forest campsite with a dog lying beside the lantern", "rainforest-like green ferns around the lantern",
 ],
 "Sahil": [
  "on the sand at a beach campsite at sunset", "beach tent with waves in the background at twilight",
  "on a driftwood log at the beach at night", "rocky coastline camp above the sea",
  "friends having a beach picnic after sunset", "on a surfboard stand next to a beach tent",
  "tropical beach with palm trees and a hammock at dusk", "beach bonfire nearby with the lantern on a cooler",
  "pebble beach on a Mediterranean cove at night", "sea kayak pulled up on the shore next to a tent",
 ],
 "Gece_Ay_Isigi": [
  "under a full moon on a hill campsite", "milky way sky above a tent",
  "moonlight reflecting on a calm lake next to the camp", "stargazing couple lying on a blanket",
  "silhouette of a camper holding the lantern under the moon", "long-exposure star trails above a campsite",
  "moonlit desert dunes camp", "crescent moon over mountains with a glowing tent",
  "telescope next to the lantern on a clear night", "night meadow with fireflies and the lantern",
 ],
 "Ates_Basi": [
  "beside a crackling campfire with friends", "roasting marshmallows at a campfire",
  "cast iron pot cooking over a campfire", "guitar player by the campfire at night",
  "family telling stories around the campfire", "hot coffee mugs next to the fire pit",
  "solo camper warming hands at the fire", "stone fire ring with logs and the lantern on a rock",
  "campfire embers flying into the night sky", "wooden chairs around a fire pit at a glamping site",
 ],
 "Dag_Gol": [
  "alpine lake shore campsite at sunrise", "mountain summit camp above the clouds",
  "wooden dock on a lake at dusk", "canoe on the lakeside with a tent nearby",
  "rocky mountain ridge with a tent at golden hour", "fishing rod and the lantern by the river",
  "waterfall nearby a small campsite", "high plateau camp with snowy peaks behind",
  "reflections of mountains in a still lake at blue hour", "canyon campsite with red rocks",
 ],
 "Kis_Yagmur": [
  "snowy winter camp with a tent covered in snow", "lantern in the snow with falling snowflakes",
  "winter cabin porch with the lantern at night", "heavy rain under a tarp shelter at camp",
  "foggy rainy forest camp with puddles", "frozen lake winter camp at dusk",
  "hot tea and wool blanket in a winter tent", "northern lights over a snowy campsite",
  "hiker in a raincoat holding the lantern", "cozy rainy-day tent entrance with steaming cup",
 ],
 "Glamping_Aile": [
  "luxury glamping tent with a wooden deck", "family picnic table dinner at a campsite",
  "hammock between trees with a person relaxing", "kids making shadow puppets with the lantern",
  "romantic dinner for two at a glamping site", "group of friends playing board games at a camp table",
  "yurt interior with warm decor", "campground with multiple tents glowing at night",
  "mother and child reading a story at camp", "outdoor cinema night at a glamping site",
 ],
 "Urun_Studyo": [
  "on a clean white background, e-commerce product photo", "on a dark moody background with dramatic rim light",
  "flat lay with camping gear: compass, knife, map, mug", "on a wooden crate with rope and pine cones",
  "on a stone surface with moss, studio lighting", "floating with dynamic splash of water showing waterproofing",
  "product lineup of several lanterns in different colors", "hand holding the lantern against a blurred night background",
  "exploded-view style showing the lantern's features", "lantern on a backpack strap, lifestyle detail",
 ],
}
aspects = ["LANDSCAPE_3_2","PORTRAIT_4_5","SQUARE_1_1","LANDSCAPE_16_9"]
out=[]; n=0
for ti,(t,scenes) in enumerate(themes.items()):
  for si,s in enumerate(scenes):
    for v in range(2):
      lamp = lamps[(n*3+ti)%len(lamps)]
      ang = angles[(si*2+v+ti)%len(angles)]
      n+=1
      p = f"{ang.capitalize()} of {lamp} as the hero light source, {s}. Photorealistic outdoor lifestyle photography, warm lantern glow, cinematic lighting, high detail."
      out.append({"id":n,"theme":t,"aspect":aspects[(n)%4],"prompt":p})
json.dump(out,open("prompts.json","w"),indent=1,ensure_ascii=False)
print(len(out))
