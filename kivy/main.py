#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    score = NumericProperty(0)
    pass

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty()
    player = ObjectProperty()
    #score = NumericProperty()

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        if (self.ball.y < self.player.top) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        #if self.ball.y < self.player.top and (self.player.x < self.ball.x < self.player.right):
        #    print(self.player.score)
        #    self.player.score += 1
        #    #self.serve_ball()

        if self.ball.y < self.player.top:
            if self.player.x < self.ball.x < self.player.right:
                #print(self.player.score)
                self.player.score += 1
                #self.serve_ball()

        

    def on_touch_move(self, touch):
        
        if touch.x < 50:
            self.player.x = touch.x
        if touch.x > 50:
            self.player.right = touch.x


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    PongApp().run()
    
