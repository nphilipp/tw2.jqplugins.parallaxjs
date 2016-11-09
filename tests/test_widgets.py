from unittest import TestCase
from sieve.operators import assert_eq_xml

from tw2.jqplugins.parallaxjs import ParallaxImageWidget


class TestWidgets(TestCase):

    def test_widget(self):
        test = ParallaxImageWidget()
        assert_eq_xml(test.display(min_height="400px", image_src="foo.jpg"),
                      """<div data-parallax="scroll"
                      style="background:transparent;min_height:400px"
                      data-image-src="foo.jpg"></div>""")
