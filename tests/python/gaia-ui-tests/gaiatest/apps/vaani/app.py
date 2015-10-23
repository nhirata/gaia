# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette_driver import expected, By, Wait

from gaiatest.apps.base import Base
from gaiatest.apps.music.regions.list_view import AlbumsView, ArtistsView, SongsView


class Vaani(Base):

    name = 'Vaani'
    manifest_url = 'app://306baf44-4aaf-ea4a-ac8d-aba873770063/manifest.webapp'



