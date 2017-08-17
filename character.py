import figures

MOVE_SPEED = 2


class Character(figures.Drawable):
    def __init__(self, x, y):
        self.body_parts = {'head': figures.Circle(x, y - 10, 10),
                           'torso': figures.Line(figures.Point(x, y), figures.Point(x, y + 50)),
                           'l_arm': figures.Line(figures.Point(x, y), figures.Point(x - 20, y + 40)),
                           'r_arm': figures.Line(figures.Point(x, y), figures.Point(x + 20, y + 40)),
                           'l_leg': figures.Line(figures.Point(x, y + 50), figures.Point(x - 20, y + 90)),
                           'r_leg': figures.Line(figures.Point(x, y + 50), figures.Point(x + 20, y + 90))}
        self.trigger_up = 0
        self.x_move = 0

    def draw(self, game_display):
        for body_part in self.body_parts.values():
            body_part.draw(game_display)

    def wave_arms(self, game_display):
        if self.body_parts['l_arm'].end.y == self.body_parts['head'].y - 15:
            self.trigger_up = 1
        if self.body_parts['l_arm'].end.y == self.body_parts['torso'].end.y - 5:
            self.trigger_up = 0
        if self.trigger_up == 0:
            self.body_parts['l_arm'].end.x += -0.314
            self.body_parts['l_arm'].end.y += -1
            self.body_parts['r_arm'].end.x += 0.314
            self.body_parts['r_arm'].end.y += -1
            self.draw(game_display)
        if self.trigger_up == 1:
            self.body_parts['l_arm'].end.x += 0.314
            self.body_parts['l_arm'].end.y += 1
            self.body_parts['r_arm'].end.x += -0.314
            self.body_parts['r_arm'].end.y += 1
            self.draw(game_display)

    def move(self, left, right):
        if left:
            self.x_move = -MOVE_SPEED

        if right:
            self.x_move = MOVE_SPEED

        if not (left or right):
            self.x_move = 0

        self.body_parts['head'].x += self.x_move
        self.body_parts['torso'].start.x += self.x_move
        self.body_parts['torso'].end.x += self.x_move
        self.body_parts['l_arm'].start.x += self.x_move
        self.body_parts['l_arm'].end.x += self.x_move
        self.body_parts['r_arm'].start.x += self.x_move
        self.body_parts['r_arm'].end.x += self.x_move
        self.body_parts['l_leg'].start.x += self.x_move
        self.body_parts['l_leg'].end.x += self.x_move
        self.body_parts['r_leg'].start.x += self.x_move
        self.body_parts['r_leg'].end.x += self.x_move
