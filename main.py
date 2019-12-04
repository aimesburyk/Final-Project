import random
## Introducing the player to the game with some of the info they'll need to get started.
print("Welcome to The Journey.")
print("")
name = input("Enter your Name: ")
print("")
print("You will start your journey in your senior season of high school cross country. You are a top recruit in the nation looking to commit to an elite program.")
high_school = input("Enter the name of your high school: ")
print("Going into your season you already have three schools you're very interested in. Go ahead and list those schools below.")
school_one = input("School one: ")
school_two = input("School two: ")
school_three = input("School three: ")
print("")
print("These schools are interested in you but you must earn a scholarship in order to be on the team. Make the correct decisions and you may even be able to go pro after a collegiate career.")
print("Make sure to not only focus on making the correct decisions for running but to stay happy throughout the season so you can continue to run well.")
print("")
print("TIP: While answering the questions to choose your path make sure nothing is capitalized and spelling is correct for best results.")
print("")
print("First day of practice.")
print("")
print("")
Q1 = input("Your coach offers you the captain position on your team. Do you accept this responsibility? (yes/no):  ")
print("")
## if user answers yes they will go down path number one where all of the questions "Q#" will be odd numbers
if Q1 == "yes":
  Q3 = input("Congratulations on accepting this honor! Your first job as a captain will be to organize a team building activity. What would you rather do (ultimate frisbee/pasta party):  ")
  ## there is a 10% chance on this path that the game could end due to an injury to the main player 
  num = random.randint(1,10)
  if Q3 == "ultimate frisbee":
    if num == 1:
      print("You stepped in a hole and broke your ankle while playing. Your season and career is over.")
      print("GAME OVER")
    else:
      print("Everyone enjoyed the game and you Proved yourself a true leader for the season to come.")
      print("")
      print("First meet of the year")
      print("")
      Q9 = input("You prepare to run your first meet of your senior season. Do you take it out aggressive or conservative? (aggressive/conservative): ")
      if Q9 == "aggressive":
        Q19 = input("You take this first race out aggressive.")
      else:
        Q21 = input("You decide to take this first race out at a safe pace to save more energy for the end. You end up getting boxed in a large group of runners. The only way out is to cut off one of your teammates. Do you stay boxed in or cut off your teammate to break out? (boxed in/cut off): ")
        if Q21 == "boxed in":
          print("You ended up making your way out of the pack and moved up. It was too little too late though and you only finished in 21st place among the field. On to the next race.")
          print("")
          Q25 = input("You are frustrated with how the last race went. Do you have a team meeting to tell your teammates to run better as a team or bite your tongue? (team meeting/bite tongue): ")
          if Q25 == "team meeting":
            print("You call your team together to tell them to help eachother run better in races. they all understand and respect what you told them.")
            print("")
            print("Second race")
            print("")
            Q27 = input("You are looking to have a better showing this race. Do you go out aggressive this time or trust your teammates and run as a pack? (aggressive/pack run")
            if Q27 == "aggressive":
              print("")
            else:
              print("")
          else:
            print("You decide to bite your tongue and feel it's better you don't lecture your team on teamwork.")
            print("")
            print("Second race")
            print("")
            Q29 = input("This second race you are looking to ")
        else:
          print("You try to breakout out of the group by cutting off one of your teammates. You end up getting tangled up with your teammate and you both fall. You do not finish the race.")
          print("")
          print("You tore a calf muscle during your last race and will miss your next race. You now only have one race remaining to impress a coach.")
          print("")
          print("Final meet")
          print("")
          Q23 = input("This is your last chance to impress a coach. Your calf is still feeling a little sore. Do you take this next race more aggressive or hold back to keep your calf healthy? (aggressive/play it safe): ")
          if Q23 == "aggressive":
            print("")
          else:
            print("")
  else:
    Q7 = input("You invited your whole team over to your house for a pasta party and everyone is having fun. They want you to go with them to TP a rivals school runners house. Do you go with them? (go/dont): ")
    if Q7 == "go":
      Q11 = input("You go with your team and TP the runners house. Their parents came out and you all start to run away! Do you run to your car or hide in a nearby bush? (car/bush): ")
    else:
      print("You decided not to go and stay at home instead.")
      print("")
      print("First meet of the year")
      print("")
      Q13 = input("You just finished an easy run before your first meet. Do you ice bath before the meet or just go home to rest tonight? (ice bath/rest):  ")
      if Q13 == "ice bath":
        Q15 = input("")
      else:
        Q17 = input("")
        ## This is the start of the second option where all of the questions "Q#" will be even numbers
else:
  Q2 = input("You decide not to accept the position and focus on yourself for the season. Practice is starting up and you are deciding between running with the other varsity runners or doing your own thing and running ahead of them to train harder. What will you do? (run with group/do my own thing):  ")
  if Q2 == "run with group":
    print("")
    print("You decide to run with your other varsity runners. You all continue to push each other to get better.")
    print("")
    print("First meet of the year")
    print("")
    Q4 = input("You just finished an easy run before your first meet. Do you ice bath before the meet or just go home to rest tonight? (ice bath/rest): ")
    if Q4 == "ice bath":
      print("")
      Q8 = input("You decided to take the ice bath and suffer through the cold. When you get home you remember you have a paper you haven't done yet at 11:59. Do you go to bed to be well rested for the meet or work on your paper to turn it in? (sleep/write paper): ")
      if Q8 == "sleep":
        print("")
        print("You choose to get some sleep and be well rested.")
        print("")
        print("meet day")
        print("")
        Q10 = input("")
      else:
        print("")
        input("You decided to stay up and write the paper and turned it in just in time! You still have to get your running gear around so it'll be a late night.")
        print("")
    else:
      print("")
      input("You decided to go home to rest.")
      print("")
  else:
    print("")
    print("You decided to do your own thing and run ahead of the group to push yourself.")
    print("")
    print("First meet of the year")
    print("")
    Q6 = input("You just finished an easy run before your first meet. Do you ice bath before the meet or just go home to rest tonight? (ice bath/rest): ")
    if Q6 == "ice bath":
      print("You choose to take an ice bath")
      print("")
      print("First meet of the year")
      print("")
      Q12 = input("You'll need to set the tone for the rest of the season. Do you go out hard and push for the front or stay conservative and stay consistent throughout the race? (aggressive/ conservative)")
      if Q12 == "aggressive":
        Q14 = input("You are running great and are 5th with half a mile left. do you push for the lead now or wait till the last 100M? (now/wait)")
        if Q14 == "now":
          print("You go with half a mile to go and have an amazing finish to win the race!!")
          Q22 = input("Do you go out and celebrate your victory at a party or move on to the next race? (party/move on)")
          if Q22 == "party":
            print("You decide to go out and party. The party gets busted but you run and make it home safe.")
            print("")
            print("Second Meet of the year")
            print("")
            Q26 = input("Your leg is feeling a little sore from when you ran from the cops. Do you take this race out a little slower to feel out your leg or keep with your aggressive start? (go easy/aggressive): ")
        else:
          print("You wait till the last 100M and make a move that bumps you up. You finish 3rd with a great PR.")
          Q24 = input("After your 3rd place finish are you satisfied and take the rest of the day off and take it easy or are you unsatisfied and go for another training run to try and get closer to winning races? (rest/run)")
          if Q24 == "rest":
            print("You take the rest of the day off.")
            print("")
            print("Second meet of the year")
            print("")
            print("You're looking to make")
          else:
            print("You are unsatisfied with the results and decide to run again. You end up overworking your body and get a stress fracture ending your season")
            print("")
            print("GAME OVER")  
      else:
        Q16 = input("You wait back and get caught in a large group with 1 mile left. Do you break out and let loose or stay conservative? (let loose/conservative)")
        if Q16 == "let loose":
          print("you decide to let loose and you make up a lot of ground but you waited too long. You finish 27th place, 2 away from medaling.")
          Q18 = input("After your rough race one of the coaches recruiting you calls you. Do you answer the phone or ignore the call? (answer/ignore)")
        else:
          print:("You decided to stay conservative. You finish in the middle of the pack and your college hopes aren't looking great.")
          Q20 = input("You need to do something to move up in the pack quick. Do you talk to your coach about adding more mileage in training or about changing race strategy? (mileage/strategy)")
          if Q20 == "mileage":
            print("You talk to your coach about adding mileage to your training. You over work your body and are unable to perform the rest of the season")
            print("")
            print("GAME OVER")
          else:
            Q26 = input("You talk to your coach about changing your strategy where he recommends going out harder. Do you take his advice or keep your old strategy? (take advice/ignore)")
            if Q26 == "take advice":
              print("")
              print("Second meet of the year")
              print("")
              Q28 = input("It's time to take the advice of your coach and go out harder. Do you follow through with your new strategy? (yes/no)")
              if Q28 == "yes":
                Q34 = input("Your new strategy sets you up much better for the last 400M. Your are in 12th place with time to make one final move. Do you start your kick now or wait until 200M left? (now/wait)")
                if Q34 == "now":
                  print("You go now which is a tad too early. You die off in the end but still gain one position to finish 11th.")
                  print("")
                  print("You are now moving onto your final race of the season. The state meet. This is the best time to impress your colleges.")
                  print("")
                  print("STATE MEET")
                  print("")
                  Q36 = input("")
              else:
                Q32 = input("You once again start the race conservative and are stuck in the middle of the pack. You become frustrated, do you drop out of the race or continue? (drop/continue)")
            else:
              print("")
              print("Second meet of the year")
              print("")
              Q30 = input("You once again start the race conservative and are stuck in the middle of the pack yet again. You become frustrated, do you drop out of the race or continue? (drop/continue)")
              if Q30 == "drop":
                print("You decided to drop out of the race. You only have one more opportunity to impress your college coaches.")
                print("")
                print("Final meet of the year")
                print("")
                Q38 = input("This is your last chance of the year to make something happen. Do you decide to go aggressive or stay to your normal strategy? (aggressive/normal): ")
                if Q38 == "normal":
                  print("You did not make any adjustments to your race strategy and you had the same outcome as the other races.")
                  print("")
                  print("The definition of insanity is doing the same thing over and over again, but expecting different results.")
                  print("")
                  print("GAME OVER")
                else:
                  print("You finally decided to be aggressive but it was too little too late. Your college offers have already been pulled.")
                  print("")
                  print("GAME OVER")
              else:
                print("you decide to continue running the race and finish 32nd overall. You have one last opportunity to impress college coaches.")
                print("")
                print("Final meet of the year")
                print("")
                Q40 = input("This is your last opportunity to make a college coach impressed. Do you switch your race strategy to a more aggressive approach or stick with a steady race? (aggressive/steady): ")
                if Q40 == "aggressive":
                  Q42 = input("Your race goes much better and you are in the top 10 halfway through the race. Do you stay aggressive and keep moving up or do you become conservative to try and hold onto this position? (aggressive/conservative): ")
                  if Q42 == "aggressive":
                    print("You moved all the way up to 3rd place before having to pull of the course and puke. You continued running but ended all the way back in 40th place.")
                    print("")
                    print("You had a good season.")
                    print("")
                    print("Just not good enough...")
                    print("")
                    print("GAME OVER")
                  else:
                    print("You played it safe and it worker out. You finish in 8th place.")
                    print("")
                    print("Your season is now over. Time to see if any coaches offered you...")
                    print("")
                    print("You received an offer of a partial scholarship from " + school_three + "! Congratulations! You're ready for the next step in your running career.")
                    print("")
                    print("To be continued...")
                else:
                  print("You stay conservative and get the same results as every other meet. You get no college offers.")
                  print("")
                  print("The definition of insanity is doing the same thing over and over, but expecting different results.")
                  print("")
                  print("GAME OVER")

    

