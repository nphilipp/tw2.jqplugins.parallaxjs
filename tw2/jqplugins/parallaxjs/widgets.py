# -*- coding: utf-8 -*-
#
# tw2.jqplugins.parallaxjs.widgets
#
# Copyright © 2016 Nils Philippsen <nils@tiptoe.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import absolute_import

from tw2.core import JSSource, Param, Widget
from tw2.jquery import jquery_js

from .resources import parallaxjs_js

__all__ = ('ParallaxImageWidget',)


# work around parallax.js problem with jQuery 3.1.x
# https://github.com/pixelcog/parallax.js/issues/166
workaround_js = JSSource(src="""$(window).on('load', function(){
    $('[data-parallax="scroll"]').parallax();
})""")


class ParallaxImageWidget(Widget):

    resources = [jquery_js, parallaxjs_js, workaround_js]

    template = "tw2.jqplugins.parallaxjs.templates.parallax_image"

    image_src = Param(
        "The image to be shown with the parallax effect.",
        attribute=True, view_name='data-image-src',
    )

    min_height = Param("The minimum height of the outer div.")

    def prepare(self):
        super(ParallaxImageWidget, self).prepare()

        self.safe_modify('attrs')
        s_parts = (
            "background:transparent",
            "min-height:" + self.min_height if self.min_height else None,
            self.attrs.get('style'))
        self.attrs['style'] = ";".join(x for x in s_parts if x)
