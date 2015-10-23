# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase
from gaiatest.apps.vaani.app import Vaani
from gaiatest.apps.music.app import Music
import time


class TestVaaniEmpty(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)

    def test_empty_music(self):
        """https://moztrap.mozilla.org/manage/case/3668/"""

        # Requires there to be no songs on SDCard which is the default
        vaani_app = Vaani(self.marionette)
        vaani_app.launch()
        self.marionnette.execute_script("myDebug.enable(‘*’)")
        print "5 seconds to manually start begins."
        time.sleep(5)
        print "5 seconds to manually test is over."
        music_app = Music(self.marionette)
        music_app.wait_to_be_displayed()
