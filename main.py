def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 2 2 2 2 . . . 
                    . . . . . . . 2 2 4 4 4 2 2 . . 
                    . . . . 2 2 5 5 4 5 5 1 5 5 2 . 
                    . . 3 3 5 5 5 4 1 1 5 5 1 5 2 . 
                    . . 1 1 5 5 1 1 1 1 1 1 1 9 2 . 
                    . . 3 3 2 2 5 5 5 1 1 1 9 9 2 . 
                    . . . . . . 2 2 4 4 4 1 2 2 . . 
                    . . . . . . . . . 2 2 2 2 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        100,
        0)
    projectile.set_velocity(100, 0)
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global statusbar
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.set_label("HP")
    statusbar.set_color(7, 2)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global myEnemy
    sprites.destroy(myEnemy, effects.fire, 500)
    sprites.destroy(myEnemy)
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.IN_BACKGROUND)
    myEnemy = sprites.create(img("""
            . . . . . . . e e e e e . . . . 
                    . . . . . e e 2 2 2 2 2 e . . . 
                    . . . . e e 2 2 2 2 2 2 2 e . . 
                    . . . . e 9 4 2 2 2 2 2 4 b e . 
                    . . e e 9 9 4 4 2 2 2 2 4 9 b e 
                    . e 2 2 9 9 4 4 4 2 2 2 4 9 9 e 
                    e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                    e 2 2 2 9 9 e e e e e e e 9 9 e 
                    e 2 2 2 9 b e b b b e b e b 9 e 
                    e 2 e e e e b b b b e b b e b e 
                    e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                    e 3 3 e e e e e e e e e e e e e 
                    e e e e e e e e e e e e e e e e 
                    e e e e f f f e e e e f f f e e 
                    . e e f b c c f e e f b c c f . 
                    . . . . b b f . . . . b b f . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        [img("""
                . . . . . . . e e e e e . . . . 
                        . . . . . e e 2 2 2 2 2 e . . . 
                        . . . . e e 2 2 2 2 2 2 2 e . . 
                        . . . . e 9 4 2 2 2 2 2 4 b e . 
                        . . e e 9 9 4 4 2 2 2 2 4 9 b e 
                        . e 2 2 9 9 4 4 4 2 2 2 4 9 9 e 
                        e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                        e 2 2 2 9 9 e e e e e e e 9 9 e 
                        e 2 2 2 9 b e b b b e b e b 9 e 
                        e 2 e e e e b b b b e b b e b e 
                        e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                        e 3 3 e e e e e e e e e e e e e 
                        e e e e e e e e e e e e e e e e 
                        e e e e f f f e e e e f f f e e 
                        . e e f b c c f e e f b c c f . 
                        . . . . b b f . . . . b b f . .
            """),
            img("""
                . . . . . . . e e e e e . . . . 
                        . . . . . e e 2 2 2 2 2 e . . . 
                        . . . . e e 2 2 2 2 2 2 2 e . . 
                        . . . . e 9 4 4 4 2 2 2 4 b e . 
                        . . e e 9 9 4 4 4 4 2 2 4 9 b e 
                        . e 2 2 9 9 4 4 4 4 4 2 4 9 9 e 
                        e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                        e 2 2 2 9 9 e e e e e e e 9 9 e 
                        e 2 2 2 9 b e b b b e b e b 9 e 
                        e 2 e e e e b b b b e b b e b e 
                        e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                        e 3 3 e e e e e e e e e e e e e 
                        e e e e e e e e e e e e e e e e 
                        e e e e f f f e e e e f f f e e 
                        . e e f f f b f e e f f f b f . 
                        . . . . c b b . . . . c b b . .
            """),
            img("""
                . . . . . . . e e e e e . . . . 
                        . . . . . e e 2 2 2 2 2 e . . . 
                        . . . . e e 2 2 2 2 2 2 2 e . . 
                        . . . . e 9 4 2 2 2 4 4 4 b e . 
                        . . e e 9 9 4 2 2 2 4 4 4 9 b e 
                        . e 2 2 9 9 4 4 2 2 2 4 4 9 9 e 
                        e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                        e 2 2 2 9 9 e e e e e e e 9 9 e 
                        e 2 2 2 9 b e b b b e b e b 9 e 
                        e 2 e e e e b b b b e b b e b e 
                        e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                        e 3 3 e e e e e e e e e e e e e 
                        e e e e e e e e e e e e e e e e 
                        e e e e f f f e e e e f f f e e 
                        . e e f c b b f e e f c b b f . 
                        . . . . f f f . . . . f f f . .
            """),
            img("""
                . . . . . . . e e e e e . . . . 
                        . . . . . e e 2 2 2 2 2 e . . . 
                        . . . . e e 2 2 2 2 2 2 2 e . . 
                        . . . . e 9 4 2 2 2 2 2 4 b e . 
                        . . e e 9 9 4 2 2 2 2 2 4 9 b e 
                        . e 2 2 9 9 4 4 2 2 2 2 4 9 9 e 
                        e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                        e 2 2 2 9 9 e e e e e e e 9 9 e 
                        e 2 2 2 9 b e b b b e b e b 9 e 
                        e 2 e e e e b b b b e b b e b e 
                        e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                        e 3 3 e e e e e e e e e e e e e 
                        e e e e e e e e e e e e e e e e 
                        e e e e f f f e e e e f f f e e 
                        . e e f b b c f e e f b b c f . 
                        . . . . c f f . . . . c f f . .
            """)],
        100,
        True)
    myEnemy.follow(mySprite, 95)
    myEnemy.set_position(164, 57)
    myEnemy.set_stay_in_screen(True)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

statusbar: StatusBarSprite = None
projectile: Sprite = None
myEnemy: Sprite = None
mySprite: Sprite = None
game.splash("Press \"A\"")
scene.set_background_image(img("""
    4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444111111111114444444444444444444444444444444444444441111444444444444444444444444444444444444444444111111111111
        44444444444444444444444444444444444444444444444444441ddddddddd14444444444444444444444444441111144444441dd11444444444444444444444444444444444444444441dddddddddd1
        44444444444444444444444444444411111444444444444444441ddddddddd14444444444444444444444444441ddd144444441ddd1444444444444444444441111444444444444444441dddddddddd1
        4444444444444444444444444444411ddd1144444444444444441d11dddddd14444444444444444444444444111ddd111444411ddd1144444444444444444411dd1144444444444444441dd1d1ddddd1
        444444444444444444444444444411ddddd144444444444444441ddddddd1d144444444111444444111111141ddddddd144441ddddd14444444444444444111dddd144444444444444441dddddd11dd1
        44444411114444444444444444441dddddd144411144444444441ddddddddd1444444411d14444441ddddd141ddddddd144411ddddd114444444444444441dddddd144411114444444441dddddddddd1
        4444441dd14444444444444444441ddd1d114441d144444444441ddddddddd144444441dd14444441ddddd141ddddddd144411ddddd114444444444444441ddd1d114441dd14444444441dddd1ddddd1
        1111111dd14111111441111111111dddddd14111d111444444441ddddddd1d111111111dd14444441ddddd111d11dddd14111ddddddd11111441111111111dddddd14411dd11444444441ddddddd1dd1
        d11dddddd141d1dd1441ddddddddddd1ddd111ddddd1111111111ddddddd1d11d11ddd1dd144444411dd1dd11ddddddd141dddddddddd1dd1441ddddddddddddd1d1111dddd1141111111dddddd11ddd
        dddd1dddd141dddd14411d1dd1ddddddddd111ddddd111dd1dd11ddddddddd11dddd1d1dd11111111dddddd11dd1dddd141ddddddddddddd1441dd1ddd1dddddddd1111dddd1141d11dd1ddddddddddd
        ddddddddd111dd1d1111dddddddddddddddd11dddddd11ddddddddddddddddd1ddddddddd11d11d11ddddddddddddddd141ddddddddddd1d1111dddddddddddddddd11dddddd111ddddddddddddddddd
        d11d1dddd1ddddddd1dd1d1ddddddddddddd11ddddddd1dddd11ddddddddddddd1111ddddddd1ddd11dd1ddddddddddd111ddddddddddddddd1ddd1ddddddddddddd11ddddddd111d11ddddddddddddd
        ddddddddd1ddddddd1dddddddddddddddddddd1dddddd11ddddddddddddddddddddddddddddd1ddd1ddddddddddddddd1d1ddddddddddddddd1dddddddddddddddddddddddddd1dddddddddddddddddd
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc
        11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc
        11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d
        11ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d1111111
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        1111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd111
        111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbcbbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d111d1111d111dd11dd
        d11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11d
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d
        11ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d1111111
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbccbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        cccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
        bccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccc
        ccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbb
        bbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddb
        bbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111dd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc
        dbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
mySprite = sprites.create(img("""
        ..............ccccccccc........
            ............cc555555555cc......
            ...........c5555555555555c.....
            ..........c55555555555555dc....
            .........c555555555555b5bdc....
            .........555bc1555555555bdcccc.
            ........c555ccc55555555bbdccddc
            ........c555bcb5555555ccddcdddc
            .......c555555555551ccccddbdddc
            .......c555555b555c1cccbddbbdbc
            .......c5555555bbc33333ddddbcc.
            .......c555555555bc333555ddbc..
            .......c5555555555555555555c...
            .......cd555555555555cccc555c..
            .......cd55555555555c555c555c..
            .......cdd555555555b5555b555c..
            .......cddd55555ddbb555bb555c..
            .......cdddd55555555555b5555c..
            .......cddddd5555555ddb5555dc..
            c......cdddddd555555555555dcc..
            cc...ccddddddd555555555555dc...
            cdccccdddddd555555d55555ddcc...
            cdddddddddbd5555555ddddddccccc.
            ccdddddddbb55555555bddddccbddc.
            .ccddddddbd55555555bdddccdddc..
            ..cccddddbd5555555cddcccddbc...
            ....ccccccd555555bcccc.cccc....
            .........cc555555bc............
            .........cc55555555c...........
            ..........cccccccccc...........
    """),
    SpriteKind.player)
mySprite.set_position(3, 51)
mySprite.set_stay_in_screen(True)
animation.run_image_animation(mySprite,
    [img("""
            ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb555555ff155555c
                ......cb55555555ff55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb13bbc.
                ...cccd55ddddd555b3335c.
                .....bdddddddddd55b335c.
                ..cccdddddb55bbddd5555c.
                ..cccdddddb555bbbbcccc..
                ...ccddddddb5555cbcdc...
                ccccbdddddd5cb55cbcc....
                cddddddddd5555ccbbc.....
                .cddddddbdd555bbbcc.....
                ..ccdddbbbdd55cbcdc.....
                ....ccbbcbddddccdddcc...
                ......cccdd555dcccccc...
                ........cccccccc........
        """),
        img("""
            .........ccc............
                .........cccccccc.......
                ......cc..cc55555cc.....
                ......cccc555555555c....
                ......ccb55555555555c...
                ...cc..b55555ff155555c..
                ...cccb5555555ff55d55c..
                ....ccb55555d55555555c..
                .....b55555d5555d5555c..
                ..cc.b555ddd55555bbbbc..
                ..cccd55ddddd5555d555c..
                ...ccdd5dbdddbbbd555c...
                ....bdddb555bbbbbccc....
                ..cccdddb555cbbbbbbc....
                ...ccddddb555cbbbbbbc...
                ....cdddddb555cbbbbbc...
                ...ccddddddb55cbbbbbcc..
                ..ccbddddd55bcbbbbbbcc..
                ccdddddddd5555bbbbbbc...
                cdddddddbdd555bbbbbc....
                .ccddddbbbdd55cbbccc....
                ...cccbbcbddddccdddcc...
                ......cccdd555dcccccc...
                ........cccccccc........
        """),
        img("""
            ........ccc.............
                ........cccccccc........
                .....cc..cc55555cc......
                .....cccc555555555c.....
                .....ccb55555555555c....
                ...cc.b5555bcc555555c...
                ...ccb55555555c55d55c...
                ....cb5555dd55555555c...
                .....5555dd5555d5555c...
                ..cc.555dd555555dbbbc...
                ..ccc55ddd555555d555c...
                ...ccd5dbdd5555d555c....
                ....bdddb555bbbbbccc....
                ..cccdddb555cbbbbbbbc...
                ...ccddddb555cbbbbbbbc..
                ....cdddddb555cbbbbbbc..
                ...ccddddddb55cbbbbbbcc.
                ...cbddddd55bcbbbbbbbcc.
                ..cbdddddd5555bbbbbbbc..
                .cddddddbdd555bbbbbbc...
                cddddddbbbdd55cbbccc....
                ccccccbbcbddddccdddcc...
                ......cccdd555dcccccc...
                ........cccccccc........
        """),
        img("""
            ........................
                ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb55555bcc555555c
                ......cb555555555c55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb1bbbc.
                ....ccd55ddddd5bbbb335c.
                ...ccbdddddddd5bbbb335c.
                .ccccddddddddd55bbb335c.
                cdcccdddddb55bb5bb3335c.
                cddbddddddb555bb5b3335c.
                cddddddddddb5555b53335c.
                ccddddddbd55bb55c5555c..
                .ccddddbbbdd55cccbccc...
                ...ccbbbcbddddccdddc....
                .....ccccdd555dccccc....
                ........cccccccc........
        """),
        img("""
            ........................
                ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb55555bcc555555c
                ......cb555555555c55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb1bbbc.
                ....ccd55ddddd5bbbb335c.
                ...ccbdddddddd5bbbb335c.
                .ccccddddddddd55bb3335c.
                cdcccdddddb55bb55b3335c.
                cddbddddddb555bb553335c.
                cddddddddddb5555b5555c..
                ccddddddbd55bb55cbccc...
                .ccddddbbbdd55ccbbc.....
                ...ccbbbcbddddccdddc....
                .....ccccdd555dccccc....
                ........cccccccc........
        """),
        img("""
            ........................
                ........................
                ........................
                ...........ccc..........
                ...........cccc.........
                .......ccc..ccccccc.....
                .......cccccc555555cc...
                ........ccb5555555555c..
                .....cc..b555555555555c.
                .....cccb55555bcc555555c
                ......cb555555555c55d55c
                ......b5555555555555555c
                ...cc.b555dd5555bb1bbbc.
                ....ccd55ddddd55bbb335c.
                ...ccbddddddddd5bb3335c.
                .ccccdddddddddd55b3335c.
                cdcccdddddb55bbd553335c.
                cddbddddddb555bb55555c..
                cddddddddddb5555bbccc...
                ccddddddbd55bb55cbc.....
                .ccddddbbbdd55ccbdc.....
                ...ccbbbcbddddccdddc....
                .....ccccdd555dccccc....
                ........cccccccc........
        """)],
    500,
    True)
controller.move_sprite(mySprite, 0, 100)
myEnemy = sprites.create(img("""
        . . . . . . . e e e e e . . . . 
            . . . . . e e 2 2 2 2 2 e . . . 
            . . . . e e 2 2 2 2 2 2 2 e . . 
            . . . . e 9 4 2 2 2 2 2 4 b e . 
            . . e e 9 9 4 4 2 2 2 2 4 9 b e 
            . e 2 2 9 9 4 4 4 2 2 2 4 9 9 e 
            e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
            e 2 2 2 9 9 e e e e e e e 9 9 e 
            e 2 2 2 9 b e b b b e b e b 9 e 
            e 2 e e e e b b b b e b b e b e 
            e e 3 3 e e 2 2 2 2 e 2 2 e e e 
            e 3 3 e e e e e e e e e e e e e 
            e e e e e e e e e e e e e e e e 
            e e e e f f f e e e e f f f e e 
            . e e f b c c f e e f b c c f . 
            . . . . b b f . . . . b b f . .
    """),
    SpriteKind.enemy)
animation.run_image_animation(myEnemy,
    [img("""
            . . . . . . . e e e e e . . . . 
                . . . . . e e 2 2 2 2 2 e . . . 
                . . . . e e 2 2 2 2 2 2 2 e . . 
                . . . . e 9 4 2 2 2 2 2 4 b e . 
                . . e e 9 9 4 4 2 2 2 2 4 9 b e 
                . e 2 2 9 9 4 4 4 2 2 2 4 9 9 e 
                e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                e 2 2 2 9 9 e e e e e e e 9 9 e 
                e 2 2 2 9 b e b b b e b e b 9 e 
                e 2 e e e e b b b b e b b e b e 
                e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                e 3 3 e e e e e e e e e e e e e 
                e e e e e e e e e e e e e e e e 
                e e e e f f f e e e e f f f e e 
                . e e f b c c f e e f b c c f . 
                . . . . b b f . . . . b b f . .
        """),
        img("""
            . . . . . . . e e e e e . . . . 
                . . . . . e e 2 2 2 2 2 e . . . 
                . . . . e e 2 2 2 2 2 2 2 e . . 
                . . . . e 9 4 4 4 2 2 2 4 b e . 
                . . e e 9 9 4 4 4 4 2 2 4 9 b e 
                . e 2 2 9 9 4 4 4 4 4 2 4 9 9 e 
                e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                e 2 2 2 9 9 e e e e e e e 9 9 e 
                e 2 2 2 9 b e b b b e b e b 9 e 
                e 2 e e e e b b b b e b b e b e 
                e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                e 3 3 e e e e e e e e e e e e e 
                e e e e e e e e e e e e e e e e 
                e e e e f f f e e e e f f f e e 
                . e e f f f b f e e f f f b f . 
                . . . . c b b . . . . c b b . .
        """),
        img("""
            . . . . . . . e e e e e . . . . 
                . . . . . e e 2 2 2 2 2 e . . . 
                . . . . e e 2 2 2 2 2 2 2 e . . 
                . . . . e 9 4 2 2 2 4 4 4 b e . 
                . . e e 9 9 4 2 2 2 4 4 4 9 b e 
                . e 2 2 9 9 4 4 2 2 2 4 4 9 9 e 
                e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                e 2 2 2 9 9 e e e e e e e 9 9 e 
                e 2 2 2 9 b e b b b e b e b 9 e 
                e 2 e e e e b b b b e b b e b e 
                e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                e 3 3 e e e e e e e e e e e e e 
                e e e e e e e e e e e e e e e e 
                e e e e f f f e e e e f f f e e 
                . e e f c b b f e e f c b b f . 
                . . . . f f f . . . . f f f . .
        """),
        img("""
            . . . . . . . e e e e e . . . . 
                . . . . . e e 2 2 2 2 2 e . . . 
                . . . . e e 2 2 2 2 2 2 2 e . . 
                . . . . e 9 4 2 2 2 2 2 4 b e . 
                . . e e 9 9 4 2 2 2 2 2 4 9 b e 
                . e 2 2 9 9 4 4 2 2 2 2 4 9 9 e 
                e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                e 2 2 2 9 9 e e e e e e e 9 9 e 
                e 2 2 2 9 b e b b b e b e b 9 e 
                e 2 e e e e b b b b e b b e b e 
                e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                e 3 3 e e e e e e e e e e e e e 
                e e e e e e e e e e e e e e e e 
                e e e e f f f e e e e f f f e e 
                . e e f b b c f e e f b b c f . 
                . . . . c f f . . . . c f f . .
        """)],
    100,
    True)
myEnemy.follow(mySprite, 75)
myEnemy.set_position(160, 65)
myEnemy.set_stay_in_screen(True)
info.set_score(0)

def on_forever():
    effects.blizzard.start_screen_effect(5000)
    scene.set_background_color(4)
    game.set_game_over_playable(True, music.melody_playable(music.wawawawaa), False)
    game.set_game_over_effect(True, effects.confetti)
forever(on_forever)
