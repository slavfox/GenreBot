# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import discord
import os
import re
import random


intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


class GenreGen:
    tpl_re = re.compile(r"\{(.*?)\}")

    TEMPLATE = [
        "{TOP_GENRE}",
        "{TOP_GENRE}",
        "{QUALIFIER} {TOP_GENRE}",
        "{QUALIFIER} {TOP_GENRE}",
        "{PREFIX}-{TOP_GENRE}",
        "{QUALIFIER} {QUALIFIER} {TOP_GENRE}",
    ]

    TOP_GENRE = [
        "{GENRE}",
        "{GENRE}",
        "{GENRE}",
        "{GENRE}",
        "Nu-{GENRE}",
        "Post-{GENRE}",
        "Electro-{GENRE}",
        "Lo-fi {GENRE}",
        "Avant-{GENRE}",
        "Prog-{GENRE}",
    ]

    QUALIFIER = [
        "Harsh",
        "Heavy",
        "Soft",
        "Cool",
        "Dark",
        "Minimal",
        "New",
        "Tropical",
        "Ambient",
        "Punk",
        "Downtempo",
        "Indie",
        "Alternative",
        "Progressive",
        "Contemporary",
        "Hard",
        "Euphoric",
        "Acid",
        "Happy",
        "Psychedelic",
        "Industrial",
        "Instrumental",
        "Neotraditional",
        "Southern",
        "Hardcore",
        "Orchestral",
        "Vocal",
        "Space age",
        "Melodic",
        "Technical",
        "Atmospheric",
        "Symphonic",
        "Anarchist",
        "Hardcore",
        "Ska",
        "Deep",
        "Raw",
        "Pretty",
        "Jazzy",
        "Classic",
    ]

    PREFIX = [
        "Clown",
        "Bedroom",
        "Bard",
        "Witch",
        "Accounting",
        "Tax-evasion",
        "Librarian",
        "Crime",
        "Male",
        "Gender",
        "Rooftop",
        "Sky",
        "Cloud",
        "Ocean",
        "Cringe",
        "Cuddle",
        "Tiktok",
        "Fidget",
        "Hyper",
        "Ultra",
        "Super",
        "Mega",
        "Minimal",
        "Future",
        "Medieval",
        "Zen",
        "Crab",
        "Elevator",
        "Burrito",
        "Cat",
        "Kitten",
        "Synth",
        "Space",
        "Jungle",
        "Trip",
        "Doom",
        "Sludge",
        "Death",
        "Groove",
        "Pirate",
        "Emo",
        "Vocaloid",
        "Void",
        "Turbo",
        "Forest",
        "Speed",
        "Anime",
        "Art",
        "Study"
    ]

    GENRE = ([
        "{CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}{CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}{CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}{CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}",
        "{CORE_GENRE}{CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{PREFIX} {CORE_GENRE}",
        "{CORE_GENRE}core",
        "{PREFIX}core",
        "{CORE_GENRE}core",
        "{PREFIX}core",
        "{PREFIX}-hop",
        "{CORE_GENRE}wave",
        "{PREFIX}wave",
        "{PREFIX}gaze",
        "{CORE_GENRE}tronica",
        "{PREFIX}tronica",
        "{CORE_GENRE}step",
        "{PREFIX}step",
    ] * 4) + [
        "{CORE_GENRE}abilly",
        "{PREFIX}abilly",
    ]
    CORE_GENRE = [
        "Hip-hop",
        "Rock",
        "Metal",
        "Ambient",
        "Jazz",
        "Punk",
        "Blues",
        "Pop",
        "Rap",
        "Electronic",
        "Country",
        "Swing",
        "Dance",
        "House",
        "Funk",
        "Dub",
        "Soul",
        "Techno",
        "Disco",
        "Grunge",
        "Djent",
        "Noise",
        "Polka",
        "Humppa",
        "Rhythm",
        "Boogie",
        "Phonk",
        "Fusion",
        "Experimental"
    ]

    @classmethod
    def generate_genre(cls):
        genre = random.choice(cls.TEMPLATE)
        cache = {}
        while match := cls.tpl_re.search(genre):
            choices = set(getattr(cls, match.group(1)))
            choices -= cache.get(match.group(1), set())
            choice = random.choice(list(choices))
            cache.setdefault(match.group(1), set()).add(choice)
            genre = genre.replace(match.group(0), choice, 1)
        genre = genre.replace("aa", "a")
        return genre


@tree.command()
async def genre(interaction: discord.Interaction):
    """
    Generate a random music genre.
    """
    embed = discord.Embed(
        color=discord.Color.random(),
        title=GenreGen.generate_genre().upper(),
    )
    return await interaction.response.send_message(
        "Consider writing some...", embed=embed
    )


@client.event
async def on_ready():
    print("Ready!")
    await tree.sync()


client.run(os.getenv("GENREBOT_TOKEN"))
