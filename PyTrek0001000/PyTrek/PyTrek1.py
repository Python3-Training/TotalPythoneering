﻿import random

import sys
sys.path.append('..')

import PyTrek.TrekStrings as TrekStrings
from PyTrek.Console import Con
from PyTrek.ShipKlingon import ShipKlingon as ShipKlingon
from PyTrek.ShipEnterprise import ShipEnterprise
from PyTrek.ShipStarbase import ShipStarbase
from PyTrek.Calculators import Calc
from PyTrek.Controls import Control
from PyTrek.Reports import Stats
from PyTrek.Points import *
from PyTrek.Quips import Quips
from PyTrek.MapGame import *


class Game(Con):

    def __init__(self):
        self.is_testing = False
        self.is_cloked  = False # unable to be fired-upon
        self.game_map = GameMap()
        self.enterprise = ShipEnterprise()
        self.star_date = 0
        self.time_remaining = 0
        self.destroyed = False

    def move_to(self, dest):
        '''
        Move the player to a nav, or a sub,
        destination. Handles docking, random 
        warp-in placement, as well as deliberate
        collisions / rammming.
        
        Returns final resting coordinate on success.
        Raises ErrorEnterpriseCollision on yikes.
        '''
        pos = self.game_map._go_to(dest)
        area = self.game_map.pw_area()
        was_docked = self.enterprise.docked
        self.enterprise.docked = False
        for p in area._pieces:
            if p.glyph == Glyphs.STARBASE:
                for point in Calc.surrounding(pos):
                    if  p.xpos == point[0] and \
                        p.ypos == point[1]:
                            self.enterprise.docked = True
                            ShipStarbase.dock_enterprise(self.enterprise)
        if was_docked and self.enterprise.docked == False:
            ShipStarbase.launch_enterprise(self.enterprise)
        return pos

    def game_on(self):
        '''
        See if the game is still running.
        '''
        running = self.enterprise.energy > 0 and not \
        self.destroyed and self.game_map.game_klingons > 0 and \
        self.time_remaining > 0
        return running

    def run(self):
        '''
        The game loop - runs until the game is over.
        '''
        self.show_strings(TrekStrings.LOGO_TREKER)
        self.star_date = random.randint(2250, 2300)
        self.time_remaining = random.randint(40, 45)
        self.destroyed = False
        stars     = random.randint(500, 700) # 4096 = ALL
        aliens    = random.randint(14, 24)
        starbases = random.randint(6, 8)
        self.game_map.randomize(starbases, stars, aliens)
        dest = WarpDest(64, 0)
        self.move_to(dest)
        self.game_map.get_area(64).name = 'Outer Limits'
        self.print_mission()

        self.show_strings(TrekStrings.HELM_CMDS)
        running = True
        try:
            while self.game_on():
                if not self.command_prompt():
                    break
                if self.is_testing:
                    self.destoryed = False
                    ShipStarbase.dock_enterprise(self.enterprise)
                    ShipStarbase.launch_enterprise(self.enterprise)
                    self.enterprise.shield_level = 1000
                    
        except ErrorEnterpriseCollision as ex:
            if ex.glyph == Glyphs.KLINGON:
                self.display("You flew into a KLINGON!")
            if ex.glyph == Glyphs.STARBASE:
                self.display("You flew into a STARBASE?")
            if ex.glyph == Glyphs.STAR:
                self.display("You flew into a STAR?")
            self.destroyed = True
        self.display()
        Stats.show_exit_status(self)
        self.display()
        if self.destroyed == True:
            self.display(Quips.jibe_fatal_mistake())
        self.display()
        return False

    def command_prompt(self):
        command = self.read("Enter command: ").strip().lower()
        self.display()
        if command == "nav":
            Calc.warp_navigation(self)
        if command == "sub":
            Calc.sublight_navigation(self)
        elif command == "srs":
            self.enterprise.short_range_scan(self)
        elif command == "lrs":
            self.enterprise.long_range_scan(self)
        elif command == "pha":
            Control.phasers(self)
        elif command == "tor":
            Control.torpedos(self)
        elif command == "she":
            Control.shields(self)
        elif command == "com":
            Control.computer(self)
        elif command.startswith('qui') or command.startswith('exi'):
            return False
        else:
            self.show_strings(TrekStrings.HELM_CMDS)
        return True

    def print_mission(self):
        self.display("Mission: Destroy {0} Klingon ships in {1} stardates with {2} starbases.".format(
            self.game_map.game_klingons, self.time_remaining, self.game_map.game_starbases))
        self.display()
    
    @staticmethod
    def mainloop():
        import traceback
        game = Game()
        try:
            game.run()
        except Exception as ex:
            print(ex)
            # Stack trace:
            traceback.print_exc() 


Game.mainloop()
 
