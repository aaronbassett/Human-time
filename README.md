# Don't use yet

I still haven't sorted out the exact time increments and what it should say for each. 
At present it only has a few inacurrate basic phrases I've added. These will be expanded upon 
and an actual rational reason as to when phrases change.

# Quick Start

**On OSX**

    python human_time.py | say

**On Ubuntu**

    python human_time.py | espeak

**In your own Python scripts**

    import human_time
    
    print human_time.human_time()

You can also pass in your own datetime object

    from datetime import datetime
    import human_time
    
    human_time.human_time(datetime(2011, 9, 1, 1, 2))