from tethys_sdk.base import TethysAppBase, url_map_maker


class JeffDerricott(TethysAppBase):
    """
    Tethys app class for Jeff Derricott.
    """

    name = 'Jeff Derricott'
    index = 'jeff_derricott:home'
    icon = 'jeff_derricott/images/paladeo.gif'
    package = 'jeff_derricott'
    root_url = 'jeff-derricott'
    color = '#72bdf9'
    description = 'This app is about me, and a place to see my Mockups for Motus.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='jeff-derricott',
                controller='jeff_derricott.controllers.home'
            ),
            UrlMap(
                name='Mockups',
                url='Mockups',
                controller='jeff_derricott.controllers.Mockups'
            ),
        )

        return url_maps
