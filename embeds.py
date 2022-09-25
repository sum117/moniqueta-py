import random
from enum import Enum
from discord import Embed, User, ClientUser
"""
Creates a character embed.
"""

class ErrorMessage(Enum):
    NO_EMBED_DESCRIPTION = "Nenhuma descrição de embed foi providenciada."
class StaticContent(Enum):
    FOOTER_TEXT = 'Trazido a você por Tonabrix1 & sum117'

def create_char_embed(client_user: ClientUser, user:User, image:str = None, embed_description:str = None) -> None:

    #TODO: Database fetching right here (later).
    # char_name = fetchFromDatabase(user_id).name
    # ... etc

    #Variables
    char_name: str = 'Tonabrix1'
    char_title: str = 'The God of Cat Girls, Vaginas, and Time' #God fucking damnit <- the second developer didn't write that nor does he agree with what is stated
    char_image: str = 'https://github.com/tonabrix1.png'
    char_race_color: str = "#000"
    char_description: str = """"
                            The day he was born, immediately upon coming out of the womb he was met with the scorn of the males around him, his incredible
                            handsomeness and massive cock lead them to jealousy and contempt.  However, his great power of perserverance brought him far
                            from his humble beginnings as simply the god of time.  One day Tonabrix1 was walking down the road when he saw a short cloaked beggar,
                            due to his kind nature he offered the beggar some food in exchange for sex.  The beggar happily agreed and removed their hood to reveal two fluffy
                            cat-like ears.  Legend has it that her tight catussy allowed him to ascend to a new level of divinity on the spot, permitting him dominion over not only
                            the beloved race of cat girls (who have difficulty repopulating due to their inability to produce male progeny), but also vaginas; the first door through which
                            all (mammalian) beings must walk in order to become full-fledged individuals.  To this very day he watches over the lands in a voyueristic manner,
                            using the vaginas of all woman as if they were his own eyes to peer out into the world.
                            """

    #Embed building
    embed: Embed = Embed()
    embed.set_author(name= user.username, icon_url=user.display_avatar.url)
    embed.set_footer(text= StaticContent.FOOTER_TEXT, icon_url=client_user.avatar.url)
    embed.color = char_race_color
    embed.description = embed_description or ErrorMessage.NO_EMBED_DESCRIPTION

    #Image is included if it was supplied by the user in their post.
    if image is not None:
        embed.set_image(url=image)

    #Random chance of overwritten description (tiny developer easter-egg).
    random_number = random.randInt(0,100)
    if random_number is 1:
        embed.description = char_description

