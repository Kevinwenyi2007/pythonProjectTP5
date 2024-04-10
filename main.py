import random

import arcade

import game_state

#import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = 0
       self.paper = 1
       self.scissors = 2
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = GameState.NOT_STARTED

   def setup(self):
       self.player = arcade.Sprite('assets/faceBeard.png', 0.5)
       self.computer = arcade.Sprite('assets/compy.png', 0.5)
       self.players = arcade.SpriteList()
       self.rock = 0
       self.paper = 1
       self.scissors = 2
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None



   def validate_victory(self):
        if self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.PAPER :
            self.player_won_round = False
        if self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
            self.player_won_round = True
        if self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
            self.player_won_round = True
        if self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS :
            self.player_won_round = False
        if self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK:
            self.player_won_round = False
        if self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
            self.player_won_round = True
        if self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.SCISSORS:
            self.draw_round = True
        if self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.PAPER:
            self.draw_round = True
        if self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.ROCK:
            self.draw_round = True



   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
       pass

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       pass


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):
       if self.game_state == game_state.GameState.NOT_STARTED:
           arcade.draw_text('appuyer sur espace pour commencer le jeu',
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5,
                            arcade.color.WHITE,
                            60,
                            width=SCREEN_WIDTH,
                            align="center")
       if self.game_state == game_state.GameState.ROUND_ACTIVE:
           arcade.draw_text('appuyer sur un image pour faire une attaque',
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5,
                            arcade.color.WHITE,
                            50,
                            width=SCREEN_WIDTH,
                            align="center")
       if self.game_state == game_state.GameState.ROUND_DONE:
           if self.player_score == 1 and self.computer_score == 0:
                arcade.draw_text('vous avez gagne la ronde! appuyer sur espace pour recommencer',
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 0.5,
                            arcade.color.BLACK_BEAN,
                            30,
                            width=SCREEN_WIDTH,
                            align="center")
           else:
               arcade.draw_text('ordinateur a gagne la ronde! appuyer sur espace pour recommencer',
                                0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 0.5,
                                arcade.color.BLACK_BEAN,
                                30,
                                width=SCREEN_WIDTH,
                                align="center")
       if self.game_state == game_state.GameState.GAME_OVER:
           if self.player_score == 3 and self.computer_score < 3:
                arcade.draw_text('vous avez gagne la partie! appuyer sur espace pour recommencer',
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 0.25,
                            arcade.color.BLACK_BEAN,
                            30,
                            width=SCREEN_WIDTH,
                            align="center")
           else:
               arcade.draw_text('ordinateur a gagne la partie! appuyer sur espace pour recommencer',
                                0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 0.25,
                                arcade.color.BLACK_BEAN,
                                30,
                                width=SCREEN_WIDTH,
                                align="center")

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       player = arcade.Sprite('assets/faceBeard.png', 0.5)
       player.center_x = 200
       player.center_y =200
       player.draw()

       computer = arcade.Sprite('assets/compy.png', 0.5)
       computer.center_x = 700
       computer.center_y = 200
       computer.draw()

       self.rock = AttackAnimation(AttackType.ROCK)
       self.paper = AttackAnimation(AttackType.PAPER)
       self.scissors = AttackAnimation(AttackType.SCISSORS)



       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       #self.draw_instructions()
       #self.players.draw()
       #self.draw_possible_attack()
       #self.draw_scores()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):
        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack_chosen == True:
            pc_attack = random.randint(0, 2)
            if pc_attack == 0:
                self.computer_attack_type = AttackType.ROCK
            elif pc_attack == 1:
                self.computer_attack_type = AttackType.PAPER
            else:
                self.computer_attack_type = AttackType.SCISSORS
            self.validate_victory()
            if self.player_won_round == True:
                self.player_score += 1
            if self.player_won_round == False and self.draw_round == False:
                self.computer_score += 1
            if self.player_score == 3 or self.computer_score == 3:
                self.game_state = GameState.GAME_over

       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)


   def on_key_press(self, key, key_modifiers):
       if self.game_state == GameState.NOT_STARTED:
           self.game_state = GameState.ROUND_ACTIVE
       elif self.game_state == GameState.ROUND_DONE:
           self.reset_round()
           self.game_state = GameState.ROUND_ACTIVE
       elif self.game_state == GameState.GAME_OVER:
           self.game_state = GameState.ROUND_ACTIVE
           self.setup()

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):
       if self.rock.collides_with_point((x, y)):
           self.player_attack_type = AttackType.ROCK
           self.player_attack_chosen = True

       if self.paper.collides_with_point((x, y)):
           self.player_attack_type = AttackType.PAPER
           self.player_attack_chosen = True

       if self.scissors.collides_with_point((x, y)):
           self.player_attack_type = AttackType.SCISSORS
           self.player_attack_chosen = True
       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True



def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()

