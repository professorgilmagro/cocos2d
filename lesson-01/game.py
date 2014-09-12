#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Gilmar S. Santos <gilmar.pythonman@outlook.com>

import cocos

from cocos.actions import *

COLOR_BLUE = (0, 64, 224, 255)


class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        super(HelloWorld, self).__init__(*COLOR_BLUE)

        label = cocos.text.Label(
            u"Olá mundo",
            font_name="Arial",
            font_size=40,
            anchor_x="center",
            anchor_y="center"
        )

        label.position = 320, 240
        sprite = cocos.sprite.Sprite("grossini_one.png")
        sprite.position = 320, 280

        scale = ScaleBy(3, duration=2)

        sprite.do(Repeat(Reverse(scale) + scale))
        label.do(RotateBy(360, duration=5))

        self.add(label)
        self.add(sprite, z=1)

cocos.director.director.init()

layer = HelloWorld()
layer.do(RotateBy(360, duration=10))

scene = cocos.scene.Scene(layer)
cocos.director.director.run(scene)
