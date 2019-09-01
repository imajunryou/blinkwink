Hi.  This is a tinker-toy website that I use to experiment with things.

What follows is just a vague outline of to-do's or a wishlist, sorta.

Things that I vaguely want to try my hand at, or would like to see exist, or that sound interesting to tinker on.

In no particular order at the top level:

- **Portfolio** Somewhere that I can point people when they ask "so, what've you been working on?"
- **Character sheet manager** I fiddle with a few roleplaying games, occasionally, and always get an itch to build a better character sheet.  It is an idea that's been done to death, but not by me.  Yet.  A few of the flavors on my itches-to-scratch list:
  - *World of Darkness* The "New" World of Darkness, but not the "Chronicles of Darkness".  I've got a bookcase of the former, none of the latter, and I wanna play with what I've got, for now.
  - *Planet Mercenary* Fresh off the presses, it is pretty neat!  Based in the "Schlock Mercenary" universe, its fast-paced mechanics and Mayhem system look like a hoot.
  - *GURPS* I love the amount of variation and complexity that can go into this, and how light-weight it can be if you prune everything back.
  - *Eclipse Phase* I've yet to actually play it!  I've got a handful of the books, but haven't even gone through them enough to really wrap my head around the core mechanics.  It looks shiny, though.  Shiny and grim, with a dash of distant hope.
  - *Dungeon World* A friend of mine has been tinkering with this system a bunch, and so it has come to my attention as a thing to poke at.  Maybe I will.
- **Bookmark manager** I'm not interested in hosting other people's bookmarks, or making mine public, per se, but I'm rather dissatisfied with the various tools that I've come across to coordinate my bookmarks across computers and devices, especially when some of the computers are shared or I only want a subset of bookmarks on a device.  I'd like to try my hand at making something more aligned with my needs.
  - *Public/Private distinction* I'd like to be able to have some bookmarks available from anywhere, and other bookmarks available when I log in.  The former I can easily point people to.  The latter, I can access when convenient (and when there's wifi, I suppose)
  - *Duplicate detection* Years of collecting bookmarks between multiple computers, and half-heartedly trying to organize them together has left me with thousands of bookmarks, and hundreds of duplicates.  I'd like an efficient way of just... cleaning those up.  I'd like to do so in a way where I have fine control over precisely which ones out of a set of duplicates get cleared out, rather than just automating it away, too.  Automate the detection, sure, but informative, fine control for the actual work.
  - *Descriptions* Pretty standard.  A quippy one-liner or so, in case the link itself is opaque.
  - *Tags* Also pretty standard.  One or more words or phrases to categorize a link so that I can find it and other similar to it, with minimal hassle.
- **Blog** It's the done thing, is it not?  I suppose I might as well get something up.
  - *Articles* What's a blog with an article or two?
  - *Math support* Delicious formulas!  Graphs!  Maybe some interactivity?!
  - *Code support* At least the normal HTML code blocks, but ideally something slightly more interactive.  What, particularly?  I dunno.  Maybe nothing... But... Maybe *something*...
- **Notepad** Sticky notes on a canvas?  Hierarchical document structure?  Something with nodes and edges?!  Something with rich text?!  Something where I can make a quick note, or write a chunk of stuff, and be able to easily find and reference it later.

# To Build This Project

To build this project locally, the following steps must be performed (I think; let me know if it seems I missed something):

- Clone the repository
- Create a local Python virtual environment
- Activate the new virtual environment
- Install the various dependencies found in `Requirements.txt`
- Create a file called `settings.cfg` in `/blinkwink/blinkwink` at the same level as `config.py`
   - This file should contain the following two lines:
   - `WTF_CSRF_ENABLED = True`
   - `SECRET_KEY = "Your super-secret key that you should never share with anyone"`
- Set up an environment variable to point at this file:

```bash
export BLINKWINK_CONFIG=settings.cfg
```

# To Run This Project Locally

Once you have a local copy, fire off `manage.py` with the `runserver` argument:

```bash
python3 manage.py runserver
```

By default, this will start running on port 5000.
