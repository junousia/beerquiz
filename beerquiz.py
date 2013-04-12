#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
from pynt.pynt import Settings, Beer
from random import randint
import sys

Settings.host           = 'http://api.openbeerdatabase.com/v1/'
Settings.public_token   = 'db198084eb53128e0fb7246d00aa424ab2fc28d713b43d0df5908652f4a8af4c'
Settings.private_token  = '01ae167826935d3cbc0421cd0caa787d4c4a8cf60f5becc796af7566dbaa3711'

def main():
    beers = Beer.all()["beers"]    
    beer = beers[randint(0,len(beers)-1)]

    while 1:
        print "Which beer is this? \"{}\"".format(beer["description"].encode('utf-8'))

        if raw_input('Your guess: ') == beer["name"]:
            print "Correct answer, well done!"
            return
        else:
            print "Wrong answer, correct answer is {}\n".format(beer["name"].encode('utf-8'))
            beer = beers[randint(0,len(beers)-1)]

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\nQuitting...\n"